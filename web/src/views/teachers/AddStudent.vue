<template>
    <v-sheet width="500" class="mx-auto">
    <v-form fast-fail @submit.prevent>
      <v-label>Thêm học sinh mới vào danh sách</v-label>
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
        <v-btn class="mt-2" @click="handleAddStudent">Thêm</v-btn>
      </div>
    </v-form>
  </v-sheet>
</template>
<script>
import {ref} from 'vue'
import axios from 'axios';
import { useRouter} from "vue-router";
export default{
  setup(){
    const router = useRouter()
    const student = ref({
      fullname: '',
      dob: '',
      sex: '',
      email: '',
      password: '',
      phone: 0,
      address: '',
      date_of_join:''
    })
    //Render a random password
    function generateRandomPassword(length) {
      const charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=<>?";
      let password = "";
      for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * charset.length);
        password += charset[randomIndex];
      }
      return password;
    }
    async function handleAddStudent(){
      student.value.password = generateRandomPassword(8)
      await axios.post('http://localhost:5000/students', student.value)
      await alert(`Mật khẩu mới cho ${student.value.email} là ${student.value.password}`)
      router.push('/teachers/student-list')
    }
    return {
      student,
      handleAddStudent
    }
  }
}
</script>
<style lang="scss">
  .input-radio{
    width: 16px;
    height: 16px;
  }
</style>