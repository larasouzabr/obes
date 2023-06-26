<template>
  <nav class="navbar navbar-expand-lg" v-if="!isPaginaLogin">
    <div class="container-fluid">
      <router-link to="/" class="navbar-brand">
        <img src="../assets/obes.svg" alt="OBES Logo" width="123" height="39" />
      </router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <div>
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link
                to="/"
                class="nav-link active fs-5"
                aria-current="page"
                >Início</router-link
              >
            </li>
            <li class="nav-item dropdown">
              <a
                class="nav-link fs-5"
                href="#"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                Categorias
              </a>
              <ul class="dropdown-menu">
                <li v-for="categoria in categories" :key="categoria">
                  <a class="dropdown-item + {{ category.id }}" href="#">
                    {{ categoria.name }}
                  </a>
                </li>
              </ul>
            </li>
          </ul>
        </div>
        <form class="d-flex" role="search">
          <input
            class="form-control me-2"
            type="search"
            placeholder="O que você está procurando?"
            aria-label="O que você está procurando?"
          />
          <button class="btn btn-outline" type="submit">Pesquisar</button>
        </form>
        <div class="user-info">
          <ul
            class="navbar-nav user-information-ul me-auto mb-2 mb-lg-0 d-flex d-row"
          >
            <router-link to="/profile" v-if="signedIn()">
              <img
                src="../assets/avatar.png"
                alt="Avatar usuário"
                width="32"
                height="32"
                style="border-radius: 50%"
              />
              <span> Olá, {{ firstName }}! </span>
            </router-link>
            <router-link to="/sign-up" v-if="!signedIn()">
              <img
                src="../assets/avatar.png"
                alt="Avatar usuário"
                width="45"
                height="32"
              />
              <span> Olá, usuário! </span>
            </router-link>
          </ul>
        </div>
      </div>
    </div>
  </nav>
</template>
<script>
import { isSignedIn } from "@/services/auth";
import api from "@/services/api";

export default {
  computed: {
    isPaginaLogin() {
      return (
        this.$route.path === "/login" ||
        this.$route.path === "/register" ||
        this.$route.path === "/sign-up"
      );
    },
    firstName() {
      const hasSpace = this.userName.indexOf(" ") >= 0;
      if (hasSpace) {
        return this.userName.substring(0, this.user.name.indexOf(" "));
      } else {
        return this.userName;
      }
    },
  },
  data() {
    return {
      categories: [],
      user: JSON.parse(localStorage.getItem("user")),

      userName: "",
    };
  },
  mounted() {
    api
      .getAllCategories()
      .then((response) => {
        this.categories = response.data;
      })
      .catch((error) => {
        console.error(error);
      });
    if (this.user) {
      api.getUserById(this.user?.id).then((response) => {
        this.userName = response.data.name;
      });
    }
  },

  methods: {
    signedIn() {
      return isSignedIn();
    },
  },
};
</script>

<style scoped>
form {
  justify-content: center;
}
.form-control {
  width: 60vh;
}
.navbar {
  background-color: #decffb;
}

span {
  color: #432876;
}

.dropdown-menu > li :hover {
  background-color: #724fb2;
  color: #decffb;
}
.navbar-collapse {
  justify-content: space-between;
}
.user-information-ul {
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
}

li > img {
  height: 32px;
}
.btn-outline {
  border: 1px solid #432876;
  color: #432876;
}

.user-info {
  color: #432876;
}

.nav-item .nav-link {
  color: #432876;
}
.nav-item:active {
  color: #432876;
}
</style>
