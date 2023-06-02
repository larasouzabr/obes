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
          <router-link to="/books">{{
            isDonation ? "Detalhes" : "R$ " + book.price
          }}</router-link>
        </button>
      </div>
      <div class="button" v-if="isOnProfile">
        <span class="informationAboveButton" v-if="!book.isDonation"
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
  },
};
</script>
