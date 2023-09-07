<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="home-navigation">
    <v-container class="d-flex align-center justify-space-between">
      <router-link class="pl-12" to="/" style="color: white">
        <font-awesome-icon icon="fa-solid fa-house" />
        Trang chủ
      </router-link>
      <slot>
        <router-link style="color: #fff;float: right" to="/login" class="pr-12">
          Đăng nhập
        <font-awesome-icon icon="fa-solid fa-right-to-bracket" />
      </router-link>
      </slot>
    </v-container>
  </div>
</template>
<script>
  export default {
    name: "Navigation",
  }
</script>
<style>
.home-navigation{
  height: 50px;
  width: 100%;
  position:fixed;
  top: 0;
  background-color: forestgreen;
  z-index: 10;
}
a{
  text-decoration: none;
}
</style>