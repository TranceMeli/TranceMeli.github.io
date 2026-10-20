<script setup>
import { computed } from 'vue'
import { useContent } from '../composables/useContent'
import projectData from '../data/projects.json'
import RichText from '../components/RichText.vue'
import ContactLinks from '../components/ContactLinks.vue'
import CvSection from '../components/CvSection.vue'
import CvEntry from '../components/CvEntry.vue'
import CvLines from '../components/CvLines.vue'

const { lang, t } = useContent()

// Die Projekte im Lebenslauf kommen aus derselben Datei wie die Projekte-Seite
// (src/data/projects.json) – hier nur die mit "featured": true.
const projectEntries = computed(() =>
  projectData.projects
    .filter((project) => project.featured)
    .sort((a, b) => (a.cvOrder ?? 99) - (b.cvOrder ?? 99))
    .map((project) => {
      const text = project[lang.value] ?? project.de
      return {
        id: project.id,
        title: project.title,
        meta: `*${text.subtitle}*`,
        tech: project.tech.join(' · '),
        bullets: text.highlights,
      }
    }),
)
</script>

<template>
  <article class="page cv">
    <h1>{{ t.cv.name }}</h1>
    <p class="cv-role">{{ t.cv.role }}</p>
    <p class="cv-links"><ContactLinks /></p>

    <CvSection :title="t.cv.profile.title">
      <p v-for="(paragraph, i) in t.cv.profile.paragraphs" :key="i">
        <RichText :text="paragraph" />
      </p>
    </CvSection>

    <CvSection :title="t.cv.training.title">
      <CvEntry v-for="entry in t.cv.training.entries" :key="entry.title" v-bind="entry" />
    </CvSection>

    <CvSection :title="t.cv.projectsTitle">
      <CvEntry v-for="entry in projectEntries" :key="entry.id" v-bind="entry" />
    </CvSection>

    <CvSection :title="t.cv.experience.title">
      <CvEntry v-for="entry in t.cv.experience.entries" :key="entry.title" v-bind="entry" />
    </CvSection>

    <CvSection :title="t.cv.education.title">
      <CvEntry v-for="entry in t.cv.education.entries" :key="entry.title" v-bind="entry" />
    </CvSection>

    <CvSection :title="t.cv.skills.title">
      <CvLines :lines="t.cv.skills.lines" />
    </CvSection>

    <CvSection :title="t.cv.languages.title">
      <CvLines :lines="t.cv.languages.lines" />
    </CvSection>

    <CvSection :title="t.cv.interests.title">
      <p>{{ t.cv.interests.text }}</p>
    </CvSection>
  </article>
</template>
