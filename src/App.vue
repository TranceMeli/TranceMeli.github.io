<script setup>
import { watchEffect } from 'vue'
import { useRoute } from 'vue-router'
import { useContent } from './composables/useContent'
import AppHeader from './components/AppHeader.vue'
import AppSidebar from './components/AppSidebar.vue'
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
  <AppHeader />

  <main class="shell">
    <AppSidebar />

    <section class="reader">
      <div class="book">
        <RouterView v-slot="{ Component }">
          <Transition name="page" mode="out-in">
            <component :is="Component" />
          </Transition>
        </RouterView>
      </div>

      <PagePager />
    </section>
  </main>

  <AppFooter />
</template>
