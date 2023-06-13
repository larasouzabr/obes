<template>
  <div class="container">
    <router-link :to="`/book-detail/${book.id}`" href="#">
      <div class="image">
        <img :src="book.image_url" alt="" />
      </div>
      <div class="information">
        <span class="bookName"
          ><strong> {{ book.title }}</strong></span
        >
      </div>
      <div class="button" v-if="!isOnProfile">
        <span class="informationAboveButton" v-if="!isDonation"
          ><strong> A partir de:</strong></span
        >
        <button class="btn btn-outline" type="submit">
          <router-link :to="`/book-detail/${book.id}`">{{
            isDonation ? "Detalhes" : "R$ " + book.price
          }}</router-link>
        </button>
      </div>
      <div class="button" v-if="isOnProfile">
        <span
          class="informationAboveButton"
          v-if="book.type_book !== 'donation'"
          ><strong> R$ {{ book.price }}</strong></span
        >
        <button class="btn btn-outline" type="submit">Editar</button>
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
    isOnProfile: Boolean,
    isOnInstitutionalPage: Boolean,
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
