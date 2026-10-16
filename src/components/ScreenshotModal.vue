<script setup>
import { computed, onMounted, onUnmounted, ref, watch } from 'vue'

// Vergrößerte Ansicht der Screenshots in einem nativen <dialog>:
// Der Browser übernimmt Esc zum Schließen, den Fokus-Rahmen und sperrt den Hintergrund.
const props = defineProps({
  title: { type: String, required: true },
  images: { type: Array, required: true },
  startIndex: { type: Number, default: 0 },
  labels: { type: Object, required: true },
})
const emit = defineEmits(['close'])

const dialog = ref(null)
const index = ref(props.startIndex)
const failed = ref(false)

const total = computed(() => props.images.length)
const current = computed(() => props.images[index.value])

// Bei einem neuen Bild den Fehlerzustand zurücksetzen
watch(index, () => {
  failed.value = false
})

function step(delta) {
  index.value = (index.value + delta + total.value) % total.value
}

function close() {
  dialog.value?.close()
}

function onKeydown(event) {
  if (event.key === 'ArrowRight') step(1)
  else if (event.key === 'ArrowLeft') step(-1)
}

onMounted(() => {
  dialog.value.showModal()
  document.body.classList.add('modal-open') // Seite dahinter nicht mitscrollen
})

onUnmounted(() => {
  document.body.classList.remove('modal-open')
})
</script>

<template>
  <dialog
    ref="dialog"
    class="shot-modal"
    :aria-label="title"
    @close="emit('close')"
    @keydown="onKeydown"
  >
    <!-- Klick neben das Bild schließt das Modal -->
    <div class="shot-body" @click.self="close">
      <button type="button" class="shot-close" :aria-label="labels.close" @click="close">×</button>

      <button
        v-if="total > 1"
        type="button"
        class="shot-nav prev"
        :aria-label="labels.prev"
        @click="step(-1)"
      >‹</button>

      <figure class="shot-figure">
        <p v-if="failed" class="shot-error">{{ labels.error }}</p>
        <img
          v-else
          :src="current"
          :alt="`${title} (${index + 1}/${total})`"
          @error="failed = true"
        />
        <figcaption>
          {{ title }} · {{ index + 1 }}/{{ total }} ·
          <a :href="current" target="_blank" rel="noopener">{{ labels.original }}</a>
        </figcaption>
      </figure>

      <button
        v-if="total > 1"
        type="button"
        class="shot-nav next"
        :aria-label="labels.next"
        @click="step(1)"
      >›</button>
    </div>
  </dialog>
</template>
