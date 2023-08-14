/* eslint-disable no-unused-vars */
import { createApp } from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Vue from 'vue'
import router from './routes'

const app = createApp(App)
app.use(router)
app.mount('#app')
