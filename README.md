<p align="center">
  <img src="https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=white" alt="Vue.js" />
  <img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white" alt="Vite" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions" />
  <img src="https://img.shields.io/badge/GitHub_Pages-222222?style=for-the-badge&logo=githubpages&logoColor=white" alt="GitHub Pages" />
</p>

# Digitales Bewerbungsportfolio / Digital Application Portfolio

Meine Bewerbungsmappe als Webseite im Prospekt-Stil, auf Deutsch und Englisch, gebaut mit Vue 3 und Vite.
My application folder as a brochure-style website in German and English, built with Vue 3 and Vite.

## Starten / Run locally

Voraussetzung: Node.js 20.19+ oder 22.12+ / Requires Node.js 20.19+ or 22.12+.

```bash
npm install     # einmalig: Abhängigkeiten installieren
npm run dev     # Entwicklungsserver mit Live-Reload (http://localhost:5173)
npm run build   # Produktions-Build nach dist/
npm run preview # gebaute Seite lokal ansehen
```

## Struktur / Structure

```
index.html                 Einstiegsseite (nur <div id="app">)
vite.config.js             Vite-Konfiguration (base!)
.github/workflows/deploy.yml   Build + Veröffentlichung auf GitHub Pages
src/
  main.js                  Start: App, Router und Styles laden
  App.vue                  Grundgerüst: Header, Sidebar, Seite, Pager, Footer
  router.js                URLs, z. B. /#/de/cv und /#/en/projects
  pages.js                 Liste der Seiten (Reihenfolge = Blätterreihenfolge)
  config.js                Sprachen und Standardsprache
  composables/useContent.js  aktuelle Sprache + passende Texte
  content/de.js, en.js     alle Texte (Deutsch / Englisch)
  content/shared.js        Links (GitHub, LinkedIn)
  data/projects.json       Kategorien + Projekte (Projekte-Seite; Lebenslauf: nur "featured")
  components/              wiederverwendbare Bausteine
  views/                   eine Datei pro Seite
  styles/                  Farben, Schrift, Layout, Seiten
  assets/fonts/            JetBrains Mono (SIL OFL), lokal eingebunden
  assets/certificates/     Zeugnis-Bild (ihk-zeugnis.jpg)
```

## Inhalte ändern / Edit content

| Was                          | Wo                                                         |
| ---------------------------- | ---------------------------------------------------------- |
| Anschreiben, Lebenslauf, FAQ | `src/content/de.js` und `src/content/en.js`                |
| Projekte (DE/EN)             | `src/data/projects.json` – pro Projekt `category`, `tech`, `repo`, `demo`, `status` (`"wip"`), `screenshots` (Liste von URLs), `featured` (erscheint im Lebenslauf) |
| Zeugnis                      | Bild in `src/assets/certificates/` ersetzen (`ihk-zeugnis.*`) |
| Links (GitHub, LinkedIn)     | `src/content/shared.js`                                    |
| Farben                       | `src/styles/variables.css` (Palette: [ColorPalette](https://github.com/TranceMeli/ColorPalette)) |
| Neue Seite                   | View in `src/views/`, Eintrag in `src/pages.js`, Titel in `content/de.js` + `en.js` unter `nav` |

In den Texten sind `**fett**`, `*kursiv*`, `[Linktext](https://…)` und `\n` (Zeilenumbruch) möglich.
Texts support `**bold**`, `*italic*`, `[link text](https://…)` and `\n` (line break).

## Veröffentlichen / Deploy

1. Repo → **Settings → Pages → Build and deployment → Source: GitHub Actions**.
2. Änderungen nach `main` pushen. Der Workflow baut die Seite und veröffentlicht sie.
3. Die Seite erscheint unter `https://<benutzername>.github.io/`.

Liegt das Projekt in einem Repo mit anderem Namen als `<benutzername>.github.io`, in `vite.config.js` `base: '/repo-name/'` setzen.
If the repo is not named `<username>.github.io`, set `base: '/repo-name/'` in `vite.config.js`.
