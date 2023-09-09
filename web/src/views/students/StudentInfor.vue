<template lang="pug">
v-container
  v-row
    v-col
      .v-col-6.ma-auto
        label Thông tin của Hoàng Minh Đức
        .information
          .infor-item.d-flex.justify-start
            label Họ và tên:
            v-text-field(variant="outlined" density="compact")
          .infor-item.d-flex.justify-start
            label Ngày sinh:
            v-btn(@click="() => {datepickerState = !datepickerState}") 01/01/1990
            v-date-picker(show-adjacent-months='' v-if="datepickerState")
          .infor-item.d-flex.justify-start
            label Email:
            v-text-field(variant="outlined" density="compact")
          .infor-item.d-flex.justify-start
            label Phone:
            v-text-field(variant="outlined" density="compact")
          .infor-item.d-flex.justify-start
            label Address:
            v-textarea(variant="outlined" density="compact" rows="3" )


</template>
<script>
import {ref} from 'vue'
import { VDatePicker } from 'vuetify/labs/VDatePicker'
  export default{
    name: 'StudentInfor',
    components: {
      VDatePicker,
    },
    setup(){
      const datepickerState = ref(false)
      return {
        datepickerState
      }
    }
  }
</script>
<style lang="sass" scoped>

</style>