"""Erzeugt Vorschaubilder (240 px breit, WebP) für alle Screenshots in src/data/projects.json.

Benutzung (im Projektordner):
    pip install pillow
    python scripts/make_thumbnails.py          # nur fehlende Vorschauen erzeugen
    python scripts/make_thumbnails.py --all    # alle neu erzeugen

Die Vorschauen landen in src/assets/thumbs/<projekt-id>-<nr>.webp. Fehlt eine Vorschau,
lädt die Seite stattdessen das Originalbild (funktioniert, ist aber schwerer).
"""
import io
import json
import sys
import urllib.request
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "src" / "data" / "projects.json"
OUT = ROOT / "src" / "assets" / "thumbs"
WIDTH = 240


def main(force: bool = False) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    projects = json.loads(DATA.read_text(encoding="utf-8"))["projects"]
    made = skipped = failed = 0

    for project in projects:
        for index, url in enumerate(project.get("screenshots", [])):
            target = OUT / f"{project['id']}-{index}.webp"
            if target.exists() and not force:
                skipped += 1
                continue
            try:
                request = urllib.request.Request(url, headers={"User-Agent": "thumbnail-script"})
                with urllib.request.urlopen(request, timeout=30) as response:
                    data = response.read()
                image = Image.open(io.BytesIO(data)).convert("RGB")
                height = round(image.height * WIDTH / image.width)
                image.resize((WIDTH, height), Image.LANCZOS).save(target, "WEBP", quality=78, method=6)
                made += 1
            except Exception as error:  # Netzwerk- oder Bildfehler: weitermachen
                failed += 1
                print(f"Übersprungen: {project['id']} #{index}: {error}")

    print(f"Fertig: {made} erzeugt, {skipped} vorhanden, {failed} fehlgeschlagen.")


if __name__ == "__main__":
    main(force="--all" in sys.argv)
