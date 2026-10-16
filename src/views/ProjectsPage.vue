<script setup>
import { computed, ref } from 'vue'
import { useContent } from '../composables/useContent'
import projectData from '../data/projects.json'
import RichText from '../components/RichText.vue'
import ProjectCard from '../components/ProjectCard.vue'
import ScreenshotModal from '../components/ScreenshotModal.vue'

const { lang, t } = useContent()

// Projekte nach Kategorie gruppieren (Reihenfolge wie in projects.json)
const groups = computed(() =>
  projectData.categories
    .map((category) => ({
      ...category,
      projects: projectData.projects.filter((project) => project.category === category.id),
    }))
    .filter((group) => group.projects.length > 0),
)

// Aktuell geöffnetes Screenshot-Modal (null = geschlossen)
const viewer = ref(null)
</script>

<template>
  <article class="page projects">
    <h1>{{ t.projects.title }}</h1>
    <p class="subtitle"><RichText :text="t.projects.intro" /></p>

    <section v-for="group in groups" :key="group.id" class="project-category">
      <h2 class="category-title">
        {{ group[lang] ?? group.de }}
        <span class="category-count">({{ group.projects.length }})</span>
      </h2>

      <div class="project-grid">
        <ProjectCard
          v-for="project in group.projects"
          :key="project.id"
          :project="project"
          :lang="lang"
          :labels="t.projects.labels"
          @open="viewer = $event"
        />
      </div>
    </section>

    <ScreenshotModal
      v-if="viewer"
      :title="viewer.title"
      :images="viewer.images"
      :start-index="viewer.index"
      :labels="t.projects.labels"
      @close="viewer = null"
    />
  </article>
</template>
