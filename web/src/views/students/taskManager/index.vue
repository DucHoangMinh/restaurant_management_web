<template lang="pug">
v-dialog(v-model='addTaskDialog' width='50%' height="80%")
  v-card.v-col
    label.text-center.text-h5.my-4 Đăng ký lịch gặp mặt giáo viên
    .addTaskForm.v-col-8.mx-auto
      .d-flex.align-center.justify-center
        label.v-col-5 Tên công việc: {{isTeacher ? '(nếu có)' : ''}}
        v-text-field(variant="outlined" density="compact" v-model="task.title")
      .d-flex.align-center.justify-center
        label.v-col-5 Thời gian bắt đầu:
        VueDatePicker(time-picker-inline v-model="task.start" format="dd/MM/yyyy HH:mm")
      .d-flex.align-center.justify-center
        label.v-col-5 Thời gian kết thúc:
        VueDatePicker(time-picker-inline v-model="task.end" format="dd/MM/yyyy HH:mm")
      .d-flex.align-center.justify-center
        label.v-col-6 Công khai với sinh viên khác:
        .d-flex.v-col-6
          input(type="radio" value="true" v-model="task.public" name="taskPublic")
          label.pr-2 Cho phép
          input(type="radio" value="false" v-model="task.public" name="taskPublic")
          label Không cho phép
    v-card-actions.d-flex.justify-lg-space-around
      v-btn(color='primary'  @click='addTaskDialog = false') Hủy
      v-btn(color="green" @click="addTask") Thêm
v-dialog(v-model='showDialog' width='50%' height="80%")
    v-card
      label.text-center.text-h5.my-4 Cập nhật lịch gặp mặt giáo viên
      .addTaskForm.v-col-8.mx-auto
        .d-flex.align-center.justify-center
          label.v-col-5 Tên công việc:
          v-text-field(variant="outlined" density="compact" v-model="task.title")
        .d-flex.align-center.justify-center
          label.v-col-5 Thời gian bắt đầu:
          VueDatePicker(time-picker-inline v-model="task.start" format="dd/MM/yyyy HH:mm")
        .d-flex.align-center.justify-center
          label.v-col-5 Thời gian kết thúc:
          VueDatePicker(time-picker-inline v-model="task.end" format="dd/MM/yyyy HH:mm")
        .d-flex.align-center.justify-center
          label.v-col-6 Công khai với sinh viên khác:
          .d-flex.v-col-6
            input(type="radio" value="true" v-model="task.public" name="taskPublic")
            label.pr-2 Cho phép
            input(type="radio" value="false" v-model="task.public" name="taskPublic")
            label Không cho phép
      v-card-actions.d-flex.justify-lg-space-around
        v-btn(color='primary'  @click='showDialog = false') Hủy
        v-btn(color='danger'  @click='deleteTask')  Xóa nhiệm vụ
        v-btn(color="green" @click="updateTask") Cập nhật thông tin
v-dialog(v-model='confirmStudentScheduleDialog' width='50%' height="80%")
    v-card
      v-container
        div
          label.text-center.text-h5.my-4 Xác nhận lịch gặp mặt
        .d-flex.justify-space-around.mb-16.mt-16
          v-btn(color='primary' @click="confirmStudentScheduleDialog=false") Hủy
          v-btn(color='danger' @click="() => markAsNotSuitable()")  Đánh dấu là lịch không phù hợp
          v-btn(color="green" @click="() => markAsSuitable()") Xác nhận là lịch phù hợp
Navigation
v-container
  .addTaskButton.pb-8.text-right(style="cursor:pointer")
    v-btn(color="green" style="font-size:14px" @click="addTaskDialog = true") {{isTeacher ? 'Đánh dấu lịch bận' : 'Đăng ký lịch làm việc mới'}}
        font-awesome-icon(icon="fa-solid fa-calendar-plus").pl-2
  vue-cal(
    :events="events"
    events-on-month-view
    :time-from="7 * 60"
    :time-to="20 * 60"
    active-view="month"
    :on-event-click="onEventClick"
    ).vuecal--green-theme
