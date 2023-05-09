<template>
  <main class="main-detail">
    <div class="content">
      <div>
        <img :src="book.image" alt="Capa do livro" class="cover" />
      </div>
      <div class="details">
        <h3 class="title">{{ book.title }}</h3>

        <span class="category">{{ book.category }}</span>

        <div class="description">
          <span>{{ book.title }}. </span><span>{{ book.publisher }}. </span>
          <span>{{ book.cover_type }} </span
          ><span>{{ book.condition_description }}. </span
          ><span>Tamanho: {{ book.dimensions }}. </span
          ><span>Páginas: {{ book.pages }}</span>
        </div>

        <div class="purchase-inf">
          <div v-if="book.price == 0">
            <p>Este produto está disponível para doação!</p>
            <a href="#" class="button donate">Solicitar doação</a>
          </div>
          <div v-else>
            <p class="price">R$ {{ book.price }}</p>
            <a href="#" class="button add">Adicionar ao carrinho</a>
          </div>

          <span class="soldby">Vendido por:</span>

          <div class="info-user">
            <span>Rafaella Santos</span>
            <star-rating
              v-bind:increment="0.5"
              v-bind:max-rating="5"
              inactive-color="#E9ECEF"
              v-bind:star-size="20"
              v-bind:show-rating="false"
              v-bind:rating="4.0"
              v-bind:read-only="true"
            />
          </div>
        </div>
      </div>
    </div>
  </main>
  <CarouselComp
    :description="'Outras opções parecidas'"
    class="carousel"
  ></CarouselComp>
</template>

<script>
import StarRating from "vue-star-rating";
import CarouselComp from "@/components/carousel/CarouselComp.vue";

export default {
  name: "BookDetailPage",
  components: {
    StarRating,
    CarouselComp,
  },
  data() {
    return {
      book: JSON.parse(this.$route.query.book),
    };
  },
  mounted() {
    document.body.style.background =
      "linear-gradient(to bottom, #DECFFB, #FFFFFF) no-repeat";
  },
};
</script>

<style scoped>
body {
  background-color: #a87ff3 !important;
}

.main-detail {
  width: 70vw;
  height: 75vh;
  margin: 0px auto;
}
.info-user {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.content {
  display: grid;
  grid-template-columns: 1fr 2fr;
  justify-items: center;
  gap: 20px;
  width: 90%;
  margin: 40px auto 0px;
  text-align: center;
}

.details {
  display: grid;
  align-content: space-between;
  justify-items: center;
  align-content: center;
  gap: 50px;
}

.cover {
  max-width: 100%;
}

.title {
  font-size: 3.1rem;
  font-weight: bold;
}

.category {
  color: #a87ff3;
  font-weight: bold;
}

.description {
  color: #432876;
}

.purchase-inf {
  display: grid;
}

.price {
  font-size: 4.25rem;
  color: #29154d;
}

.button {
  display: inline-block;
  background: #432876;
  color: #decffb;
  padding: 15px 30px;
  border-radius: 4px;
}

.soldby {
  color: #29154d7a;
  font-weight: bold;
}
</style>
