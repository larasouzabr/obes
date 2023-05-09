<template>
  <section class="container">
    <profileHeader :user="user"></profileHeader>
    <overall-info :user="user"></overall-info>
    <available-books :type="venda" :books="user.forSelling"></available-books>
    <available-books :type="doacao" :books="user.forDonation"></available-books>
  </section>
</template>

<script>
import profileHeader from "@/components/profile/HeaderInfo.vue";
import OverallInfo from "@/components/profile/OverallInfo.vue";
import AvailableBooks from "@/components/profile/AvailableBooks.vue";
import user from "../../public/fake-data/profile.json";
export default {
  name: "ProfilePage",
  components: {
    profileHeader,
    OverallInfo,
    AvailableBooks,
  },
  data: () => ({
    venda: "venda",
    doacao: "doação",
    user,
  }),
  mounted() {
    document.body.style.background = "#F9F2FF";
  },
};
</script>

<style>
body {
  background-color: #f9f2ff;
}
</style>
