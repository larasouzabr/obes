<template>
  <section class="container">
    <profileHeader :imageUrl="imageUrl"></profileHeader>
    <overall-info></overall-info>
    <available-books :type="venda"></available-books>
    <available-books :type="doacao"></available-books>
  </section>
</template>

<script>
import profileHeader from "@/components/profile/HeaderInfo.vue";
import OverallInfo from "@/components/profile/OverallInfo.vue";
import AvailableBooks from "@/components/profile/AvailableBooks.vue";

export default {
  name: "ProfilePage",
  components: {
    profileHeader,
    OverallInfo,
    AvailableBooks,
  },
  data() {
    return {
      imageUrl:
        "https://conteudo.imguol.com.br/c/entretenimento/80/2017/04/25/a-atriz-zoe-saldana-como-neytiri-em-avatar-1493136439818_v2_1x1.jpg",
      venda: "venda",
      doacao: "doação",
    };
  },
};
</script>

<style>
body {
  background-color: #f9f2ff;
}
</style>
