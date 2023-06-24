<template>
  <div class="content">
    <div class="d-flex">
      <div class="picture">
        <img :src="review.profilePicture" alt="Foto de perfil do Usuário" />
      </div>
      <div class="rating">
        <star-rating
          v-bind:increment="0.5"
          v-bind:max-rating="5"
          inactive-color="#E9ECEF"
          v-bind:star-size="20"
          v-bind:show-rating="false"
          v-bind:rating="review.rating"
          v-bind:read-only="true"
        />
        <span class="review-date">{{ review.date }}</span>
      </div>
    </div>
    <div class="comment">
      <span class="book-name">{{ review.bookTitle }}</span>
      <span class="book-comment">{{ review.comment }}</span>
    </div>
  </div>
</template>

<script>
import StarRating from "vue-star-rating";

export default {
  name: "ratingReview",
  components: {
    StarRating,
  },
  props: {
    review: Object,
  },
};
</script>

<style scoped>
.content {
  background-color: #d3bff9;
  height: 80px;
  width: 90%;
  display: flex;
  justify-content: flex-start;
  margin-top: 10px;
}
.comment {
  margin-top: 9px;
  display: flex;
  flex-direction: column;
}
.book-comment {
  font-size: 12px;
}
.review-date,
.book-name {
  font-weight: 400;
  color: #635b5b;
  font-size: 10px;
}
.rating {
  margin: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.picture > img {
  width: 51px;
  height: 51px;
  margin: 10px;
}
</style>
