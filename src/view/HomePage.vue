<template>
  <BannerMain></BannerMain>
  <div class="categories">
    <CarouselComp :description="'Novidades no Sebo'"></CarouselComp>
    <CarouselComp
      :description="'Novidades em Doações'"
      :is-donation="true"
    ></CarouselComp>
  </div>
</template>

<script>
import BannerMain from "@/components/BannerMain.vue";
import CarouselComp from "@/components/carousel/CarouselComp.vue";

export default {
  name: "HomePage",
  components: { BannerMain, CarouselComp },
  mounted() {
    document.body.style.background = "#5E3A9E";
  },
};
</script>

<style scoped>
.categories {
  margin: 3rem;
  background-color: #ffffff;
  border-radius: 16px;
}
</style>