</template>
<script>
  import {ref, onMounted} from 'vue'
  import VueCal from 'vue-cal'
  import Navigation from "@/views/components/Navigation.vue";
  import DropDown from "@/views/components/DropDown.vue";
  import VueDatePicker from '@vuepic/vue-datepicker';
  import 'vue-cal/dist/vuecal.css'
  import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
  import {mixin} from "@/mixin/mixin";
  import axios from "axios";
  export default {
    name: 'StudentTaskManager',
    components: {
      FontAwesomeIcon,
      Navigation,
      VueCal,
      VueDatePicker,
      DropDown
    },
    setup(){
      const confirmStudentScheduleDialog = ref(false)
      const selectedEvent = ref({})
      const showDialog = ref(false)
      const addTaskDialog = ref(false)
      const events = ref([])
      const dropdownState = ref(false)
      const email = ref(mixin.methods.getCookieValue('email'))
      const role = ref(mixin.methods.getCookieValue('role'))
      const isTeacher = ref(false)
      function changeDropdownState(){
        dropdownState.value = !dropdownState.value
      }
      const task = ref({
        title: '',
        start: '',
        end: '',
        email: mixin.methods.getCookieValue('email'),
        public: true,
        isTeacher: false
      })
      function resetTaskValues(){
        task.value = {
          title: '',
          start: '',
          end: '',
          email: mixin.methods.getCookieValue('email'),
          public: true
        }
      }
      async function markAsNotSuitable(){
        await axios.patch(`http://127.0.0.1:5000/tasks/marknotsuitable/${selectedEvent.value.task_id}`, {}, {
            headers: {
              token: mixin.methods.getCookieValue('token')
            }
        })
            .then(() => {
              location.href = '/student/taskmanager'
            })
      }
      async function markAsSuitable(){
        await axios.patch(`http://127.0.0.1:5000/tasks/marksuitable/${selectedEvent.value.task_id}`, {}, {
            headers: {
              token: mixin.methods.getCookieValue('token')
            }
        })
            .then(() => {
              location.href = '/student/taskmanager'
            })
      }
      async function addTask(){
        try {
          const request_data = {
            title: task.value.title,
            email: task.value.email,
            start: mixin.methods.formatToPostgreTimeStamp(task.value.start),
            end: mixin.methods.formatToPostgreTimeStamp(task.value.end),
            public: task.value.public,
            isTeacher: role.value == 'teacher'
          }
          console.log(request_data)
          await axios.post('http://127.0.0.1:5000/tasks', request_data, {
            headers: {
              token: mixin.methods.getCookieValue('token')
            }
          })
        } catch (e){
          console.log(e)
        }
        resetTaskValues()
        location.href = '/student/taskmanager'
      }
      async function getTaskList(){
          const res = await axios.get(`http://127.0.0.1:5000/tasks/all/${mixin.methods.getCookieValue('email')}`, {
            headers: {
              token: mixin.methods.getCookieValue('token')
            }
          })
          console.log(res.data)
          return res.data
      }async function getTaskById(id){
          const res = await axios.get(`http://127.0.0.1:5000/tasks/${id}`, {
            headers: {
              token: mixin.methods.getCookieValue('token')
            }
          })
          console.log(res.data)
          return res.data
      }
      async function updateTask(){
        const request_data = {
            title: task.value.title,
            email: task.value.email,
            start: mixin.methods.formatToPostgreTimeStamp(task.value.start),
            end: mixin.methods.formatToPostgreTimeStamp(task.value.end),
            public: task.value.public
        }
        axios.patch(`http://127.0.0.1:5000/tasks/${task.value.task_id}`, request_data, {
            headers: {
              token: mixin.methods.getCookieValue('token')
            }
        })
        resetTaskValues()
        location.href = '/student/taskmanager'
      }
      async function deleteTask(){
        axios.delete(`http://127.0.0.1:5000/tasks/${task.value.task_id}`, {
            headers: {
              token: mixin.methods.getCookieValue('token')
            }
        })
        location.href = '/student/taskmanager'
        resetTaskValues()
      }
      function setTeacherOrStudent(){
        isTeacher.value =mixin.methods.getCookieValue('role') == 'teacher'
      }
      async function setUpData(){
        events.value =await getTaskList()
        for(let i = 0; i < events.value.length; i ++){
          if(events.value[i].isTeacher){
            events.value[i].class = 'teacher_event'
          }
          if(events.value[i].status == 'notsuitable'){
            events.value[i].class = 'notsuitable'
          }
          if(events.value[i].status =='suitable'){
            events.value[i].class ='suitable'
          }
          events.value[i].start = mixin.methods.formatToPostgreTimeStamp(events.value[i].start)
          events.value[i].end = mixin.methods.formatToPostgreTimeStamp(events.value[i].end)
        }
      }
      async function onEventClick (event, e) {
        if(event.email === email.value) {
          resetTaskValues()
          selectedEvent.value = event
          task.value = await getTaskById(selectedEvent.value.task_id)
          showDialog.value = true

          // Prevent navigating to narrower view (default vue-cal behavior).
          e.stopPropagation()
        }
        else {
          if(role.value == 'teacher'){
            selectedEvent.value = event
            confirmStudentScheduleDialog.value = true
          }
        }
      }
      onMounted(() => {
        setTeacherOrStudent()
        setUpData()
        console.log(events.value)
      });
      return {
        addTask,
        addTaskDialog,
        task,
        events,
        dropdownState,
        changeDropdownState,
        email,
        selectedEvent,
        showDialog,
        onEventClick,
        updateTask,
        deleteTask,
        isTeacher,
        role,
        confirmStudentScheduleDialog,
        markAsNotSuitable,
        markAsSuitable
      }
    }
  }
</script>
<style lang="sass" scoped>
::v-deep .v-input__details
  display: none
::v-deep .teacher_event
  padding: 4px
  background-color: orange !important
  color: #fff
::v-deep .suitable
  color: #fff
  background-color: green
::v-deep .notsuitable
  background-color: yellow
</style>