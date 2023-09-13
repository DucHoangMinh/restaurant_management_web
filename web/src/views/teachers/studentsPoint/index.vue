<template lang="pug">
Navigation
v-container
  div.text-left.pb-4
    label.text-left Danh sách lớp mà bạn quản lý
  div.class-list-table
    v-table
      thead
        tr
          th.text-left
            | Tên lớp
          th.text-left
            | Số lượng học sinh
          th.text-center
            | Khối
      tbody
        tr(@click="toAddPointPage(item)" v-for='item in class_list_data' :key='item.classroom_id' style="cursor: pointer")
          td.text-left {{ item.classroom_name }}
          td {{ item.calories }}
          td {{ item.grade }}

</template>
<script>
  import Navigation from "@/views/components/Navigation.vue";
  import axios from "axios";
  import {ref,onMounted} from "vue";
  import {useRouter} from "vue-router";
  import {mixin} from "@/mixin/mixin";

  export default{
    name:"TeacherManagePoints",
    components: {Navigation},
    setup() {
      const router = useRouter();
      const teacher_data = ref({})
      const class_list_data = ref([])
      function toAddPointPage(item){
        router.push(`/teachers/points/add/${item.classroom_id}`)
      }
      async function getTeacherData(){
        let reponse = await axios.get(`http://127.0.0.1:5000/teachers/${mixin.methods.getCookieValue('email')}`,{
          headers: {
            'token' : mixin.methods.getCookieValue('token')
          }
        })
        return reponse.data
      }
      async function getClassListData(){
         let reponse = await axios.get(`http://127.0.0.1:5000/classrooms/all/${teacher_data.value.id}`,{
          headers: {
            'token' : mixin.methods.getCookieValue('token')
          }
        })
        return reponse.data
      }
      async function setUpData(){
        teacher_data.value = await getTeacherData()
        class_list_data.value = await getClassListData()
      }
      onMounted(() => {
        setUpData()
      })
      return {
        class_list_data,
        toAddPointPage
      }
    }
  }
</script>