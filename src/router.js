import { createRouter, createWebHashHistory } from 'vue-router'
import { languages, defaultLanguage } from './config'
import { pages } from './pages'

// URLs sehen so aus: /#/de/cv  oder  /#/en/projects
const langPattern = languages.join('|')

const routes = [
  { path: '/', redirect: `/${defaultLanguage}/home` },
  ...pages.map((page) => ({
    path: `/:lang(${langPattern})/${page.key}`,
    name: page.key,
    component: page.component,
  })),
  {
    path: `/:lang(${langPattern})`,
    redirect: (to) => ({ name: 'home', params: { lang: to.params.lang } }),
  },
  { path: '/:pathMatch(.*)*', redirect: '/' },
]

export const router = createRouter({
  // Hash-Modus: funktioniert auf GitHub Pages ohne Server-Konfiguration,
  // auch beim Neuladen einer Unterseite.
  history: createWebHashHistory(),
  routes,
  scrollBehavior: () => ({ top: 0 }),
})
