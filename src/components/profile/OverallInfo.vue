<template>
  <section>
    <div class="stats">
      <span class="item-stat">
        <span class="title-stat"> Livros Comprados </span>
        <span class="val-stat"> {{ user.stats[0].boughtBooks }} </span>
      </span>

      <span class="item-stat">
        <span class="title-stat"> Livros Vendidos </span>
        <span class="val-stat"> {{ user.stats[0].soldBooks }} </span>
      </span>
      <span class="item-stat">
        <span class="title-stat"> Livros Doados </span>
        <span class="val-stat"> {{ user.stats[0].donatedBooks }} </span>
      </span>
    </div>
    <div class="recent-ratings">
      <div class="content-recent-ratings">
        <span class="text-main-ratings">Principais avaliações</span>
        <rating-review
          v-for="review in user.reviews"
          :key="review"
          :review="review"
        ></rating-review>
      </div>
    </div>
  </section>
</template>

<script>
import RatingReview from "./RatingReview.vue";
export default {
  name: "bannerOverall",
  components: { RatingReview },
  props: {
    user: Object,
  },
};
</script>

<style scoped>
section {
  background-color: #432876;
  height: 500px;
  display: flex;
  flex-direction: row;
  justify-content: first baseline;
  margin-bottom: 3rem;
}

.text-main-ratings {
  width: 472px;
  height: 49px;
  font-family: "Arial Rounded MT Bold";
  font-style: normal;
  font-weight: 400;
  font-size: 33px;
  line-height: 150%;
  text-align: center;
  color: #ffffff;
}
.content-recent-ratings {
  display: flex;
  margin: 3rem;
  height: 70%;
  background-color: #5e3a9e;
  flex-direction: column;
  align-items: center;
}
.recent-ratings {
  width: 55%;
}
.stats {
  width: 45%;
  margin-top: 3rem;
  display: flex;
  flex-direction: column;
}
.title-stat {
  background-color: #d3bff9;
  color: #432876;
  border-radius: 4px;
  width: 350.26px;
  height: 38px;
  font-family: "Arial Rounded MT Bold";
  font-style: normal;
  font-weight: 400;
  font-size: 25px;
  line-height: 150%;
  text-align: center;
}
.val-stat {
  font-family: "Noto Sans Arabic";
  font-style: normal;
  font-weight: 900;
  font-size: 60px;
  line-height: 150%;
  text-align: center;
  color: #ffffff;
  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.item-stat {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
