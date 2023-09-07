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
            v-model="email"
          ></v-text-field>
          <v-text-field
            type="password"
            label="Password"
            variant="outlined"
            class="pb-4"
            v-model="password"
          ></v-text-field>
          <v-btn color="green" @click="handleLogin">Đăng nhập</v-btn>
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
import axios from "axios";
import {useRouter} from "vue-router"

export default defineComponent({
  components: {Footer, Navigation, SchoolBackground},
  setup(){
    const ROUTER = useRouter()
    const role_selection = ref('Học sinh')
    const email = ref(null)
    const password = ref(null)
    function save_token_to_cookie(access_token){
      document.cookie = `token=${access_token};path=/`
    }
    async function handleLogin() {
      const account = {
        email:email.value,
        password:password.value
      }
      console.log(account)
      let response = await axios.post('http://127.0.0.1:5000/login', account)
      await save_token_to_cookie(response.data[0].token)
      document.cookie = `email=${response.data[1].email};path=/`
      ROUTER.push('/student/dashboard')
    }
    return {
      role_selection,
      email,
      password,
      handleLogin
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