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
      <div class="stars">stars</div>
    </div>

    <div class="buy">
      <div>
        <span v-if="book.price == 0" class="donated">Doação</span>
      </div>
      <a class="button">Comprar</a>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    book: {
      type: Object,
      required: true,
    },
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

.donated {
  background: #a87ff3;
  color: #e9dffc;
  padding: 5px 10px;
  border-radius: 4px;
  font-size: 0.85rem;
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
