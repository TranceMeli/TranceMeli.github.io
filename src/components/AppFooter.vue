<script setup>
import { onMounted, onUnmounted, ref } from 'vue'
import { useContent } from '../composables/useContent'
import { links } from '../content/shared'

const { t } = useContent()

// Der Text tippt sich einmal, sobald die Fußzeile sichtbar wird (nicht bei jedem Blättern)
let typed = false

const footer = ref(null)
const shown = ref(typed ? t.value.footer.cta.length : 0)
let observer
let timer

function type() {
  const full = t.value.footer.cta
  timer = setInterval(() => {
    shown.value += 1
    if (shown.value >= full.length) {
      clearInterval(timer)
      typed = true
    }
  }, 22)
}

onMounted(() => {
  if (typed || window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    shown.value = t.value.footer.cta.length
    typed = true
    return
  }
  observer = new IntersectionObserver(
    ([entry]) => {
      if (!entry.isIntersecting) return
      observer.disconnect()
      type()
    },
    { threshold: 0.6 },
  )
  observer.observe(footer.value)
})

onUnmounted(() => {
  observer?.disconnect()
  clearInterval(timer)
})
</script>

<template>
  <footer ref="footer" class="site-footer">
    <span class="prompt" aria-hidden="true">❯</span>
    <p class="cta">
      <span class="sr-only">{{ t.footer.cta }}</span>
      <span aria-hidden="true">{{ t.footer.cta.slice(0, shown) }}</span>
    </p>
    <p class="contact">
      <a v-for="link in links" :key="link.label" :href="link.href" target="_blank" rel="noopener">
        {{ link.label }}
      </a>
    </p>
    <span class="cur" aria-hidden="true"></span>
  </footer>
</template>
