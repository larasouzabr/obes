<template>
  <div class="book">
    <img :src="book.image" alt="Capa do livro" class="cover" />

    <div>
      <h3 class="title">{{ book.title }}</h3>
      <span class="author"
        >{{ book.author }} | {{ book.publication_year }}</span
      >
    </div>

    <div class="sold">
      <p class="soldby">Vendido por:</p>
      <p class="seller">Robertinha Rafaela</p>
      <div class="stars">
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

    <div class="buy">
      <a class="button">Comprar</a>
    </div>
  </div>
</template>

<script>
import StarRating from "vue-star-rating";

export default {
  props: {
    book: {
      type: Object,
      required: true,
    },
  },
  components: {
    StarRating,
  },
};
</script>

<style scoped>
p {
  margin: 0px;
}

.book {
  border-width: 0px 3px 3px 0px;
  border-style: solid;
  border-color: #432876;
  margin-bottom: 25px;
}

.book {
  display: grid;
  grid-template-columns: 1fr 3fr 1fr;
}

.cover {
  grid-row: 1 / -3;
  max-width: 80%;
}

.buy {
  grid-column: 3;
  grid-row: 1 / -3;
  display: grid;
  align-content: space-between;
  justify-items: end;
  padding: 25px;
}

.button {
  background: #432876;
  color: #fff;
  padding: 15px 30px;
  border-radius: 9px;
  transition: 0.5s;
}

.button:hover {
  background: #432876e3;
}

.title {
  font-size: 1.6rem;
  font-weight: bold;
}

.author {
  font-size: 1.3rem;
  font-weight: 400;
}

.sold {
  font-size: 0.8rem;
  line-height: 1.3rem;
}

.soldby {
  font-weight: 400;
}

.seller {
  font-weight: bold;
}
</style>
