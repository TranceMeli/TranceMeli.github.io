import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// base: '/' passt für https://trancemeli.github.io/ (Repo "TranceMeli.github.io").
// Liegt das Projekt in einem normalen Repo (z. B. "bewerbung"), muss hier
// '/bewerbung/' stehen, weil die Seite dann unter /bewerbung/ ausgeliefert wird.
export default defineConfig({
  base: '/',
  plugins: [vue()],
  build: {
    // Auch kleine Bilder (Screenshot-Vorschauen) als eigene Dateien ausliefern,
    // damit sie lazy nachgeladen werden und das JavaScript klein bleibt.
    assetsInlineLimit: 0,
  },
})
