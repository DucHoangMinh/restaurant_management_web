<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="d-flex align-center justify-space-around position-relative">
    <div class="">
      <v-sheet width="350" class="">
        <v-form fast-fail @submit.prevent>
          <v-label style="color: black" class="ma-8 text-h5">Đăng nhập vào hệ thống</v-label>
          <v-text-field
            type="email"
            label="Email"
            variant="outlined"
          ></v-text-field>
          <v-text-field
            type="password"
            label="Password"
            variant="outlined"
          ></v-text-field>
          <v-btn color="green">Đăng nhập</v-btn>
        </v-form>
      </v-sheet>
    </div>
    <SchoolBackground class=""></SchoolBackground>
  </div>
</template>
<script>
import SchoolBackground from "@/views/homepage/SchoolBackground.vue";
import {defineComponent} from "vue";

export default defineComponent({
  components: {SchoolBackground}
})


</script>
<style></style>