<script setup>
// Ein Abschnitt des Lebenslaufs: Überschrift + beliebiger Inhalt (<slot />)
defineProps({
  title: { type: String, required: true },
})
</script>

<template>
  <section>
    <h2>{{ title }}</h2>
    <slot />
  </section>
</template>
