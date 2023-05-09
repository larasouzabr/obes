<template>
  <nav-bar></nav-bar>
  <router-view />
</template>

<script>
import NavBar from "./components/NavBar.vue";

export default {
  name: "App",
  components: {
    NavBar,
  },
};
</script>
<style>
body {
  margin: 0px;
  background-image: linear-gradient(135deg, #be9ff6, #decffb);
  background-repeat: no-repeat;
  font-family: "Poppins", sans-serif;
  height: 100vh;
}

a {
  text-decoration: none;
}
</style>
