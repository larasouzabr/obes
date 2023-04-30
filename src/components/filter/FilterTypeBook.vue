<template>
  <div class="options" v-for="option in filterOptions" :key="option.id">
    <input
      class="input-checkbox"
      type="checkbox"
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
  name: "FilterTypeBook",
  data() {
    const books = fakeBooks.books;
    return {
      books,
      filterOptions: [
        {
          id: "new",
          label: `Novo (${
            books.filter((book) => book.condition === "new").length
          })`,
          value: "new",
        },
        {
          id: "semi-new",
          label: `Semi-novo (${
            books.filter((book) => book.condition === "semi-new").length
          })`,
          value: "semi-new",
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
        const filteredList = this.books.filter((item) =>
          this.selectedOptions.includes(item.condition)
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

.input-checkbox {
  background: #decffb;
  position: absolute;
  appearance: none;
  cursor: pointer;
  width: 20px;
  height: 20px;
  border-radius: 4px;
  border: 2px solid #fff;
  left: -25px;
}
.input-checkbox:checked {
  background: #432876;
}
</style>
