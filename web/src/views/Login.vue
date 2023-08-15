<!-- eslint-disable no-undef -->
<!-- eslint-disable no-unused-vars -->
<!-- eslint-disable vue/multi-word-component-names -->
<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div class="d-flex align-center justify-center" style="height: 100vh">
        <v-sheet width="400" class="mx-auto">
            <v-form fast-fail>
                <v-label class="mb-6 text-black">Vui lòng đăng nhập để sử dụng dịch vụ</v-label>
                <v-text-field v-model="email" label="Email" type="email"></v-text-field>
                <v-text-field v-model="password" label="Password" type="password"></v-text-field>
                <a href="#" class="text-body-2 font-weight-regular">Forgot Password?</a>
                <v-btn color="green" block class="mt-2" @click="handleSubmitLogin">Sign in</v-btn>
            </v-form>
            <div class="mt-2">
                <p class="text-body-2">Don't have an account? <a href="#">Sign Up</a></p>
            </div>
        </v-sheet>
    </div>
</template>
<script>
// eslint-disable-next-line no-unused-vars
import { useVuelidate } from '@vuelidate/core'
// eslint-disable-next-line no-unused-vars
import { required, email } from '@vuelidate/validators'
export default {
    name: 'LoginPage',
    data() {
        return {
            password: '',
            email: '',
        }
    },
    methods: {
        handleSubmitLogin() {
            console.log('Hoang Minh Duc')
        }
    },
}
</script>
<style></style>