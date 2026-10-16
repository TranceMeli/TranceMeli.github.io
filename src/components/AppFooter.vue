<script setup>
import { useContent } from '../composables/useContent'
import { links } from '../content/shared'

const { t } = useContent()
</script>

<template>
  <footer class="site-footer">
    <p class="cta">{{ t.footer.cta }}</p>
    <p class="contact">
      <a v-for="link in links" :key="link.label" :href="link.href" target="_blank" rel="noopener">
        {{ link.label }}
      </a>
    </p>
  </footer>
</template>
