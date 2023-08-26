<template>
  <div class="home-navigation">
    <router-link style="color: #fff;text-decoration: none;float: right" to="/login" class="">Đăng nhập</router-link>
  </div>
</template>
<script>
  export default {
    name:'HomePage',
  }
</script>
<style>
.home-navigation{
  height: 50px;
  width: 100%;
  position:fixed;
  top: 0;
  background-color: forestgreen;
}
</style>