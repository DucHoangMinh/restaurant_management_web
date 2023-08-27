<template>
  <div id="footer">
    <v-container>
      <v-label class="pt-8 text-h6 font-weight-bold">Hệ thống quản lý trường trung học phổ thông ABC</v-label>
      <v-label>Hệ thống quản lý trường trung học phổ thông ABC là nền tảng công nghệ hỗ trợ việc tổ chức, quản lý thông <br> tin và tương tác trong
        môi trường học tập, giúp cải thiện hiệu suất và trải nghiệm cho học sinh, giáo viên và quản lý trường.</v-label>
      <div class="connect-list">
        <font-awesome-icon class="pa-4" icon="fa-solid fa-link" />
        <font-awesome-icon class="pa-4" icon="fa-solid fa-link" />
        <font-awesome-icon class="pa-4" icon="fa-solid fa-link" />
        <font-awesome-icon class="pa-4" icon="fa-solid fa-link" />
        <font-awesome-icon class="pa-4" icon="fa-solid fa-link" />
      </div>
    </v-container>
  </div>
</template>
<script>
  export default {
    name: "Footer"
  }
</script>
<style>
  #footer{
    background-color: #ccc;
    height: 200px;
    position: relative;
    bottom: 0px;
    width: 100vw;
  }
  label{
    word-wrap: break-word;
    white-space: normal;
  }
</style>