<template lang="pug">
Navigation
  .header__username
    font-awesome-icon(icon='fa-solid fa-user' style="color: white").mr-2
    label(style="color: white").pr-2 Hoang Minh Duc
    font-awesome-icon(icon='fa-solid fa-bars' color='white' style="cursor: pointer;" @click="changeDropdownState")
    DropDown.drop-down(v-if="dropdownState" :email="email" :isTeacher="true")
</template>
<script>
  import Navigation from "@/views/components/Navigation.vue";
  import DropDown from "@/views/components/DropDown.vue";
  import {ref} from "vue";
  // import {mixin} from "@/mixin/mixin";
  export default {
    name: 'TeacherDashboard',
    components: {DropDown, Navigation},
    setup(){
      const dropdownState = ref(false)
      function changeDropdownState(){
        dropdownState.value = !dropdownState.value
      }
      return{
        dropdownState,
        changeDropdownState
      }
    }
  }
</script>