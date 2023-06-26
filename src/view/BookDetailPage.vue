<template>
  <main class="main-detail">
    <section v-if="showCongrats" class="congrats-message">
      <div class="d-flex">
        <h1 style="color: #29154d; margin-right: 6px">Doação solicitada!</h1>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="50"
          height="50"
          fill="currentColor"
          class="bi bi-check-circle"
          viewBox="0 0 16 16"
        >
          <path
            d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"
          />
          <path
            d="M10.97 4.97a.235.235 0 0 0-.02.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05z"
          />
        </svg>
      </div>

      <div class="text-congrats-message">
        Oba! Sua doação já foi solicitada. O doador foi avisado e logo logo
        entrará em contato! Se preferir, acesse o perfil do doador e entre em
        contato.
      </div>
    </section>

    <section v-if="showCongratsSell" class="congrats-message">
      <div class="d-flex">
        <h1 style="color: #29154d; margin-right: 6px">
          Produto adicionado no carrinho!
        </h1>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="50"
          height="50"
          fill="currentColor"
          class="bi bi-check-circle"
          viewBox="0 0 16 16"
        >
          <path
            d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"
          />
          <path
            d="M10.97 4.97a.235.235 0 0 0-.02.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05z"
          />
        </svg>
      </div>
    </section>

    <div class="content">
      <div>
        <img
          :src="book.image_url"
          :alt="'capa do livro ' + book.title"
          class="cover"
          tabindex="0"
        />
      </div>
      <div class="details">
        <h3 class="title" tabindex="0">{{ book.title }}</h3>

        <span class="category" tabindex="0">{{ categoryName }}</span>

        <div class="description" tabindex="0">
          <span>{{ book.description }} </span>
        </div>

        <div class="purchase-inf">
          <div v-if="book.price == 0">
            <p v-if="book.available == true" tabindex="0">
              Este produto está disponível para doação!
            </p>
            <a
              @click="requestDonation()"
              v-if="signedIn()"
              class="button btn donate"
              tabindex="0"
              >Solicitar doação</a
            >
            <a
              v-if="!signedIn()"
              @click="redirect()"
              tabindex="0"
              class="button btn donate"
              >Solicitar doação</a
            >
          </div>
          <div v-else>
            <p class="price" tabindex="0">
              R$
              {{ new Intl.NumberFormat("pt-BR").format(book.price) }}
            </p>
            <a
              class="button add btn"
              tabindex="0"
              @click="requestSelling()"
              v-if="showCongratsSell == false && signedIn()"
              >Adicionar ao carrinho</a
            >
            <a
              class="button add btn"
              v-if="!signedIn()"
              @click="redirect()"
              tabindex="0"
              >Adicionar ao carrinho</a
            >
          </div>

          <span class="soldby" tabindex="0">
            {{ book.price == 0 ? "Doado por:" : "Vendido por:" }}</span
          >

          <div class="info-user">
            <span tabindex="0">{{ userOwner.name }}</span>
            <star-rating
              v-bind:increment="0.5"
              v-bind:max-rating="5"
              inactive-color="#E9ECEF"
              v-bind:star-size="20"
              v-bind:show-rating="false"
              v-bind:rating="4.0"
              v-bind:read-only="true"
            />
          </div>
        </div>
      </div>
    </div>
  </main>
  <CarouselComp
    :description="'Outras opções parecidas'"
    class="carousel"
    :books="
      books.filter(
        (books) =>
          books?.category_id === this.book.category_id &&
          books?.type_book === 'sale'
      )
    "
  ></CarouselComp>
</template>

<script>
import StarRating from "vue-star-rating";
import CarouselComp from "@/components/carousel/CarouselComp.vue";
import api from "@/services/api";
import request from "@/services/request";
import { isSignedIn } from "@/services/auth";

export default {
  name: "BookDetailPage",
  components: {
    StarRating,
    CarouselComp,
  },
  props: {
    id: Number,
  },
  data() {
    return {
      showCongrats: false,
      showCongratsSell: false,

      categoryName: "",
      book: Object,
      userOwner: [],
      books: [],
    };
  },

  methods: {
    requestDonation() {
      request("post", `/donation-orders/${this.book.id}`, "");
      this.showCongrats = true;
    },
    requestSelling() {
      console.log("adicionou no carrinho");
      request("post", `/donation-orders/${this.book.id}`, "");
      this.showCongratsSell = true;
    },
    signedIn() {
      return isSignedIn();
    },
    redirect() {
      this.$router.push("/sign-up");
    },
  },

  mounted() {
    document.body.style.background =
      "linear-gradient(to bottom, #DECFFB, #FFFFFF) no-repeat";
    api
      .getBookById(this.id)
      .then((response) => {
        this.book = response.data;
        api.getUserById(this.book.user_id).then((resp) => {
          this.userOwner = resp.data;
        });
        api.getCategoryById(this.book.category_id).then((res) => {
          this.categoryName = res.data.name;
        });
      })
      .catch((error) => {
        console.error(error);
      });
    api.getBooks().then((response) => {
      this.books = response.data;
    });
  },
};
</script>

<style scoped>
body {
  background-color: #a87ff3 !important;
}

.text-congrats-message {
  margin-top: 2rem;
  max-width: 66%;
}

.congrats-message {
  margin-top: 3rem;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.main-detail {
  width: 70vw;
  margin: 0px auto;
  max-height: 100vh;
}
.info-user {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.content {
  display: grid;
  grid-template-columns: 1fr 2fr;
  justify-items: center;
  gap: 20px;
  width: 90%;
  margin: 40px auto 0px;
  text-align: center;
}

.details {
  display: grid;
  align-content: space-between;
  justify-items: center;
  align-content: center;
  gap: 50px;
}

.cover {
  max-width: 100%;
}

.title {
  font-size: 3.1rem;
  font-weight: bold;
  color: #29154d;
}

.category {
  color: #a87ff3;
  font-weight: bold;
}

.description {
  color: #432876;
  font-weight: bold;
}

.purchase-inf {
  display: grid;
}

.price {
  font-size: 4.25rem;
  color: #29154d;
}

.button {
  display: inline-block;
  background: #432876;
  color: #decffb;
  padding: 15px 30px;
  border-radius: 4px;
}

.soldby {
  color: #29154d7a;
  font-weight: bold;
}
</style>
