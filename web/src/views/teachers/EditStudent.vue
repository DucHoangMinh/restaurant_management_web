<template>
  <v-sheet width="500" class="mx-auto">
    <v-form fast-fail @submit.prevent>
      <v-label>Chỉnh sửa thông tin học sinh</v-label>
      <v-text-field
        label="Họ và tên"
        variant="outlined"
        v-model="student.fullname"
      ></v-text-field>
      <v-text-field v-model="student.dob" type="date" label="Ngày sinh" variant="outlined"></v-text-field>
      <v-text-field v-model="student.email" label="Email" type="email" variant="outlined"></v-text-field>
      <v-text-field v-model="student.phone" type="number" label="Số điện thoại" variant="outlined"/>
      <div class="choose-sex d-flex justify-lg-space-between align-center mb-4">
        <v-label>Giới tính: {{student.sex}}</v-label>
        <div class="d-flex align-center">
          <input value="Nam" class ="input-radio" type="radio"  name="sex" v-model="student.sex"/>
          <v-label>Nam</v-label>
          <input value="Nữ" class="input-radio" type="radio" name="sex" v-model="student.sex" style="margin-left: 16px"/>
          <v-label>Nữ </v-label>
        </div>
      </div>
      <v-textarea v-model="student.address" label="Địa chỉ" variant="outlined" rows="2"/>
      <v-text-field v-model="student.date_of_join" type="date" label="Ngày nhập học" variant="outlined"></v-text-field>
      <div class="d-flex justify-space-around">
        <v-btn class="mt-2" @click="handleBack">Hủy</v-btn>
        <v-btn class="mt-2" @click="handleEditStudent">Xác nhận</v-btn>
      </div>
    </v-form>
    </v-sheet>
</template>
<script>
  import {ref, onMounted} from "vue";
  import {useRoute,useRouter} from "vue-router"
  import axios from "axios";

  export default {
    setup(){
        const route = useRoute()
        const router = useRouter()
        const student = ref({
          student_id: null,
          fullname: '',
          dob: '',
          sex: '',
          email: '',
          password: '',
          phone: 0,
          address: '',
          date_of_join:''
        })
      const student_email = route.params.email
      async function getStudentByEmail(){
          let getdata = await axios.get(`http://localhost:5000/students/${student_email}`)
          console.log(getdata)
          return  getdata.data
      }
      async function setUpData(){
        let data = await getStudentByEmail()
        student.value = data
        student.value.date_of_join = new Date(data.date_of_join).toISOString().split('T')[0]
        student.value.dob = new Date(data.dob).toISOString().split('T')[0]
      }
      function handleBack(){
        router.push('/teachers/student-list')
      }
      async function handleEditStudent(){
        await axios.patch(`http://localhost:5000/students/${student.value.student_id}`, student.value)
        router.push('/teachers/student-list')
      }
      onMounted(() => {
        setUpData()
      })
      return {
          student,
          handleBack,
          handleEditStudent
      }
    },
  }
</script>
<style>

</style>