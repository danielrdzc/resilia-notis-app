<template>
  <v-app style="background-color: #f5f5f5;">
    <app-navbar v-if="$route.name != 'login'"></app-navbar>
    <router-view/>
  </v-app>
</template>

<script>
import AppNavbar from '@/components/AppNavbar.vue';

export default {
  name: 'App',

  components: {
    AppNavbar,
  },

  data: () => ({
  }),
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
