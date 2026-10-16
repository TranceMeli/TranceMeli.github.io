<script setup>
import { computed } from 'vue'
import { useContent } from '../composables/useContent'
import RichText from '../components/RichText.vue'

const { t } = useContent()

// Alle Bilder aus src/assets/certificates/ einlesen. Der Dateiname ohne Endung
// ist die "id" des Eintrags in content/de.js und en.js (certificates.items).
// Fehlt eine Datei, bricht der Build nicht ab – die Seite zeigt dann einen Hinweis.
const files = import.meta.glob('../assets/certificates/*.{jpg,jpeg,png,webp}', {
  eager: true,
  query: '?url',
  import: 'default',
})

const urlById = Object.fromEntries(
  Object.entries(files).map(([path, url]) => [path.split('/').pop().replace(/\.[^.]+$/, ''), url]),
)

const items = computed(() =>
  t.value.certificates.items.map((item) => ({ ...item, url: urlById[item.id] ?? null })),
)
</script>

<template>
  <article class="page certificates">
    <h1>{{ t.certificates.title }}</h1>
    <p class="subtitle">{{ t.certificates.subtitle }}</p>

    <template v-for="item in items" :key="item.id">
      <figure v-if="item.url" class="certificate">
        <a :href="item.url" target="_blank" rel="noopener">
          <img :src="item.url" :alt="item.alt" loading="lazy" />
        </a>
        <figcaption><RichText :text="item.caption" /></figcaption>
      </figure>
      <p v-else>{{ t.certificates.missing }}</p>
    </template>
  </article>
</template>
