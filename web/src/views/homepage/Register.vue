<template lang="pug">
Navigation
v-sheet.mx-auto(width='500')
  v-form(fast-fail='' @submit.prevent='')
    v-label.pa-4.text-h5 Đăng ký tài khoản mới
    v-text-field(label='Họ và tên' variant='outlined' v-model="user.fullname" )
    v-text-field(type='date' label='Ngày sinh' variant='outlined' v-model="user.dob" )
    v-text-field(label='Email' type='email' variant='outlined' v-model="user.email" )
    v-text-field(type='number' label='Số điện thoại' variant='outlined' v-model="user.phone" )
    .choose-sex.d-flex.justify-lg-space-between.align-center.mb-4
      v-label Gi&#x1EDB;i t&iacute;nh:
      .d-flex.align-center
        input.input-radio(value='Nam' type='radio' name='sex' v-model="user.sex" )
        v-label Nam
        input.input-radio(value='Nữ' type='radio' name='sex' style='margin-left: 16px' v-model="user.sex" )
        v-label N&#x1EEF;
    v-text-field(type='text' label='Lớp học' variant='outlined' v-model="user.classroom" )
    v-textarea(label='Địa chỉ' variant='outlined' rows='2' v-model="user.address" )
    v-text-field(label='Mật khẩu' type='password' variant='outlined' v-model="user.password" )
    .d-flex.justify-space-around
      v-btn(@click="location.href='/'").mt-2 Hủy
      v-btn(color="green" @click="handleRegister").mt-2 Đăng ký tài khoản
</template>
<script>
  import Navigation from "@/views/components/Navigation.vue";
  import {ref} from "vue";
  import axios from "axios";
  import {useRouter} from "vue-router";
  export default {
    name: 'Register',
    components: {Navigation},
    setup(){
      const router = useRouter()
      const user = ref({
        fullname: '',
        dob: '',
        sex: '',
        email: '',
        password: '',
        phone: 0,
        address: '',
        classroom: ''
      })
      async function handleRegister() {
        console.log(user.value)
        await axios.post('http://localhost:5000/user_infor', user.value)
        router.push('/login')
      }
      return {
        user,
        handleRegister
      }
    }
  }
</script>
<style lang="sass">

</style>