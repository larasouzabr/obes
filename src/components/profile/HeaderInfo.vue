<template>
  <section class="header-main">
    <header class="header">
      <div class="pic-and-info">
        <span class="img">
          <img
            :src="
              user.image_filename
                ? user.image_filename
                : require('@/assets/avatar.png')
            "
            alt=""
          />
        </span>
        <div class="information-together">
          <div class="information-main">
            <span class="profile-name">{{ user.name }}</span>
            <span class="profile-city-and-state">
              <img
                src="../../assets/geo-alt.svg"
                alt="Localização do usuário"
              />
              <label class="city"
                >{{ user.address?.city }} - {{ user.address?.state }}</label
              >
              <a
                class="btn btn-sm btn-danger"
                data-bs-toggle="modal"
                data-bs-target="#confirmationModal"
              >
                <img src="../../assets/pencil-square.svg" class="edit-button"
              /></a>
            </span>
          </div>
          <div class="about-me-and-rating">
            <span class="rating">
              <img
                src="../../assets/star-fill.svg"
                alt="Avaliação geral do usuário"
              />
              <span class="actual-rating"> 4.5 </span>
            </span>
            <span style="color: #a0a0a0"> Sobre mim: </span>
            <br />
            <span style="color: #29154d"> {{ user.about_me }} </span>
          </div>
        </div>
      </div>
      <div class="buttons">
        <router-link class="btn btn-purple btn-lg" to="/profile/donateabook"
          >Quero doar</router-link
        >
        <router-link
          type="button"
          class="btn btn-purple btn-lg"
          to="/profile/sellabook"
        >
          Quero vender
        </router-link>
      </div>
    </header>
  </section>

  <div
    class="modal fade"
    id="confirmationModal"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Editar informações</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="form-group">
            <label>Nome</label>
            <input
              type="text"
              class="form-control"
              required
              v-model="userEdit.name"
            />
          </div>
          <div class="form-group">
            <label>Email</label>
            <input
              type="email"
              class="form-control"
              required
              v-model="userEdit.email"
            />
          </div>
          <div class="form-group">
            <label>Sobre mim:</label>
            <textarea class="form-control" required maxlength="150"></textarea>
          </div>
          <div class="form-group">
            <label>Número</label>
            <input
              type="text"
              class="form-control"
              required
              v-model="userEdit.phone_number"
            />
          </div>
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label>Cidade</label>
                <input
                  type="text"
                  class="form-control"
                  required
                  v-model="address.city"
                />
              </div>
            </div>
            <div class="col-md-4 ms-auto">
              <div class="form-group">
                <label>Estado</label>
                <input
                  type="text"
                  class="form-control"
                  required
                  v-model="address.state"
                />
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
          >
            Cancelar
          </button>
          <button
            type="button"
            class="btn btn-primary"
            data-bs-dismiss="modal"
            @click="editUserInfo()"
          >
            Editar
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { request } from "@/services/request";
export default {
  name: "profileHeader",
  props: {
    user: Object,
  },
  data() {
    return {
      userEdit: {
        name: "",
        email: "",
        phone_number: "",
      },
      address: {
        city: "",
        state: "",
      },
    };
  },
  computed: {
    passwordsMatch() {
      return this.user.password === this.userEdit.password;
    },
  },
  watch: {
    passwordConfirm(newVal) {
      if (!this.passwordsMatch && newVal !== "") {
        this.message = "As senhas não correspondem";
      } else {
        this.message = "";
      }
    },
  },
  methods: {
    editUserInfo() {
      request("put", "/user", this.userEdit);
      if (this.user.address == null) {
        request("post", "/addresses", this.address);
      } else {
        request("put", `/address/${this.user.address.id}`, this.address);
      }
    },
  },
};
</script>

<style lang="css" scoped>
.profile-city-and-state {
  display: flex;
  flex-direction: row;
  white-space: nowrap;
}

.img > img {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  background-size: cover;
  background-position: center;
}

.edit-button {
  margin-left: 7px;
}

.rating {
  display: flex;
}

.header {
  display: flex;
  justify-content: space-between;
}

.profile-name {
  font-size: 36px;
  font-weight: 700;
  line-height: 54px;
  letter-spacing: 0em;
  text-align: left;
  margin-right: 2rem;
  white-space: nowrap;
}

.buttons {
  display: flex;
  flex-direction: column;
}

.btn-purple {
  background-color: #432876;
  color: #ffff;
  margin: 5px;
  padding: 14px;
  white-space: nowrap;
}

.information-together {
  margin-left: 3rem;
}

.city,
.actual-rating {
  font-family: "Roboto", sans-serif;
  font-size: 25px;
  font-weight: 600;
  line-height: 50px;
  letter-spacing: 0em;
  text-align: left;
  margin-left: 5px;
}

.pic-and-info {
  display: flex;
  flex-direction: row;
}
.information-main {
  width: 90%;
  display: flex;
  flex-direction: row;
  align-content: center;
  flex-wrap: nowrap;
  align-items: flex-start;
}
.header-main {
  margin-top: 4rem;
  margin-bottom: 4rem;
}
</style>
