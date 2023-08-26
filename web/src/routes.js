import LoginPage from './views/Login.vue'
import Dashboard from './views/dashboards/DashBoard.vue'
import StudentsList from './views/teachers/StudentsList.vue'
import AddStudent from './views/teachers/AddStudent.vue'
import { createRouter, createWebHistory } from 'vue-router'
const routes = [
    { path : '/login',  name: 'LoginPage', component: LoginPage},
    {path : '/dashboard', name: 'Dashboard',component: Dashboard},
    {path : '/teachers/student-list', name: 'StudentList', component: StudentsList},
    {path : '/teachers/student-list/add', name: 'AddStudent', component: AddStudent}
]
const router = createRouter({
    history: createWebHistory(),
    routes: routes
})
export default router