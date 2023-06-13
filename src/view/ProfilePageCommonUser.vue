<template>
  <section class="container">
    <profileHeader :user="userInfo"></profileHeader>
    <overall-info :user="profile"></overall-info>
    <available-books
      :description="'Seus livros a venda'"
      :type="'sell'"
      :books="booksByUser.filter((book) => book.type_book === 'sale')"
    ></available-books>
    <available-books
      :description="'Seus livros na doação'"
      :type="'donation'"
      :books="booksByUser.filter((book) => book.type_book === 'donation')"
    ></available-books>
    <div class="button">
      <button @click="logout()" class="btn btn-red btn-lg">LOGOUT</button>
    </div>
  </section>
</template>

<script>
import api from "@/services/api";
import profile from "../../public/fake-data/profile.json";
import profileHeader from "@/components/profile/HeaderInfo.vue";
import OverallInfo from "@/components/profile/OverallInfo.vue";
import AvailableBooks from "@/components/profile/AvailableBooks.vue";
import { signOut } from "@/services/auth";

export default {
  name: "ProfilePage",
  components: {
    profileHeader,
    OverallInfo,
    AvailableBooks,
  },
  data() {
    return {
      user: JSON.parse(localStorage.getItem("user")),
      userInfo: [],
      profile,
      booksByUser: [],
    };
  },
  mounted() {
    document.body.style.background = "#F9F2FF";
    api
      .getUserById(this.user.id)
      .then((response) => {
        this.userInfo = response.data;
        api.getBooksDonatedOrSellingByUser(this.userInfo.id).then((resp) => {
          this.booksByUser = resp.data;
        });
      })
      .catch((error) => {
        console.error(error);
      });
  },
  methods: {
    logout() {
      signOut();
      this.$router.push("/login");
    },
  },
};
</script>

<style lang="css" scoped>
body {
  background-color: #f9f2ff;
}
.button {
  display: flex;
  justify-content: center;
  margin: 3rem;
}
.btn-red {
  background-color: #c10c0c;
  color: #ffff;
  margin: 5px;
  padding: 14px;
  white-space: nowrap;
}
.btn-red:hover {
  background-color: #f85050;
  color: #ffff;
  margin: 5px;
  padding: 14px;
  white-space: nowrap;
}
</style>
