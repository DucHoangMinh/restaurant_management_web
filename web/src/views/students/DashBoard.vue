<template lang="pug">
Navigation
  .header__username
    font-awesome-icon(icon='fa-solid fa-user' style="color: white").mr-2
    label(style="color: white").pr-2 Hoang Minh Duc
    font-awesome-icon(icon='fa-solid fa-bars' color='white' style="cursor: pointer;" @click="changeDropdownState")
    DropDown.drop-down(v-if="dropdownState")
</template>
<script>
import Navigation from "@/views/components/Navigation.vue";
import DropDown from "@/views/components/DropDown.vue";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {ref,onMounted} from "vue";

export default {
  name: 'StudentDashBoard',
  components: {DropDown, FontAwesomeIcon, Navigation},
  setup(){
    const dropdownState = ref(false)
    function changeDropdownState(){
      dropdownState.value = !dropdownState.value
    }
    onMounted(() => {
      console.log("This is only a test")
    })
    return {
      dropdownState,
      changeDropdownState
    }
  }
}
</script>
<style scoped lang="sass">
  .drop-down
    position: absolute
</style>