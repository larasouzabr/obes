<template>
  <div class="catalog">
    <div v-for="book in paginatedBooks" :key="book.id">
      <book :book="book" />
    </div>
    <div v-if="hasPages" class="pages">
      <button @click="prevPage" :disabled="!hasPrev">Anterior</button>
      <button
        v-for="page in totalPages"
        :key="page"
        @click="selectedPage = page - 1"
        :disabled="selectedPage === page - 1"
      >
        {{ page }}
      </button>
      <button @click="nextPage" :disabled="!hasNext">Próxima</button>
    </div>
  </div>
</template>

<script>
import Book from "./CatalogBook.vue";

export default {
  components: {
    Book,
  },
  props: {
    books: {
      type: Array,
      required: true,
    },
    perPage: {
      type: Number,
      default: 7,
    },
  },
  data() {
    return {
      selectedPage: 0,
    };
  },
  computed: {
    totalPages() {
      return Math.ceil(this.books.length / this.perPage);
    },
    paginatedBooks() {
      const start = this.selectedPage * this.perPage;
      const end = start + this.perPage;
      return this.books.slice(start, end);
    },
    hasPages() {
      return this.totalPages > 1;
    },
    hasNext() {
      return this.selectedPage < this.totalPages - 1;
    },
    hasPrev() {
      return this.selectedPage > 0;
    },
  },
  methods: {
    nextPage() {
      if (this.hasNext) {
        this.selectedPage++;
      }
    },
    prevPage() {
      if (this.hasPrev) {
        this.selectedPage--;
      }
    },
  },
};
</script>

<style scoped>
button {
  margin: 1rem;
  background: #f9f2ff;
  border: 3px solid #925ff0fc;
  border-radius: 4px;
  padding: 10px 20px;
}

.catalog {
  display: grid;
  align-content: start;
  justify-items: center;
  height: 100%;
  gap: 20px;
}
</style>
