<template>
  <section class="section">
    <span class="section-title">{{ description }}</span>
    <div v-if="!isOnInstProf">
      <div v-if="books.length == 0" class="no-content">
        Não há nada aqui! Clique em "Quero
        {{ type == "donation" ? "Doar" : "Vender" }}" para adicionar novos
        livros
      </div>
      <div class="items">
        <carousel-item-profile-page-vue
          v-for="book in books"
          :key="book"
          :isOnProfile="true"
          :book="book"
          class="item"
        ></carousel-item-profile-page-vue>
      </div>
    </div>
    <div v-else>
      <div v-if="books.length == 0" class="no-content">
        Não há nada aqui! Solicite novas doações na tela principal
      </div>
      <div class="items">
        <carousel-item-inst
          v-for="book in books"
          :key="book"
          :book="book"
          class="item"
        ></carousel-item-inst>
      </div>
    </div>
  </section>
</template>

<script>
import CarouselItemProfilePageVue from "../carousel/CarouselItemProfilePage.vue";
import CarouselItemInst from "../carousel/CarouselItemInst.vue";
export default {
  components: { CarouselItemProfilePageVue, CarouselItemInst },
  name: "availableBooks",
  props: {
    type: String,
    books: Object,
    description: String,
    isOnInstProf: Boolean,
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

.no-content {
  display: flex;

  justify-content: center;
  font-size: larger;
  margin-top: 5%;
}

.section-title {
  width: 100%;
  background-color: #432876;
  color: #e9dffc;
  font-size: 45px;
  text-align: center;
}
</style>
