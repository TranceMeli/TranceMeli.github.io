<script setup>
import { computed, onMounted, onUnmounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useContent } from '../composables/useContent'
import { pages } from '../pages'

const route = useRoute()
const router = useRouter()
const { lang, t } = useContent()

const index = computed(() => pages.findIndex((page) => page.key === route.name))
const hasPrev = computed(() => index.value > 0)
const hasNext = computed(() => index.value >= 0 && index.value < pages.length - 1)

function go(step) {
  const target = pages[index.value + step]
  if (target) router.push({ name: target.key, params: { lang: lang.value } })
}

// Pfeiltasten blättern – aber nicht bei Alt+←/→ (Browser zurück/vor)
// nicht in Eingabefeldern und nicht, während ein Modal geöffnet ist.
function onKeydown(event) {
  if (event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return
  if (event.target.closest?.('input, textarea, select, [contenteditable]')) return
  if (document.querySelector('dialog[open]')) return // Modal offen: Pfeile gehören dem Modal

  if (event.key === 'ArrowRight') go(1)
  if (event.key === 'ArrowLeft') go(-1)
}

onMounted(() => window.addEventListener('keydown', onKeydown))
onUnmounted(() => window.removeEventListener('keydown', onKeydown))
</script>

<template>
  <div class="pager">
    <button type="button" :disabled="!hasPrev" @click="go(-1)">{{ t.pager.prev }}</button>
    <button type="button" class="next" :disabled="!hasNext" @click="go(1)">
      {{ t.pager.next }}
    </button>
  </div>
</template>
