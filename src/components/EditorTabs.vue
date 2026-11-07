<script setup>
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import { useContent } from '../composables/useContent'
import { pages } from '../pages'
import { fileName } from '../utils/fileName'

// Zuletzt besuchte Seiten bleiben als Tabs offen (wie im Editor), höchstens vier
const MAX_TABS = 4
const open = ref([])

const route = useRoute()
const { lang, t } = useContent()

watch(
  () => route.name,
  (name) => {
    if (!name || open.value.includes(name)) return
    open.value = [...open.value, name].slice(-MAX_TABS)
  },
  { immediate: true },
)

const label = (key) => fileName(pages.findIndex((page) => page.key === key), t.value.nav[key])
</script>

<template>
  <nav class="tabs" aria-hidden="false">
    <RouterLink
      v-for="key in open"
      :key="key"
      class="tab"
      :to="{ name: key, params: { lang } }"
    >
      {{ label(key) }}
    </RouterLink>
  </nav>
</template>
