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

// Filter: "all" oder die ID einer Kategorie
const filter = ref('all')
const visibleGroups = computed(() =>
  filter.value === 'all' ? groups.value : groups.value.filter((group) => group.id === filter.value),
)

// Aktuell geöffnetes Screenshot-Modal (null = geschlossen)
const viewer = ref(null)
</script>

<template>
  <article class="page projects">
    <h1>{{ t.projects.title }}</h1>
    <p class="subtitle"><RichText :text="t.projects.intro" /></p>

    <div class="filters" role="group" :aria-label="t.projects.title">
      <button type="button" :class="{ on: filter === 'all' }" @click="filter = 'all'">
        {{ t.projects.labels.all }}
      </button>
      <button
        v-for="group in groups"
        :key="group.id"
        type="button"
        :class="{ on: filter === group.id }"
        @click="filter = group.id"
      >
        {{ group[lang] ?? group.de }}
      </button>
    </div>

    <section v-for="group in visibleGroups" :key="group.id" class="project-category">
      <h2 class="category-title">
        <span class="c"># {{ group[lang] ?? group.de }}</span>
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
