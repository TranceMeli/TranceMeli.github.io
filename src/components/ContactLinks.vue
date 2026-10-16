<script setup>
import { links } from '../content/shared'
</script>

<template>
  <template v-for="(link, index) in links" :key="link.label">
    <template v-if="index > 0"> · </template>
    <a :href="link.href" target="_blank" rel="noopener">{{ link.label }}</a>
  </template>
</template>
