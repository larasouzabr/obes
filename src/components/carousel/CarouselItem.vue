<template>
  <div class="container">
    <router-link to="/books" href="#">
      <div class="image">
        <img :src="book.image" alt="" />
      </div>
      <div class="information">
        <span class="bookName"
          ><strong> {{ book.title }}</strong></span
        >
        <span class="bookAuthor">{{ book.author }}</span>
      </div>
      <div class="button">
        <span class="informationAboveButton" v-if="!isDonation"
          ><strong> A partir de:</strong></span
        >
        <button class="btn btn-outline" type="submit">
          <router-link to="/books">{{
            isDonation ? "Detalhes" : "R$ " + book.price
          }}</router-link>
        </button>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "CarouselItem",
  props: {
    book: Object,
    isDonation: Boolean,
  },
};
</script>

<style scoped>
.container {
  background-color: #e9dffc;
  width: 185px;
  padding: 1rem;
  border-radius: 5px;
  min-height: 26.75rem;
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
.information {
  display: flex;
  flex-direction: column;
  margin: 1rem;
}
.btn-outline {
  border: 3px solid #432876;
  color: #432876;
  font-weight: bolder;
  width: 8rem;
}
.bookAuthor {
  font-size: 10px;
  padding: 2px;
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
