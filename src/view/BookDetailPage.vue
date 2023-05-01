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
          <span>Rafaella Santos</span>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  name: "BookDetailPage",
  data() {
    return {
      book: JSON.parse(this.$route.query.book),
    };
  },
};
</script>

<style scoped>
.main-detail {
  width: 70vw;
  height: 100vh;
  margin: 0px auto;
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
