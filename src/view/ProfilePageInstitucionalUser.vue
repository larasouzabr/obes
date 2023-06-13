<template>
  <section class="container">
    <profileHeader :user="userInfo"></profileHeader>
    <available-books
      :type="'Livros requisitados'"
      :books="booksCollection"
      :isOnInstProf="true"
    ></available-books>
    <div class="button">
      <button @click="logout()" class="btn btn-red btn-lg">LOGOUT</button>
    </div>
  </section>
</template>

<script>
import api from "@/services/api";
import profileHeader from "@/components/profile/HeaderInfo.vue";
import AvailableBooks from "@/components/profile/AvailableBooks.vue";
import { request } from "@/services/request";
import { signOut } from "@/services/auth";

export default {
  name: "ProfilePage",
  components: {
    profileHeader,
    AvailableBooks,
  },
  data() {
    return {
      user: JSON.parse(localStorage.getItem("user")),
      userInfo: [],
      booksRequested: [],
      booksCollection: [],
    };
  },
  mounted() {
    document.body.style.background = "#F9F2FF";
    request("get", `/donation-orders`).then((resp) => {
      resp.forEach((book) => {
        this.booksCollection.push(book);
      });
    });

    api
      .getUserById(this.user.id)
      .then((response) => {
        this.userInfo = response.data;
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
