<script setup>
import { useContent } from '../composables/useContent'
import { pages } from '../pages'
import { fileName } from '../utils/fileName'

const { lang, t } = useContent()
</script>

<template>
  <aside class="sidebar">
    <p class="sidebar-title">EXPLORER</p>
    <nav>
      <!-- RouterLink setzt für die aktive Seite automatisch aria-current="page" -->
      <RouterLink
        v-for="(page, index) in pages"
        :key="page.key"
        :to="{ name: page.key, params: { lang } }"
      >
        <span class="arrow" aria-hidden="true">▸</span> {{ fileName(index, t.nav[page.key]) }}
      </RouterLink>
    </nav>
  </aside>
</template>
