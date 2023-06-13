<template>
  <BannerMain></BannerMain>
  <div class="categories">
    <CarouselComp
      :books="books.filter((book) => book.type_book === 'sale')"
      :description="'Novidades em Vendas'"
    ></CarouselComp>
    <CarouselComp
      :books="
        books.filter(
          (book) => book.category_id === 18 && book.type_book === 'sale'
        )
      "
      :description="'Novidades em Vendas de ficção'"
    ></CarouselComp>
    <CarouselComp
      v-if="user.user_type == 'institutional'"
      :description="'Novidades em Doações'"
      :books="
        books.filter(
          (book) => book.type_book === 'donation' && book.available == true
        )
      "
    ></CarouselComp>
  </div>
</template>

<script>
import BannerMain from "@/components/BannerMain.vue";
import CarouselComp from "@/components/carousel/CarouselComp.vue";
import api from "@/services/api";

export default {
  name: "HomePage",
  components: { BannerMain, CarouselComp },
  mounted() {
    document.body.style.background = "#5E3A9E";
    api
      .getBooks()
      .then((response) => {
        this.books = response.data;
      })
      .catch((error) => {
        console.error(error);
      });
  },
  data() {
    return {
      books: [],
      user: JSON.parse(localStorage.getItem("user")),
    };
  },
};
</script>

<style scoped>
.categories {
  margin: 3rem;
  background-color: #ffffff;
  border-radius: 16px;
}
</style>
