<template>
  <Navigation></Navigation>
  <div id="body" class="d-flex justify-space-between">
    <div class="detail pa-16 d-flex align-center" style="box-sizing: border-box;">
      <label>Trang quản lý đào tạo của trường Trung Học Phổ Thông HighSchool. <br> Vui lòng
        <router-link to="/login" style="text-decoration: underline">đăng nhập</router-link>
        để tiếp tục sử dụng dịch vụ.</label>
    </div>
    <SchoolBackground></SchoolBackground>
  </div>
  <Footer></Footer>
</template>
<script>
  import Navigation from "@/views/components/Navigation.vue";
  import SchoolBackground from "@/views/components/SchoolBackground.vue";
  import Footer from "@/views/components/Footer.vue";
  export default {
    name:'HomePage',
    components: {Footer, SchoolBackground, Navigation},
  }
</script>
<style>
#body{
}
</style>