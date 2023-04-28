<template>
  <div class="options" v-for="option in filterOptions" :key="option.id">
    <input
      class="input-checkbox"
      type="checkbox"
      :id="option.id"
      :value="option.value"
      v-model="selectedOptions"
    />
    <label :for="option.id">{{ option.label }}</label>
  </div>
</template>

<script>
export default {
  name: "FilterYear",
  data() {
    return {
      list: [
        { id: 1, name: "Livro A", category: "new" },
        { id: 2, name: "Livro B", category: "semi-new" },
        { id: 3, name: "Livro C", category: "new" },
        { id: 4, name: "Livro D", category: "semi-new" },
      ],
      filterOptions: [
        { id: "2013", label: "2013 (8)", value: "2013" },
        { id: "2023", label: "2023 (8)", value: "2023" },
        { id: "2008", label: "2008 (8)", value: "2008" },
      ],
      selectedOptions: [],
    };
  },
  computed: {
    filteredList() {
      if (this.selectedOptions.length === 0) {
        return this.list;
      } else {
        return this.list.filter((item) =>
          this.selectedOptions.includes(item.category)
        );
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
