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
  background-color: #5e3a9e;
  /* background-color: #5E3A9E; */
  /* background: #decffb; */
  background-image: linear-gradient(135deg, #be9ff6, #decffb);
  background-repeat: no-repeat;
  /* background-color: #5E3A9E; */
  font-family: "Poppins", sans-serif;
}

a {
  text-decoration: none;
}
</style>
