<script setup>
import { useContent } from '../composables/useContent'
import RichText from '../components/RichText.vue'

const { t } = useContent()
</script>

<template>
  <article class="page letter">
    <h1>{{ t.letter.title }}</h1>
    <p class="subtitle"><RichText :text="t.letter.subtitle" /></p>

    <p v-for="(paragraph, i) in t.letter.paragraphs" :key="i">
      <RichText :text="paragraph" />
    </p>

    <p class="signature"><RichText :text="t.letter.closing" /></p>
  </article>
</template>
