<script setup>
import { computed, onMounted, onUnmounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { useContent } from '../composables/useContent'
import { slugOf } from '../utils/fileName'

const route = useRoute()
const { t } = useContent()

// Der Tipp-Effekt läuft nur beim ersten Laden der Seite, nicht bei jedem Blättern
let typed = false

const full = computed(() => t.value.header.wordmark)
const shown = ref(typed ? full.value.length : 0)
let timer

onMounted(() => {
  if (typed || window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    shown.value = full.value.length
    typed = true
    return
  }
  timer = setInterval(() => {
    shown.value += 1
    if (shown.value >= full.value.length) {
      clearInterval(timer)
      typed = true
    }
  }, 65)
})
onUnmounted(() => clearInterval(timer))

const slug = computed(() => slugOf(t.value.nav[route.name] ?? 'home'))

// print("…"): Schlüsselwort cyan, Text in Anführungszeichen gelb
const typedParts = computed(() => {
  const text = full.value.slice(0, shown.value)
  const keyword = text.slice(0, 5)
  const rest = text.slice(5)
  const quote = rest.indexOf('"')
  return quote < 0
    ? { keyword, before: rest, string: '' }
    : { keyword, before: rest.slice(0, quote), string: rest.slice(quote) }
})
</script>

<template>
  <div class="editor-head" aria-hidden="true">
    <div class="ln"><b>1</b><span class="c"># {{ t.meta.title }}</span></div>
    <div class="ln">
      <b>2</b><span><span class="k">from</span> portfolio <span class="k">import</span> {{ slug }}</span>
    </div>
    <div class="ln">
      <b>3</b>
      <span>
        <span class="k">{{ typedParts.keyword }}</span>{{ typedParts.before }}<span class="s">{{ typedParts.string }}</span><span class="cur"></span>
      </span>
    </div>
  </div>
</template>
