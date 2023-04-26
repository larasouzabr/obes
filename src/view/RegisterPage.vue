<template>
  <div class="main-content">
    <div class="background"></div>

    <div class="content">
      <div v-if="template == 'Register'">
        <HeaderMain />
      </div>

      <div v-if="template == 'Register'">
        <main>
          <img src="../assets/obes.svg" alt="Logo Obes" />

          <p><strong>Primeiramente, nos informe quem é você:</strong></p>

          <form action="" method="post">
            <label for="person">
              <input
                class="input-radio"
                type="radio"
                name="user-type"
                id="person"
                value="RegisterPerson"
                v-model="userType"
              />
              <div class="option">
                <img src="../assets/icon-person.svg" alt="Ícone de pessoa" />
                <span>Sou uma pessoa</span>
              </div>
            </label>
            <label for="institution">
              <input
                class="input-radio"
                type="radio"
                name="user-type"
                id="institution"
                value="RegisterInstitution"
                v-model="userType"
              />
              <div class="option">
                <img
                  src="../assets/icon-institution.svg"
                  alt="Ícone de instituição"
                />
                <span>Sou uma instituição</span>
              </div>
            </label>
          </form>

          <a href="#" class="button-next" @click="template = userType"
            >Próximo <img src="../assets/arrow-right.svg" alt=""
          /></a>
        </main>
      </div>
      <div v-else-if="template == 'RegisterPerson'">
        <RegisterPerson />
      </div>
      <div v-else>
        <RegisterInstitution />
      </div>
    </div>
  </div>
</template>

<script>
import HeaderMain from "../components/HeaderMain.vue";
import RegisterPerson from "../components/register/RegisterPerson.vue";
import RegisterInstitution from "../components/register/RegisterInstitution.vue";

export default {
  name: "RegisterPage",
  components: {
    HeaderMain,
    RegisterPerson,
    RegisterInstitution,
  },
  data() {
    return {
      userType: "",
      template: "Register",
    };
  },
};
</script>

<style scoped>
header {
  margin: 0px;
}

.main-content {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 30px;
  height: 100vh;
}

.background {
  background-image: url("../assets/background-main.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: bottom right;
  max-height: inherit;
}

.content {
  display: grid;
  gap: 30px;
  align-items: center;
  margin: 45px 65px 45px 0px;
}

p {
  margin: 0px;
}

main {
  display: grid;
  gap: 15px;
  justify-content: center;
  justify-items: center;
  align-items: center;
}

main img {
  max-width: 85vw;
}

main p {
  width: 100%;
  text-align: center;
  font-size: 1.3rem;
}

main form {
  width: 80%;
  display: grid;
  gap: 30px;
}

main label {
  position: relative;
  cursor: pointer;
  display: flex;
  font-weight: 600;
  align-items: center;
}

main .input-radio {
  position: absolute;
  appearance: none;
  cursor: pointer;
  width: 25px;
  height: 25px;
  border-radius: 50%;
  border: 2px solid #fff;
  left: -50px;
}

main .input-radio:checked {
  background: #432876;
}

main .option {
  width: 100%;
  border: 3px solid #43287633;
  border-radius: 4px;
  padding: 28px 0px 28px 28px;
  color: #432876;
}

main .option img {
  width: 50px;
}

main .button-next {
  background: #432876;
  color: #fff;
  padding: 30px 60px;
  border-radius: 4px;
  text-align: center;
  font-size: 1.8rem;
  transition: 0.5s;
}

main .button-next:hover {
  background: #432876e3;
}

@media (max-width: 636px) {
  header {
    justify-content: center;
  }
}
</style>
