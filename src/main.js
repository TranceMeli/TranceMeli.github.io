import { createApp } from 'vue'
import App from './App.vue'
import { router } from './router'

import './styles/fonts.css'
import './styles/variables.css'
import './styles/base.css'
import './styles/layout.css'
import './styles/pages.css'
import './styles/modal.css'
import './styles/responsive.css'

createApp(App).use(router).mount('#app')
