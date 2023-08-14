import LoginPage from './views/Login.vue'
import { createRouter, createWebHistory } from 'vue-router'
const routes = [
    { path : '/login',  name: 'LoginPage', component: LoginPage}
]
const router = createRouter({
    history: createWebHistory(),
    routes: routes
})
export default router