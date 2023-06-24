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
            <span class="profile-city-and-state" v-if="user.address?.id">
              <img
                src="../../assets/geo-alt.svg"
                alt="Localização do usuário"
              />
              <label class="city"
                >{{ user.address?.city }} - {{ user.address?.state }}</label
              >
            </span>
            <a
              class="btn btn-sm btn-primary edit-button"
              data-bs-toggle="modal"
              data-bs-target="#confirmationModal"
              @click="insertDataInUser"
            >
              <img src="../../assets/pencil-square.svg"
            /></a>
          </div>
          <div class="about-me-and-rating">
            <span class="rating">
              <img
                src="../../assets/star-fill.svg"
                alt="Avaliação geral do usuário"
              />
              <span class="actual-rating"> 4.5 </span>
            </span>
            <span style="color: #495057"> Sobre mim: </span>
            <br />
            <span style="color: #29154d"> {{ user.about_me }} </span>
            <span style="color: #6766ff" v-if="!user.about_me">
              Edite suas informações para adicionar uma breve resumo aqui.
            </span>
          </div>
        </div>
      </div>
      <div class="buttons" v-if="user.user_type == 'common'">
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
          <div class="form-group required">
            <label class="control-label">Nome</label>
            <input
              type="text"
              class="form-control"
              required
              v-model="userEdit.name"
            />
          </div>
          <div class="form-group required">
            <label class="control-label">Email</label>
            <input
              type="email"
              class="form-control"
              required
              v-model="userEdit.email"
            />
          </div>
          <div class="form-group required">
            <label class="control-label">Sobre mim</label>
            <textarea
              class="form-control"
              required
              maxlength="150"
              v-model="userEdit.about_me"
            ></textarea>
            <div class="wordCount">
              <p>{{ characterCount }} / 150</p>
            </div>
          </div>
          <div class="form-group required">
            <label class="control-label">Número de celular</label>
            <input
              type="text"
              class="form-control"
              required
              v-model="userEdit.phone_number"
            />
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
import { signOut } from "@/services/auth";
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
        about_me: "",
      },
      address: {
        city: "",
        state: "",
      },
    };
  },
  computed: {
    characterCount() {
      return this.userEdit.about_me?.length;
    },
  },
  methods: {
    editUserInfo() {
      const changeCriticalInfo =
        this.userEdit.name !== this.user.name ||
        this.userEdit.email !== this.user.email;
      request("put", "/user", JSON.stringify(this.userEdit));
      changeCriticalInfo
        ? this.$router.push("/sign-up") && signOut()
        : window.location.reload();
    },
    insertDataInUser() {
      this.userEdit.name = this.user.name;
      this.userEdit.email = this.user.email;
      this.userEdit.phone_number = this.user.phone_number;
      this.userEdit.about_me = this.user.about_me;
    },
  },
};
</script>

<style lang="css" scoped>
.profile-city-and-state {
  display: flex;
  align-items: center;
  flex-direction: row;
  white-space: nowrap;
}

.profile-city-and-state img {
  margin: 5px;
}

.img > img {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  background-size: cover;
  background-position: center;
}
.wordCount {
  display: flex;
  justify-content: flex-end;
  font-size: 10px;
}
.form-group.required .control-label:after {
  content: "*";
  color: red;
}

.edit-button {
  margin-left: 7px;
  display: flex;
  height: fit-content;
  align-self: center;
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
  margin-right: 5px;
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
  align-items: flex-center;
}
.header-main {
  margin-top: 4rem;
  margin-bottom: 4rem;
}

.modal-footer .btn-primary {
  background: #432876;
  --bs-btn-border-color: #432876;
  --bs-btn-hover-border-color: #432876;
}
</style>
