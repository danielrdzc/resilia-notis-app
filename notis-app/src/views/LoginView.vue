<template>
    <v-container class="no-padding" fill-height fluid>
      <div class="blue-background"></div>
      <login-card></login-card>
    </v-container>
  </template>

  <script>
// @ is an alias to /src
import LoginCard from '@/components/login/LoginCard.vue';

export default {
  name: 'login',
  components: {
    LoginCard,
  },
};
</script>

<style scoped>
.no-padding {
  padding: 0;
}

.blue-background {
  width: 100%;
  height: 100vh;
  background-color: #0d1d4ee3;
  position: absolute;
  top: 0%;
}
</style>