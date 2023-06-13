<template>
  <div class="container">
    <div class="image">
      <img :src="book.book.image_url" alt="" />
    </div>
    <div class="information">
      <span class="bookName"
        ><strong> {{ book.book.title }}</strong></span
      >
    </div>
    <div class="status">
      <button class="btn-outline" type="submit">
        {{ book.status == "PENDING" ? "Solicitado" : "Finalizado" }}
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    book: Object,
  },
};
</script>

<style scoped>
.container {
  background-color: #e9dffc;
  width: 185px;
  padding: 1rem;
  border-radius: 5px;
  min-height: 22.75rem;
  position: relative;
}

.bookName {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  max-width: 150px;
  font-size: 15px;
}

a {
  color: #000;
}

img {
  width: 155px;
  height: 222px;
}

.status {
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.information {
  display: flex;
  flex-direction: column;
  margin: 1rem;
  text-align: center;
}
.btn-outline {
  border: 3px solid #432876;
  color: #432876;
  font-weight: bolder;
  width: 8rem;
}
.button {
  display: flex;
  flex-direction: column;
  position: absolute;
  bottom: 1rem;
  right: 15%;
  flex-wrap: nowrap;
  justify-content: center;
  align-items: center;
}
</style>
