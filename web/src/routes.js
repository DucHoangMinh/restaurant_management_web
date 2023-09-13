import LoginPage from './views/homepage/Login.vue'
import Dashboard from './views/dashboards/DashBoard.vue'
import StudentsList from './views/teachers/StudentsList.vue'
import AddStudent from './views/teachers/AddStudent.vue'
import SchoolBackground from "@/views/components/SchoolBackground.vue";
import EditStudent from "@/views/teachers/EditStudent.vue";
import HomePage from "@/views/homepage/HomePage.vue";
import StudentDashBoard from "@/views/students/DashBoard.vue"
import StudentInfor from "@/views/students/StudentInfor.vue";
import StudentTaskManager from "@/views/students/taskManager/index.vue"
import TeacherManagePoints from "@/views/teachers/studentsPoint/index.vue"
import TeacherDashBoard from "@/views/teachers/DashBoard.vue"
import TeacherAddPoint from "@/views/teachers/studentsPoint/AddPoint.vue"
import { createRouter, createWebHistory } from 'vue-router'
const routes = [
    { path : '/login',  name: 'LoginPage', component: LoginPage},
    {path : '/dashboard', name: 'Dashboard',component: Dashboard},
    {path : '/teachers/student-list', name: 'StudentList', component: StudentsList},
    {path : '/teachers/student-list/add', name: 'AddStudent', component: AddStudent},
    {path:  '/teachers/points', name:'TeacherManagePoints', component: TeacherManagePoints},
    {path:  '/teachers/points/add/:class_id', name: 'TeacherAddPoints',component: TeacherAddPoint},
    {path : '/schoolbackground', name: 'SchoolBackground', component: SchoolBackground},
    {path : '/teachers/student-list/edit/:email', name: EditStudent, component: EditStudent},
    {path : '/teachers/dashboard', name: 'TeacherDashBoard', component: TeacherDashBoard},
    {path : '/',name:'HomePage', component: HomePage},
    {path : '/student/dashboard', component: StudentDashBoard},
    {path : '/student/infor/:email',component: StudentInfor},
    {path : '/student/taskmanager',component: StudentTaskManager},
]
const router = createRouter({
    history: createWebHistory(),
    routes: routes
})
export default router