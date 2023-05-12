<template>
  <div class="content-carousel">
    <h2>
      <strong>{{ description }}</strong>
    </h2>
    <Carousel v-bind="settings" :breakpoints="breakpoints">
      <Slide v-for="book in books.books" :key="book">
        <div class="carousel__item">
          <carousel-item :isDonation="isDonation" :book="book"></carousel-item>
        </div>
      </Slide>
      <template #addons>
        <Navigation />
      </template>
    </Carousel>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { Carousel, Navigation, Slide } from "vue3-carousel";
import "vue3-carousel/dist/carousel.css";
import CarouselItem from "./CarouselItem.vue";
import books from "../../../public/fake-data/fake-data.json";
export default defineComponent({
  name: "CarouselComp",
  components: {
    Carousel,
    Slide,
    Navigation,
    CarouselItem,
  },
  props: {
    description: String,
    isDonation: Boolean,
  },
  data: () => ({
    settings: {
      itemsToShow: 1,
      snapAlign: "center",
    },
    breakpoints: {
      700: {
        itemsToShow: 3.5,
        snapAlign: "center",
      },
      1024: {
        itemsToShow: 7,
        snapAlign: "start",
      },
    },
    books,
  }),
});
</script>

<style scoped>
.content-carousel {
  margin: 3rem;
  background-color: #ffffff;
}
h2 {
  margin-top: 3rem;
  margin-bottom: 1rem;
  padding-top: 2rem;
}
</style>
