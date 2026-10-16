import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { defaultLanguage } from '../config'
import de from '../content/de'
import en from '../content/en'

const content = { de, en }

// Liefert die aktuelle Sprache (aus der URL) und die passenden Texte.
// Ändert sich die URL (z. B. /de/cv → /en/cv), aktualisieren sich alle
// Komponenten, die `t` benutzen, automatisch.
export function useContent() {
  const route = useRoute()
  const lang = computed(() => (route.params.lang in content ? route.params.lang : defaultLanguage))
  const t = computed(() => content[lang.value])
  return { lang, t }
}
