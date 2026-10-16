import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// base: '/' passt für https://trancemeli.github.io/ (Repo "TranceMeli.github.io").
// Liegt das Projekt in einem normalen Repo (z. B. "bewerbung"), muss hier
// '/bewerbung/' stehen, weil die Seite dann unter /bewerbung/ ausgeliefert wird.
export default defineConfig({
  base: '/',
  plugins: [vue()],
})
