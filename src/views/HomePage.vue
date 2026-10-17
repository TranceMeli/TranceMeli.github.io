<script setup>
import { useContent } from '../composables/useContent'

const { t } = useContent()

// Willkommensbild: Einfach eine Datei "welcome.jpg" (oder .png, .webp, .avif, .svg, .gif)
// in src/assets/home/ ablegen – sie ersetzt dann automatisch den Platzhalter.
// Fehlt die Datei, bricht der Build nicht ab, es erscheint der Platzhalter.
const images = import.meta.glob('../assets/home/welcome.{jpg,jpeg,png,webp,avif,svg,gif}', {
  eager: true,
  query: '?url',
  import: 'default',
})
const imageUrl = Object.values(images)[0]
</script>

<template>
  <article class="page home">
    <img v-if="imageUrl" class="home-image" :src="imageUrl" :alt="t.home.imageAlt" />
    <div v-else class="home-placeholder" aria-hidden="true">M.</div>

    <h1>{{ t.home.title }}</h1>
  </article>
</template>
