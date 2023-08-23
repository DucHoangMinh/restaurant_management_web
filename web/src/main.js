/* eslint-disable no-unused-vars */
import { createApp } from 'vue'
import App from './App.vue'
import router from './routes'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faUserSecret , faUser, faUserPlus, faSchool, faPen, faTrash} from '@fortawesome/free-solid-svg-icons'
library.add(faUserSecret, faUser, faUserPlus, faSchool, faPen, faTrash)

const vuetify = createVuetify({
  components,
  directives,
})

const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(router)
app.use(vuetify)
app.mount('#app')
