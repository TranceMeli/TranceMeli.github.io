// Reihenfolge = Reihenfolge der "Buchseiten" (Sidebar, Zurück/Weiter, Pfeiltasten).
// "key" ist zugleich Routenname, URL-Teil und Schlüssel für die Navigationstexte.
import HomePage from './views/HomePage.vue'
import CoverLetterPage from './views/CoverLetterPage.vue'
import ResumePage from './views/ResumePage.vue'
import ProjectsPage from './views/ProjectsPage.vue'
import FaqPage from './views/FaqPage.vue'
import CertificatesPage from './views/CertificatesPage.vue'

export const pages = [
  { key: 'home', component: HomePage },
  { key: 'cover-letter', component: CoverLetterPage },
  { key: 'cv', component: ResumePage },
  { key: 'projects', component: ProjectsPage },
  { key: 'faq', component: FaqPage },
  { key: 'certificates', component: CertificatesPage },
]
