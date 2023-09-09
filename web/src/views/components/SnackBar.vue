<template>
    <v-snackbar
      :timeout="2000"
      v-model="showSnackbarState"
    >
      {{ message }}
    </v-snackbar>
</template>
<style>
</style>
<script>
import {ref,watch} from 'vue'
export default {
  props: {
    timeout: {
      type: Number,
      default: 2000,
    },
    message: String,
    showSnackbar: Boolean
  },
  setup(props){
    const showSnackbarState = ref(true)
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