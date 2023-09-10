<template lang="pug">
v-snackbar(:timeout='5000' v-model='showSnackbarState' close-on-content-click='' color='green' position='fixed' style='top: 0px; right: 0px' location-strategy='connected')
  .d-flex.align-center
    font-awesome-icon(icon="fa-solid fa-circle-info")
    label.pl-2 {{message}}
</template>
<style lang="sass" scoped>
</style>
<script>
import {ref,watch} from 'vue'
export default {
  props: {
    timeout: {
      type: Number,
      default: 5000,
    },
    message: String,
    showSnackbar: Boolean
  },
  setup(props){
    const showSnackbarState = ref(false)
    watch(() => props.showSnackbar, (newData) => {
      showSnackbarState.value = newData
      console.log(newData)
    })
    return {
      showSnackbarState
    }
  }
}
</script>