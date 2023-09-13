<template lang="pug">
Navigation
v-container
  v-table
    thead
      tr
        th.text-left
          | Mã sinh viên
        th.text-center
          | Họ và tên
        th.text-center
          | Điểm số
    tbody
      tr(v-for='item in student_list' :key='item.name')
        td.text-left {{ item.student_id }}
        td {{ item.fullname }}
        td
          v-text-field(type="number" variant="outlined" density="compact" v-model="item.point")
  .text-center
    v-btn(color="green" @click="send_point").mt-8 Gửi điểm lên hệ thống


</template>
<script>
  import Navigation from "@/views/components/Navigation.vue";
  import {ref,onMounted} from "vue";
  import {useRoute} from "vue-router";
  import axios from "axios";
  import {mixin} from "@/mixin/mixin";
  export default {
    name: 'TeacherAddPoint',
    components: {Navigation},
    setup(){
      const route = useRoute();
      const class_id = route.params.class_id;
      const student_list = ref([])
      async function get_student_list() {
        const getted_list = await axios.get(`http://127.0.0.1:5000/student_classroom/${class_id}`,{
          headers: {
            'token' : mixin.methods.getCookieValue('token')
          }
        })
        return getted_list.data;
      }
      async function send_point(){
        let request_data = []
        for (let item of student_list.value){
          request_data.push({
            student_id: item.student_id,
            point: item.point,
            subject_id: 0,
            classroom_id: class_id
          })
        }
        await axios.post(`http://127.0.0.1:5000/subject_result`,request_data,{
          headers: {
            'token' : mixin.methods.getCookieValue('token')
          }
        })
      }
      async function setUpData() {
        student_list.value = await get_student_list()
      }
      onMounted(() => {
        setUpData()
      });
      return {
        student_list,
        send_point
      }
    }
  }
</script>