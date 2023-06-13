<template>
  <main>
    <img src="../../assets/obes.svg" alt="Logo Obes" />

    <form @submit.prevent="salvarUsuario" method="post">
      <label for="name">Nome da instituição</label>
      <input
        type="text"
        name="name"
        id="name"
        placeholder="Digite o nome da instituição"
        required
        v-model="user.name"
      />

      <label for="email">E-mail</label>
      <input
        type="email"
        name="email"
        id="email"
        placeholder="Digite um e-mail que representa a instituição"
        required
        v-model="user.email"
      />

      <span>Tipo de Instituição:</span>
      <div class="institution-type">
        <div>
          <input
            type="radio"
            name="institution-type"
            id="school"
            value="escola"
            v-model="user.institutional_type"
          />
          <label for="school">Escola</label>
        </div>
        <div>
          <input
            type="radio"
            name="institution-type"
            id="library"
            value="biblioteca"
            v-model="user.institutional_type"
          />
          <label for="bookstore">Biblioteca</label>
        </div>
        <div>
          <input
            type="radio"
            name="institution-type"
            id="other"
            value="outra"
            v-model="user.institutional_type"
          />
          <label for="other">Outra</label>
        </div>
      </div>

      <label for="password">Senha</label>
      <div class="col-auto">
        <span id="passwordHelpInline" class="form-text">
          Precisa ter entre 8-50 caracteres
        </span>
      </div>
      <input
        type="password"
        name="password"
        id="password"
        placeholder="Digite sua senha"
        minlength="8"
        v-model="user.password"
        required
      />

      <label for="password-confirm">Confirmação da senha</label>
      <input
        v-model="passwordConfirm"
        type="password"
        name="password-confirm"
        id="password-confirm"
        placeholder="Digite sua senha novamente"
        required
      />
      <div
        class="alert alert-primary"
        role="alert"
        v-if="!passwordsMatch && passwordConfirm !== ''"
      >
        {{ message }}
      </div>
      <div class="buttons">
        <router-link to="/login" class="button cancel">Cancelar</router-link>
        <button type="submit" :disabled="!passwordsMatch" class="button create">
          Criar conta
        </button>
      </div>
    </form>

    <div class="info">
      <p>
        Já possui cadastro?
        <span
          ><router-link to="/sign-up" class="sign"
            >Acesse sua conta</router-link
          ></span
        >.
      </p>
      <p>
        Ao seguir com o cadastro, você concorda com os
        <span>Termos de Uso</span> e <span>Política de Privacidade</span>
      </p>
    </div>
  </main>
</template>

<script>
import api from "@/services/api";
export default {
  name: "RegisterInstitution",
  data() {
    return {
      user: {
        name: "",
        email: "",
        password: "",
        user_type: "institutional",
        institutional_type: "",
      },
      passwordConfirm: "",
      message: "",
    };
  },
  computed: {
    passwordsMatch() {
      return this.user.password === this.passwordConfirm;
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
    salvarUsuario() {
      api.addNewUser(this.user).catch((e) => {
        this.errors = e.response.data.errors;
      });
      this.$router.push("/sign-up");
    },
  },
};
</script>

<style scoped>
main img {
  max-width: 80vw;
}

main form {
  width: 100%;
  display: grid;
}

main input {
  display: block;
  margin-bottom: 10px;
  width: 100%;
  height: 40px;
  border: 1px solid #432876;
  border-radius: 4px;
  padding: 10px;
}

.institution-type {
  display: flex;
  justify-content: space-between;
}

.institution-type div {
  display: flex;
  gap: 10px;
}

.institution-type input {
  margin: 0px;
  display: inline-block;
  appearance: none;
  cursor: pointer;
  width: 25px;
  height: 25px;
  border-radius: 50%;
  border: 2px solid #fff;
}

.institution-type input:checked {
  background: #432876;
}

.buttons {
  display: flex;
  gap: 20px;
  justify-content: space-between;
}

.button {
  padding: 10px 0px;
  border-radius: 4px;
  font-weight: bold;
  width: 100%;
  text-align: center;
}

.button.cancel {
  cursor: pointer;
  border: 2px solid #432876;
  color: #432876;
  transition: 0.5s;
}

.button.cancel:hover {
  border: 2px solid #432876e3;
  color: #432876e3;
}

.button.create {
  border: 0px;
  background: #432876;
  color: #e9dffc;
  transition: 0.5s;
}
.button.create:disabled {
  border: 0px;
  background: #ad87f3;
  color: #e9dffc;
  transition: 0.5s;
}

.button.create:disabled:hover {
  border: 0px;
  background: #ad87f3;
  color: #e9dffc;
  transition: 0.5s;
}

.button.create:hover {
  background: #432876e3;
}

.info {
  text-align: center;
}

.info span {
  color: #432876;
  font-weight: bold;
}

.info .sign {
  color: #432876;
  transform: 0.5s;
}

.info .sign:hover {
  color: #432876e3;
}

@media (max-width: 636px) {
  header {
    justify-content: center;
  }
}
</style>
