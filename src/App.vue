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
  font-family: "Poppins", sans-serif;
}

a {
  text-decoration: none;
}
</style>
