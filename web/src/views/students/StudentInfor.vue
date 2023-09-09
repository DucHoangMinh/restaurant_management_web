<template lang="pug">
Navigation
  .header__username
    font-awesome-icon(icon='fa-solid fa-user' style="color: white").mr-2
    label(style="color: white").pr-2 Hoang Minh Duc
    font-awesome-icon(icon='fa-solid fa-bars' color='white' style="cursor: pointer;" @click="changeDropdownState")
    DropDown.drop-down(v-if="dropdownState" :email="email")
SnackBar(:message="snackbarMessage" :showSnackbar="snackbarState")
v-container.pt-16
  v-row
    v-col
      .v-col-8.ma-auto.pa-12(style="border: 1px solid #ccc; border-radius: 10px")
        label.text-h5.pb-12.d-block Thông tin tài khoản Hoàng Minh Đức
        .information
          .infor-item.d-flex.justify-start.align-center.pb-4
            label.v-col-3.text-left Họ và tên:
            v-text-field(variant="outlined" density="compact" v-model="student.fullname")
          .infor-item.d-flex.justify-start.align-center.pb-4
            label.v-col-3.text-left Ngày sinh:
            VueDatePicker(v-model="student.dob" :enable-time-picker="false")
          .infor-item.d-flex.justify-start.align-center.pb-4
            label.v-col-3.text-left Giới tính:
            input.input-radio.mr-1(value='Nam' type='radio' name='sex' v-model='student.sex')
            label Nam
            input.input-radio.mr-1(value='Nữ' type='radio' name='sex' v-model='student.sex' style='margin-left: 16px')
            label N&#x1EEF;
          .infor-item.d-flex.justify-start.align-center.pb-4
            label.v-col-3.text-left Email:
            v-text-field(variant="outlined" density="compact" v-model="student.email")
          .infor-item.d-flex.justify-start.align-center.pb-4
            label.v-col-3.text-left Phone:
            v-text-field(variant="outlined" density="compact" v-model="student.phone")
          .infor-item.d-flex.justify-start.pb-12
            label.v-col-3.text-left Address:
            v-textarea(variant="outlined" density="compact" rows="3" v-model="student.address")
        v-btn.bg-green(@click="handleChangeStudentInfor") Xác nhận thay đổi
</template>
<script>
import {ref, onMounted} from 'vue'
import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';
import Navigation from "@/views/components/Navigation.vue";
import DropDown from "@/views/components/DropDown.vue";
import axios from 'axios'
import {mixin} from "@/mixin/mixin";
import {useRoute} from 'vue-router'
import SnackBar from "@/views/components/SnackBar.vue";
  export default{
    mixins: [mixin],
    name: 'StudentInfor',
    components: {
      SnackBar,
      DropDown,
      Navigation,
      VueDatePicker
    },
    setup(){
      const route = useRoute()
      const student = ref({
        fullname: null,
        dob: null,
        email: null,
        phone: null,
        address: null,
        sex: null
      })
      const datepickerState = ref(false)
      const dropdownState = ref(false)
      const snackbarMessage = ref('')
      const snackbarState = ref(false)

      async function getStudentInfor(){
        let email = route.params.email
        let config = {
          headers: {
            token : mixin.methods.getCookieValue('token')
          }
        }
        const tempData = await axios.get(`http://127.0.0.1:5000/students/${email}`,config)
        return tempData.data
      }
      async function setUpData(){
        let tempInfor = await getStudentInfor()
        student.value = tempInfor
      }
      function changeDropdownState(){
        dropdownState.value = !dropdownState.value
      }
      async function handleChangeStudentInfor(){
        snackbarMessage.value = 'test'
        snackbarState.value = true
        setTimeout(() => {
          snackbarState.value = false
        },2000)
      }
      onMounted(() => {
        setUpData()
      })
      return {
        datepickerState,
        student,
        dropdownState,
        changeDropdownState,
        handleChangeStudentInfor,
        snackbarMessage,
        snackbarState
      }
    }
  }
</script>
<style lang="sass" scoped>
  ::v-deep .v-input__details
    display: none
  v-date-picker
    z-index: 1
</style>