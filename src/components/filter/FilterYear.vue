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
  name: "FilterYear",
  data() {
    const books = fakeBooks.books;
    return {
      books,
      filterOptions: [
        {
          id: "y2008",
          label: `2008 (${
            books.filter((book) => book.publication_year <= 2008).length
          })`,
          value: 2008,
        },
        {
          id: "y2013",
          label: `2013 (${
            books.filter((book) => book.publication_year <= 2013).length
          })`,
          value: 2013,
        },
        {
          id: "y2023",
          label: `2023 (${
            books.filter((book) => book.publication_year <= 2023).length
          })`,
          value: 2023,
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
          (item) => item.publication_year <= Math.max(this.selectedOptions)
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
