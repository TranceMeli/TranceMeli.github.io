<script setup>
import { useContent } from '../composables/useContent'
import { pages } from '../pages'

const { lang, t } = useContent()

const number = (index) => String(index + 1).padStart(2, '0')
</script>

<template>
  <aside class="sidebar">
    <nav>
      <!-- RouterLink setzt für die aktive Seite automatisch aria-current="page" -->
      <RouterLink
        v-for="(page, index) in pages"
        :key="page.key"
        :to="{ name: page.key, params: { lang } }"
      >
        {{ number(index) }} {{ t.nav[page.key] }}
      </RouterLink>
    </nav>
  </aside>
</template>