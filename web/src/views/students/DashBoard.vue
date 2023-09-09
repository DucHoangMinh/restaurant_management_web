<template lang="pug">
Navigation
  .header__username
    font-awesome-icon(icon='fa-solid fa-user' style="color: white").mr-2
    label(style="color: white").pr-2 Hoang Minh Duc
    font-awesome-icon(icon='fa-solid fa-bars' color='white' style="cursor: pointer;" @click="changeDropdownState")
    DropDown.drop-down(v-if="dropdownState" :email="email")
</template>
<script>
import Navigation from "@/views/components/Navigation.vue";
import DropDown from "@/views/components/DropDown.vue";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {mixin} from "@/mixin/mixin.js";
import {ref,onMounted} from "vue";

export default {
  mixins : [mixin],
  name: 'StudentDashBoard',
  components: {DropDown, FontAwesomeIcon, Navigation},
  setup(){
    const dropdownState = ref(false)
    const email = ref(mixin.methods.getCookieValue('email'))
    function changeDropdownState(){
      dropdownState.value = !dropdownState.value
    }
    onMounted(() => {
      console.log(mixin.methods.getCookieValue('email'))
    })
    return {
      dropdownState,
      changeDropdownState,
      email
    }
  }
}
</script>
<style scoped lang="sass">
  .drop-down
    position: absolute
</style>