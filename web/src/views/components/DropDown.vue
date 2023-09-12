<template lang="pug">
.dropdown-wrapper()
  .dropdown-triangle
  div(v-for="item in dropdownList")
    label(@click="() => handleDropdownClick(item)").dropdown-item.pr-4.pl-4.pt-1.pb-1.d-block {{ item }}
</template>
<script>
  import { onMounted} from "vue";
  import {useRouter} from "vue-router";
  export default {
    name: 'DropDown',
    props: {
      email : String
    },
    setup(props){
      const router = useRouter()
      const dropdownList = [
        'Thông tin tài khoản',
        'Khóa học của bạn',
        'Quản lý công việc',
        'Cài đặt',
        'Đăng xuất'
      ]
      function handleDropdownClick(item){
        switch(item){
          case 'Đăng xuất': {
            handleLogout()
            break
          }
          case 'Thông tin tài khoản' : {
            toStudentInfor()
            break
          }
          case 'Quản lý công việc': {
            toTaskManage()
          }
        }
      }
      async function handleLogout() {
        document.cookie = "token=; expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/";
        document.cookie = "email=; expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/";
        router.push('/')
      }
      function toStudentInfor(){
        router.push(`/student/infor/${props.email}`)
      }
      function toTaskManage(){
        router.push('/student/taskmanager')
      }
      onMounted(() => {
        console.log(props.email)
      })
      return {
        dropdownList,
        handleDropdownClick
      }
    }}
</script>
<style lang="sass" scoped>
  .dropdown-wrapper
    position: absolute
    background-color: white
    border-radius: 4px
    box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.5)
    top: 100%
  .dropdown-triangle
    position: absolute
    top: -8px
    right: 0
    width: 0
    height: 0
    border-left: 10px solid transparent
    border-right: 10px solid transparent
    border-bottom: 10px solid #fff
  .dropdown-item
    border-bottom: 1px solid #cccccc
    cursor: pointer
  .dropdown-item:hover
    transform: translateX(2px)
    opacity: 0.7
</style>