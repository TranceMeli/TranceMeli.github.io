<script setup>
import { computed } from 'vue'

// Stellt einfache Auszeichnungen aus den Content-Dateien dar:
//   **fett**   *kursiv*   [Linktext](https://…)   \n = Zeilenumbruch
// Es wird bewusst kein v-html benutzt: Der Text wird in Teile zerlegt und als
// normale Vue-Elemente gerendert, so kann kein fremdes HTML eingeschleust werden.
const props = defineProps({
  text: { type: String, required: true },
})

const TOKEN = /\*\*(.+?)\*\*|\*(.+?)\*|\[(.+?)\]\((.+?)\)|\n/g

const safeUrl = (url) => (/^(https?:\/\/|mailto:)/.test(url) ? url : '#')

const parts = computed(() => {
  const result = []
  let last = 0

  for (const match of props.text.matchAll(TOKEN)) {
    if (match.index > last) {
      result.push({ type: 'text', value: props.text.slice(last, match.index) })
    }
    if (match[1] !== undefined) result.push({ type: 'strong', value: match[1] })
    else if (match[2] !== undefined) result.push({ type: 'em', value: match[2] })
    else if (match[3] !== undefined) result.push({ type: 'link', value: match[3], href: safeUrl(match[4]) })
    else result.push({ type: 'br' })
    last = match.index + match[0].length
  }

  if (last < props.text.length) {
    result.push({ type: 'text', value: props.text.slice(last) })
  }
  return result
})
</script>

<template>
  <template v-for="(part, i) in parts" :key="i">
    <strong v-if="part.type === 'strong'">{{ part.value }}</strong>
    <em v-else-if="part.type === 'em'">{{ part.value }}</em>
    <a v-else-if="part.type === 'link'" :href="part.href" target="_blank" rel="noopener">{{ part.value }}</a>
    <br v-else-if="part.type === 'br'" />
    <template v-else>{{ part.value }}</template>
  </template>
</template>
