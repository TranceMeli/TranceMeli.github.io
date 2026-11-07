// Seitenname -> Dateiname im Stil eines Python-Projekts: "Lebenslauf" -> "03_lebenslauf.py"
export const slugOf = (label) =>
  label
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '_')
    .replace(/^_|_$/g, '')

export const fileName = (index, label) => `${String(index + 1).padStart(2, '0')}_${slugOf(label)}.py`
