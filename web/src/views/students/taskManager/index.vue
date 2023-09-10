<template lang="pug">
v-dialog(v-model='addTaskDialog' width='50%' height="80%" )
  v-card.v-col
    .addTaskForm.v-col-8.ma-auto
      .d-flex.align-center.justify-center
        label.v-col-5 Tên công việc
        v-text-field(variant="outlined" density="compact" v-model="task.title")
      .d-flex.align-center.justify-center
        label.v-col-5 Thời gian bắt đầu
        VueDatePicker(time-picker-inline v-model="task.start" format="dd/MM/yyyy HH:mm")
      .d-flex.align-center.justify-center
        label.v-col-5 Thời gian kết thúc
        VueDatePicker(time-picker-inline v-model="task.end" format="dd/MM/yyyy HH:mm")
    v-card-actions.d-flex.justify-lg-space-around
      v-btn(color='primary'  @click='addTaskDialog = false') Hủy
      v-btn(color="green" @click="addTask") Thêm
Navigation
v-container
  .addTaskButton.pb-8.text-right(style="cursor:pointer")
    v-btn(color="green" style="font-size:14px" @click="addTaskDialog = true") Thêm công việc mới
        font-awesome-icon(icon="fa-solid fa-calendar-plus").pl-2
  vue-cal(:events="events" events-on-month-view active-view="month").vuecal--green-theme
</template>
<script>
  import {ref, onMounted} from 'vue'
  import VueCal from 'vue-cal'
  import Navigation from "@/views/components/Navigation.vue";
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
      VueDatePicker
    },
    setup(){
      const addTaskDialog = ref(false)
      const events = ref([])
      const task = ref({
        title: '',
        start: '',
        end: '',
        email: mixin.methods.getCookieValue('email')
      })
      async function addTask(){
        try {
          const request_data = {
            title: task.value.title,
            email: task.value.email,
            start: mixin.methods.formatToPostgreTimeStamp(task.value.start),
            end: mixin.methods.formatToPostgreTimeStamp(task.value.end)
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
        location.href = '/student/taskmanager'
      }
      async function getTaskList(){
          const res = await axios.get(`http://127.0.0.1:5000/tasks/${mixin.methods.getCookieValue('email')}`, {
            headers: {
              token: mixin.methods.getCookieValue('token')
            }
          })
          return res.data
      }
      async function setUpData(){
        events.value =await getTaskList()
        for(var i = 0; i < events.value.length;i ++){
          events.value[i].start = mixin.methods.formatToPostgreTimeStamp(events.value[i].start)
          events.value[i].end = mixin.methods.formatToPostgreTimeStamp(events.value[i].end)
        }
      }
      onMounted(() => {
        console.log(typeof events.value)
        setUpData()
      });
      return {
        addTask,
        addTaskDialog,
        task,
        events
      }
    }
  }
</script>
<style lang="sass" scoped>
::v-deep .v-input__details
  display: none
</style>