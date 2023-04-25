<template>
  <NavBar></NavBar>
  <BannerMain></BannerMain>
  <h1>This is the home page</h1>
</template>

<script>
import BannerMain from "@/components/BannerMain.vue";
import NavBar from "../components/NavBar.vue";

export default {
  name: "HomePage",
  components: { BannerMain, NavBar },
};
</script>
