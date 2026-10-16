<script setup>
import { useContent } from '../composables/useContent'

const { t } = useContent()
</script>

<template>
  <article class="page home">
    <h1>{{ t.home.title }}</h1>
  </article>
</template>
