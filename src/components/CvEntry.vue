<script setup>
import RichText from './RichText.vue'

// Ein Eintrag im Lebenslauf (Ausbildung, Projekt, Station, …)
defineProps({
  title: { type: String, required: true },
  meta: { type: String, default: '' },
  tech: { type: String, default: '' },
  paragraphs: { type: Array, default: () => [] },
  bullets: { type: Array, default: () => [] },
})
</script>

<template>
  <div class="entry">
    <h3>{{ title }}</h3>
    <p v-if="meta" class="entry-meta"><RichText :text="meta" /></p>
    <p v-if="tech" class="tech">{{ tech }}</p>
    <p v-for="(text, i) in paragraphs" :key="`p${i}`"><RichText :text="text" /></p>
    <ul v-if="bullets.length">
      <li v-for="(text, i) in bullets" :key="`b${i}`"><RichText :text="text" /></li>
    </ul>
  </div>
</template>
