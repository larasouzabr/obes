<template>
  <LoginPage />
</template>

<script>
import LoginPage from "./view/LoginPage.vue";

export default {
  name: "App",
  components: {
    LoginPage,
  },
};
</script>
<style>
body {
  margin: 0px;
  background: #decffb;
  font-family: "Poppins", sans-serif;
}

a {
  text-decoration: none;
}
</style>
