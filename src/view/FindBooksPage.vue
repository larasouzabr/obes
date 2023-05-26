<template>
  <div class="content">
    <section>
      <h2 class="caption">Filtros</h2>
      <div class="block filters">
        <div class="filter">
          <h3 class="category">Tipo do livro</h3>
          <form action="" method="post">
            <FilterTypeBook :books="books" @event="updateFilterType" />
          </form>
        </div>

        <div class="filter">
          <h3 class="category">Preço</h3>
          <form action="" method="post">
            <FilterPrice :books="books" @event="updateFilterPrice" />
          </form>
        </div>

        <div class="filter">
          <h3 class="category">Ano da publicação</h3>
          <FilterYear :books="books" @event="updateFilterYear" />
        </div>
      </div>

      <h2 class="caption">Reviews</h2>
      <div class="block reviews">
        <article class="review">
          <p>
            Crepúsculo é um livro bom, a leitura ocorre de forma ágil e é um bom
            passatempo para uma tarde chuvosa de sábado. De arrancar suspiros
            dos leitores que gostam do gênero, o livro cumpre sua meta de ser um
            romance voltado para adolescentes que gostam de paixões perigosas e
            impossíveis.
          </p>
          <div class="stars">
            <span>estrelas</span>
          </div>
        </article>

        <article class="review">
          <p>
            Eu amei relembrar esse romance! Algumas vezes a leitura se arrastou,
            mas considerando o número de páginas já era de se esperar que isso
            fosse acontecer. Apesar dos pesares, mal posso esperar pelos
            próximos volumes!
          </p>
          <div class="stars">
            <span>estrelas</span>
          </div>
        </article>

        <article class="review">
          <p>
            A leitura do primeiro volume da Saga Crepúsculo é muito divertido,
            apesar de capítulos relativamente grandes é uma leitura fluida e
            leve, sem grandes surpresas, mas instigando o leitor a continuar
            lendo para buscar um final feliz na história de amor dos pombinhos
            vampirinhos protagonistas. Ou até quando Jacob Black deixar isso
            acontecer…
          </p>
          <div class="stars">
            <span>estrelas</span>
          </div>
        </article>
      </div>
    </section>

    <main class="catalog">
      <CatalogComp :books="filteredBooks" />
    </main>
  </div>
</template>

<script>
import FilterTypeBook from "../components/filter/FilterTypeBook.vue";
import FilterPrice from "../components/filter/FilterPrice.vue";
import FilterYear from "../components/filter/FilterYear.vue";
import CatalogComp from "../components/catalog/CatalogComp.vue";
import fakeBooks from "../../public/fake-data/fake-books.json";

export default {
  name: "FindBooksPage",
  components: {
    FilterTypeBook,
    FilterPrice,
    FilterYear,
    CatalogComp,
  },
  data() {
    const books = fakeBooks.books;
    const filteredBooks = books;
    const subBooksType = books;
    const subBooksPrice = books;
    const subBooksYear = books;

    return {
      books,
      filteredBooks,
      subBooksType,
      subBooksPrice,
      subBooksYear,
    };
  },
  methods: {
    updateFilteredBooks() {
      this.filteredBooks = this.subBooksType.filter(
        (book) =>
          this.subBooksPrice.includes(book) && this.subBooksYear.includes(book)
      );
    },
    updateFilterType(filteredList) {
      this.subBooksType = filteredList;
      this.updateFilteredBooks();
    },
    updateFilterPrice(filteredList) {
      this.subBooksPrice = filteredList;
      this.updateFilteredBooks();
    },
    updateFilterYear(filteredList) {
      this.subBooksYear = filteredList;
      this.updateFilteredBooks();
    },
  },
};
</script>

<style scoped>
.content {
  background: #fff;
  margin: 3rem;
  border-radius: 16px;
  /* padding: 3rem; */
  display: grid;
  grid-template-columns: 1fr 2fr;
}

.content section {
  background: #432876;
  border-radius: 16px 0px 0px 16px;
  padding-top: 10px;
}

.filters {
  background: #925ff0fc;
}

.reviews {
  background: #e9dffc;
}

.block {
  max-width: 95%;
  margin: 0px auto 50px;
  border-radius: 16px;
  padding: 15px 25px;
}

.caption {
  color: #fff;
  font-size: 2.5rem;
  margin: 0px;
  text-align: center;
}

.category {
  background: #29154d;
  color: #fff;
  font-size: 1.8rem;
  text-align: center;
  padding: 10px 20px;
  border-radius: 4px;
  margin: 0px;
}

.review {
  background: #f5f5f580;
  border-radius: 5px;
  padding: 15px 25px;
  margin-bottom: 1.8rem;
}

.review:last-child {
  margin-bottom: 0px;
}

main.catalog {
  padding: 25px 45px 0px 45px;
}
</style>
