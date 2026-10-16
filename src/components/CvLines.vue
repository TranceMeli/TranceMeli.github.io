<script setup>
// Zeilen im Format "Label: Wert" (IT-Kenntnisse, Sprachen)
defineProps({
  lines: { type: Array, required: true },
})
</script>

<template>
  <div class="skills">
    <p v-for="line in lines" :key="line.label">
      <strong>{{ line.label }}:</strong> {{ line.value }}
    </p>
  </div>
</template>
