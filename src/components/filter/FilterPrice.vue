<template>
  <div class="options" v-for="option in filterOptions" :key="option.id">
    <input
      class="input-radio"
      type="radio"
      :id="option.id"
      :value="option.value"
      v-model="selectedOptions"
      @change="filteredList"
    />
    <label :for="option.id">{{ option.label }}</label>
  </div>
</template>

<script>
import fakeBooks from "../../../public/fake-data/fake-books.json";

export default {
  name: "FilterPrice",
  data() {
    const books = fakeBooks.books;
    return {
      books,
      filterOptions: [
        {
          id: "donated",
          label: `0,00 (Doados) (${
            books.filter((book) => book.price === 0).length
          })`,
          value: 0,
        },
        {
          id: "price10",
          label: `Até 10 reais (${
            books.filter((book) => book.price <= 10).length
          })`,
          value: 10,
        },
        {
          id: "price14",
          label: `Até 14 reais (${
            books.filter((book) => book.price <= 14).length
          })`,
          value: 14,
        },
        {
          id: "price18",
          label: `Até 18 reais (${
            books.filter((book) => book.price <= 18).length
          })`,
          value: 18,
        },
        {
          id: "price23",
          label: `Até 23 reais (${
            books.filter((book) => book.price <= 23).length
          })`,
          value: 23,
        },
      ],
      selectedOptions: [],
      booksFiltered: [],
    };
  },
  methods: {
    filteredList() {
      if (this.selectedOptions.length === 0) {
        this.booksFiltered = this.books;
        this.$emit("event", this.booksFiltered);
      } else {
        const filteredList = this.books.filter(
          (item) => item.price <= Math.max(this.selectedOptions)
        );

        this.booksFiltered = filteredList;
        this.$emit("event", this.booksFiltered);
      }
    },
  },
};
</script>

<style scoped>
label {
  color: #fff;
}

.options {
  position: relative;
  max-width: 70%;
  margin: 20px auto;
}

.input-radio {
  background: #decffb;
  position: absolute;
  appearance: none;
  cursor: pointer;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  border: 2px solid #fff;
  left: -25px;
}
.input-radio:checked {
  background: #432876;
}
</style>
