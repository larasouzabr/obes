<template>
  <section class="section">
    <span class="section-title">Livros disponíveis para {{ type }}</span>
    <div></div>
  </section>
</template>

<script>
export default {
  name: "availableBooks",
  props: {
    type: String,
  },
};
</script>

<style scoped>
.section {
  display: flex;
  flex-direction: row;
  margin-bottom: 3rem;
}
.section-title {
  width: 100%;
  background-color: #432876;
  color: #e9dffc;
  font-size: 45px;
  text-align: center;
}
</style>
