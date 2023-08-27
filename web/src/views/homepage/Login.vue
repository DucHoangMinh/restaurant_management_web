<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <Navigation></Navigation>
  <div class="d-flex align-center justify-space-around position-relative">
    <div class="">
      <v-sheet width="350" class="">
        <v-form fast-fail @submit.prevent>
          <v-label style="color: black" class="ma-8 text-h5">Đăng nhập vào hệ thống</v-label>
          <div class="d-flex align-center pb-6">
            <v-label class="pr-4">Chọn vai trò của bạn: </v-label>
            <v-select
                density="compact"
                v-model="role_selection"
                variant="outlined"
                :items="['Giáo viên', 'Học sinh', 'Người quản trị']"/>
          </div>
          <v-text-field
            type="email"
            label="Email"
            variant="outlined"
            class="pb-4"
          ></v-text-field>
          <v-text-field
            type="password"
            label="Password"
            variant="outlined"
            class="pb-4"
          ></v-text-field>
          <v-btn color="green">Đăng nhập</v-btn>
        </v-form>
      </v-sheet>
    </div>
    <SchoolBackground class=""></SchoolBackground>
  </div>
  <Footer></Footer>
</template>
<script>
import SchoolBackground from "@/views/components/SchoolBackground.vue";
import Navigation from "@/views/components/Navigation.vue";
import Footer from "@/views/components/Footer.vue";
import {defineComponent, ref} from "vue";

export default defineComponent({
  components: {Footer, Navigation, SchoolBackground},
  setup(){
    const role_selection = ref('Học sinh')
    return {
      role_selection
    }
  }
},

)
</script>
<style scoped>
.v-input__details{
  display: none !important;
}
</style>