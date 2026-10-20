"""Entfernt Metadaten aus Bildern, ohne die Bilddaten neu zu kodieren (verlustfrei).

Entfernt werden u. a. EXIF (Kamera, Datum, GPS), XMP, IPTC/Photoshop-Blöcke, Kommentare
und eingebettete Herkunftsnachweise (C2PA / "Content Credentials"). Behalten werden das
Bild selbst und das Farbprofil (ICC), damit die Farben gleich bleiben.

Benutzung (im Projektordner):
    python scripts/strip_metadata.py --check            # nur anzeigen, was entfernt würde
    python scripts/strip_metadata.py                    # alle Bilder in src/assets bereinigen
    python scripts/strip_metadata.py pfad/zum/bild.jpg  # einzelne Dateien oder Ordner

Unterstützt: JPG/JPEG, PNG, WebP. Es werden keine Abhängigkeiten benötigt.
"""
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DIR = ROOT / "src" / "assets"


def strip_jpeg(data: bytes) -> bytes:
    if data[:2] != b"\xff\xd8":
        return data
    out = bytearray(b"\xff\xd8")
    i = 2
    while i < len(data):
        if data[i] != 0xFF:
            break
        marker = data[i + 1]
        if marker == 0xDA:  # Beginn der Bilddaten: Rest unverändert übernehmen
            out += data[i:]
            return bytes(out)
        if 0xD0 <= marker <= 0xD7 or marker in (0x01, 0xD8):  # Marker ohne Länge
            out += data[i:i + 2]
            i += 2
            continue
        length = struct.unpack(">H", data[i + 2:i + 4])[0]
        segment = data[i:i + 2 + length]
        payload = segment[4:]
        keep = True
        if marker == 0xFE:                      # Kommentar
            keep = False
        elif 0xE1 <= marker <= 0xEF:            # APP1..APP15: EXIF, XMP, IPTC, C2PA, ...
            keep = (marker == 0xE2 and payload.startswith(b"ICC_PROFILE")) or marker == 0xEE  # ICC + Adobe-Farbinfo
        if keep:
            out += segment
        i += 2 + length
    return bytes(out)


def strip_png(data: bytes) -> bytes:
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        return data
    keep = {b"IHDR", b"PLTE", b"IDAT", b"IEND", b"tRNS", b"gAMA", b"cHRM", b"sRGB", b"iCCP", b"pHYs", b"sBIT",
            b"acTL", b"fcTL", b"fdAT"}
    out = bytearray(data[:8])
    i = 8
    while i < len(data):
        length = struct.unpack(">I", data[i:i + 4])[0]
        ctype = data[i + 4:i + 8]
        chunk = data[i:i + 12 + length]
        if ctype in keep:
            out += chunk
        i += 12 + length
    return bytes(out)


def strip_webp(data: bytes) -> bytes:
    if data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        return data
    keep = {b"VP8 ", b"VP8L", b"VP8X", b"ALPH", b"ANIM", b"ANMF", b"ICCP"}
    chunks = []
    i = 12
    while i + 8 <= len(data):
        ctype = data[i:i + 4]
        size = struct.unpack("<I", data[i + 4:i + 8])[0]
        payload = data[i + 8:i + 8 + size]
        pad = b"\x00" if size % 2 else b""
        if ctype in keep:
            if ctype == b"VP8X":  # Flags für EXIF (0x08) und XMP (0x04) löschen
                payload = bytes([payload[0] & ~0x0C]) + payload[1:]
            chunks.append(ctype + struct.pack("<I", size) + payload + pad)
        i += 8 + size + (size % 2)
    body = b"WEBP" + b"".join(chunks)
    return b"RIFF" + struct.pack("<I", len(body)) + body


HANDLERS = {".jpg": strip_jpeg, ".jpeg": strip_jpeg, ".png": strip_png, ".webp": strip_webp}


def collect(paths):
    for p in paths:
        p = Path(p)
        if p.is_dir():
            yield from (f for f in sorted(p.rglob("*")) if f.suffix.lower() in HANDLERS)
        elif p.suffix.lower() in HANDLERS:
            yield p


def main(args):
    check = "--check" in args
    targets = [a for a in args if not a.startswith("--")] or [DEFAULT_DIR]
    cleaned = total = 0
    for file in collect(targets):
        total += 1
        before = file.read_bytes()
        after = HANDLERS[file.suffix.lower()](before)
        if after != before:
            cleaned += 1
            print(f"{'Enthält Metadaten' if check else 'Bereinigt'}: {file}  ({len(before)} → {len(after)} Bytes)")
            if not check:
                file.write_bytes(after)
    print(f"{total} Bilder geprüft, {cleaned} {'mit Metadaten' if check else 'bereinigt'}.")


if __name__ == "__main__":
    main(sys.argv[1:])
