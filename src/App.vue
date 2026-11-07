<script setup>
import { watchEffect } from 'vue'
import { useRoute } from 'vue-router'
import { useContent } from './composables/useContent'
import AppHeader from './components/AppHeader.vue'
import AppSidebar from './components/AppSidebar.vue'
import EditorTabs from './components/EditorTabs.vue'
import EditorHead from './components/EditorHead.vue'
import PagePager from './components/PagePager.vue'
import AppFooter from './components/AppFooter.vue'

const route = useRoute()
const { lang, t } = useContent()

// Sprache und Titel des Browser-Tabs passend zur aktuellen Seite setzen
watchEffect(() => {
  document.documentElement.lang = lang.value
  const pageName = t.value.nav[route.name]
  document.title = pageName ? `${pageName} – ${t.value.meta.title}` : t.value.meta.title
})
</script>

<template>
  <div class="win">
    <AppHeader />

    <div class="wrap">
      <AppSidebar />

      <section class="reader">
        <EditorTabs />

        <div class="book">
          <EditorHead />
          <RouterView v-slot="{ Component }">
            <Transition name="page" mode="out-in">
              <component :is="Component" />
            </Transition>
          </RouterView>
        </div>
      </section>
    </div>

    <PagePager />
  </div>

  <AppFooter />
</template>
