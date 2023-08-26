import LoginPage from './views/homepage/Login.vue'
import Dashboard from './views/dashboards/DashBoard.vue'
import StudentsList from './views/teachers/StudentsList.vue'
import AddStudent from './views/teachers/AddStudent.vue'
import SchoolBackground from "@/views/homepage/SchoolBackground.vue";
import EditStudent from "@/views/teachers/EditStudent.vue";
import HomePage from "@/views/homepage/HomePage.vue";
import { createRouter, createWebHistory } from 'vue-router'
const routes = [
    { path : '/login',  name: 'LoginPage', component: LoginPage},
    {path : '/dashboard', name: 'Dashboard',component: Dashboard},
    {path : '/teachers/student-list', name: 'StudentList', component: StudentsList},
    {path : '/teachers/student-list/add', name: 'AddStudent', component: AddStudent},
    {path : '/schoolbackground', name: 'SchoolBackground', component: SchoolBackground},
    {path : '/teachers/student-list/edit/:email', name: EditStudent, component: EditStudent},
    {path : '/',name:'HomePage', component: HomePage}
]
const router = createRouter({
    history: createWebHistory(),
    routes: routes
})
export default router