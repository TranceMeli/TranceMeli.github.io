<script setup>
import { useRoute } from 'vue-router'
import { useContent } from '../composables/useContent'
import { languages } from '../config'

const route = useRoute()
const { lang, t } = useContent()
</script>

<template>
  <header class="topbar">
    <RouterLink class="wordmark" :to="{ name: 'home', params: { lang } }">
      {{ t.header.wordmark }}
    </RouterLink>

    <p>{{ t.header.tagline }}</p>

    <!-- Sprachwechsel: gleiche Seite, andere Sprache -->
    <nav class="lang-switch" :aria-label="t.header.langLabel">
      <RouterLink
        v-for="code in languages"
        :key="code"
        :to="{ name: route.name ?? 'home', params: { lang: code } }"
        :lang="code"
        :hreflang="code"
        aria-current-value="true"
      >
        {{ code.toUpperCase() }}
      </RouterLink>
    </nav>
  </header>
</template>
