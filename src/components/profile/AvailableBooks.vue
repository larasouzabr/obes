<template>
  <section class="section">
    <span class="section-title">Livros disponíveis para {{ type }}</span>
    <div class="items">
      <carousel-item
        v-for="book in books"
        :key="book"
        :isOnProfile="true"
        :book="book"
        class="item"
      ></carousel-item>
    </div>
  </section>
</template>

<script>
import CarouselItem from "../carousel/CarouselItem.vue";
export default {
  components: { CarouselItem },
  name: "availableBooks",
  props: {
    type: String,
    books: Object,
  },
};
</script>

<style scoped>
.section {
  display: flex;
  flex-direction: column;
  margin-bottom: 3rem;
}
.item {
  margin-top: 5px;
}
.items {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  margin: 1rem;
}

.section-title {
  width: 100%;
  background-color: #432876;
  color: #e9dffc;
  font-size: 45px;
  text-align: center;
}
</style>
