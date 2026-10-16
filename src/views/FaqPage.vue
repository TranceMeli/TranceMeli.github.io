<script setup>
import { useContent } from '../composables/useContent'
import RichText from '../components/RichText.vue'
import ContactLinks from '../components/ContactLinks.vue'

const { t } = useContent()
</script>

<template>
  <article class="page faq">
    <h1>{{ t.faq.title }}</h1>

    <div class="faq-meta">
      <p class="faq-name"><strong>{{ t.faq.name }}</strong></p>
      <p class="faq-role"><em>{{ t.faq.role }}</em></p>
      <p class="faq-links"><ContactLinks /></p>
    </div>

    <blockquote>{{ t.faq.intro }}</blockquote>

    <details v-for="(item, i) in t.faq.items" :key="i">
      <summary>{{ item.q }}</summary>
      <div class="answer">
        <p v-for="(paragraph, j) in item.a" :key="j"><RichText :text="paragraph" /></p>
      </div>
    </details>
  </article>
</template>
