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
  name: "FilterPrice",
  data() {
    return {
      list: [
        { id: 1, name: "Livro A", category: "new" },
        { id: 2, name: "Livro B", category: "semi-new" },
        { id: 3, name: "Livro C", category: "new" },
        { id: 4, name: "Livro D", category: "semi-new" },
      ],
      filterOptions: [
        { id: "donated", label: "0,00 (Doados) (3)", value: "0" },
        { id: "price10", label: "Até 10 reais (3)", value: "<=10" },
        { id: "price14", label: "Até 14 reais (8)", value: "<=14" },
        { id: "price18", label: "Até 18 reais (8)", value: "<=18" },
        { id: "price23", label: "Até 23 reais (8)", value: "<=23" },
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
