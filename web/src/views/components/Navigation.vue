<!-- eslint-disable vue/multi-word-component-names -->
<template lang="pug">
.home-navigation
  v-container.d-flex.align-center.justify-space-between
    router-link.pl-12.d-flex.align-center.justify-space-between(to='/' style='color: white')
      font-awesome-icon(icon='fa-solid fa-house')
      p.ml-2 Trang chủ
    .header__username
      font-awesome-icon(icon='fa-solid fa-user' style="color: white").mr-2
      label(style="color: white").pr-2 {{userInfor.fullname}}
      font-awesome-icon(icon='fa-solid fa-bars' color='white' style="cursor: pointer;" @click="changeDropdownState")
      DropDown.drop-down(v-if="dropdownState" :email="email" :isTeacher="true")
</template>
<script>
  import {ref,onMounted} from "vue";
  import {mixin} from "@/mixin/mixin";
  import axios from "axios";
  import DropDown from "@/views/components/DropDown.vue";
  export default {
    name: "Navigation",
    components: {DropDown},
    mixins: [mixin],
    setup(){
      const dropdownState = ref(false)
      function changeDropdownState(){
        dropdownState.value = !dropdownState.value
      }
      const userInfor = ref({})
      const email = ref(mixin.methods.getCookieValue('email'))
      async function getUserInfor(){
        let getUser = axios.get(`http://127.0.0.1:5000/user_infor/${email.value}`, {
            headers: {
              token: mixin.methods.getCookieValue('token')
            }
        })
        return (await getUser).data
      }
      async function setUpData(){
        userInfor.value = await getUserInfor()
      }
      onMounted(()=>{
        setUpData()
      })
      return {
        userInfor,
        dropdownState,
        changeDropdownState
      }
    }
  }
</script>
<style>
.home-navigation{
  height: 50px;
  width: 100%;
  position:fixed;
  top: 0;
  background-color: forestgreen;
  z-index: 10;
}
a{
  text-decoration: none;
}
</style>