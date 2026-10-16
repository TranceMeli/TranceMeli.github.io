<script setup>
import { computed } from 'vue'
import { thumbnailFor } from '../data/thumbnails'

const props = defineProps({
  project: { type: Object, required: true },
  lang: { type: String, required: true },
  labels: { type: Object, required: true },
})

// "open" wird mit den Daten für das Bild-Modal ausgelöst (die Seite zeigt das Modal)
const emit = defineEmits(['open'])

// Texte in der aktuellen Sprache, sonst Deutsch als Rückfall
const text = computed(() => props.project[props.lang] ?? props.project.de ?? {})
const title = computed(() => text.value.title ?? props.project.title)
const screenshots = computed(() => props.project.screenshots ?? [])

// Kleine Vorschau, sonst das Originalbild
const thumbSrc = (index) => thumbnailFor(props.project.id, index) ?? screenshots.value[index]

const open = (index) => emit('open', { title: title.value, images: screenshots.value, index })
</script>

<template>
  <article class="project-card">
    <div class="project-head">
      <h3>{{ title }}</h3>
      <span v-if="project.status === 'wip'" class="badge-wip">{{ labels.wip }}</span>
    </div>
    <p v-if="text.subtitle" class="project-subtitle">{{ text.subtitle }}</p>

    <!-- Screenshots: kleine Vorschau, Klick öffnet das Bild groß im Modal -->
    <ul v-if="screenshots.length" class="thumbs">
      <li v-for="(url, index) in screenshots" :key="url">
        <button
          type="button"
          class="thumb"
          :aria-label="`${labels.enlarge}: ${title} (${index + 1}/${screenshots.length})`"
          @click="open(index)"
        >
          <img :src="thumbSrc(index)" alt="" loading="lazy" decoding="async" />
        </button>
      </li>
    </ul>

    <ul v-if="project.tech?.length" class="tags">
      <li v-for="tech in project.tech" :key="tech">{{ tech }}</li>
    </ul>

    <ul v-if="text.highlights?.length" class="highlights">
      <li v-for="item in text.highlights" :key="item">{{ item }}</li>
    </ul>

    <div v-if="project.repo || project.demo" class="project-links">
      <a v-if="project.repo" :href="project.repo" target="_blank" rel="noopener">{{ labels.code }}</a>
      <a v-if="project.demo" :href="project.demo" target="_blank" rel="noopener">{{ labels.demo }}</a>
    </div>
  </article>
</template>
