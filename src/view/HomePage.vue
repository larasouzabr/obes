<template>
    <BannerMain></BannerMain>
    <div class="categories">
        <CarouselComp :description="'Novidades no Sebo'"></CarouselComp>
        <CarouselComp :description="'Novidades em Doações'" :is-donation="true"></CarouselComp>
    </div>
  

</template>

<script>
import BannerMain from '@/components/BannerMain.vue';
import CarouselComp from '@/components/carousel/CarouselComp.vue';

export default {
    name: "HomePage",
    components: { BannerMain, CarouselComp },
};
</script>  

<style scoped>
.categories{
  margin:3rem;
  background-color: #FFFFFF;
  border-radius: 16px;
}
</style>
