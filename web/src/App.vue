<!-- eslint-disable no-unused-vars -->
<template>
  <router-view></router-view>
  <SnackBar></SnackBar>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import SnackBar from './views/components/SnackBar.vue'
export default {
  name: 'App',
  components: {
    SnackBar
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
