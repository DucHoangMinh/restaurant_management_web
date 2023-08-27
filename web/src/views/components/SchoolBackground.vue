<template>
  <div class="image-bgr">
    <img src="../../assets/students.png">
  </div>
</template>
<style>
  .image-bgr {
    position: relative;
    width: 700px;
    height: 700px;
    display: flex;
    align-items: center;
  }
  img{
    position: absolute;
    width: 100%;
    opacity: 0.9;
    object-fit: fill;
  }
</style>
<script>
  export default {
    name:'SchoolBackground'
  }
</script>