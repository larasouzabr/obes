<template>
  <div class="register-title" v-if="!hasSeenCongrats">
    <h1>Antes, vamos confirmar algumas informações</h1>

    <div class="register-stepper">
      <div
        class="step"
        :class="{ 'step-active': step === 1, 'step-done': step > 1 }"
      >
        <span class="step-number-1"></span>
      </div>
      <div
        class="step"
        :class="{ 'step-active': step === 2, 'step-done': step > 2 }"
      >
        <span class="step-number-2"></span>
      </div>
    </div>
  </div>
  <section class="register" v-if="!hasSeenCongrats">
    <transition name="slide-fade">
      <section v-show="step === 1">
        <form class="forms" method="post" action="#" @submit.prevent="next">
          <ul class="forms-personalData">
            <li>
              <label for="dateBirth">Data de Nascimento</label>
              <input
                type="date"
                name="dateBirth"
                id="dateBirth"
                v-model="personalData.personalInfo.dateBirth"
                required
              />
            </li>
            <li>
              <label for="cpf">CPF</label>
              <input
                type="text"
                name="cpf"
                id="cpf"
                placeholder="000.000.000-00"
                v-model="personalData.personalInfo.cpf"
                required
              />
            </li>
            <li>
              <label for="phone">Celular</label>
              <input
                type="text"
                name="phone"
                id="phone"
                placeholder="(00) 00000-0000"
                v-model="personalData.personalInfo.phoneNumber"
              />
            </li>
            <ul class="personalData-addressNumber">
              <li>
                <label for="cep">CEP</label>
                <input
                  type="text"
                  name="cep"
                  id="cep"
                  placeholder="00000-000"
                  v-model="personalData.address.cep"
                  required
                />
              </li>
              <li>
                <label for="number">Número</label>
                <input
                  type="number"
                  name="number"
                  id="number"
                  placeholder="00"
                  v-model="personalData.address.number"
                  required
                />
              </li>
            </ul>
            <li>
              <label for="addressName">Endereço</label>
              <input
                type="text"
                name="addressName"
                id="addressName"
                placeholder="
Insira sua rua/avenida"
                v-model="personalData.address.addressName"
                required
              />
            </li>
            <ul class="personalData-addressInfo">
              <li>
                <label for="complement">Complemento</label>
                <input
                  type="text"
                  name="complement"
                  id="complement"
                  v-model="personalData.address.complement"
                />
              </li>
              <li>
                <label for="neighborhood">Bairro</label>
                <input
                  type="text"
                  name="neighborhood"
                  id="neighborhood"
                  v-model="personalData.address.neighborhood"
                  required
                />
              </li>
              <li>
                <label for="city">Cidade</label>
                <input
                  type="text"
                  name="city"
                  id="city"
                  v-model="personalData.address.city"
                  required
                />
              </li>
              <li>
                <label for="state">Estado</label>
                <input
                  type="text"
                  name="state"
                  id="state"
                  v-model="personalData.address.state"
                  required
                />
              </li>
            </ul>
          </ul>
          <div class="col-12">
            <button class="btn btn-primary" type="submit">Próximo</button>
          </div>
        </form>
      </section>
    </transition>
    <transition name="slide-fade">
      <section v-show="step === 2">
        <form action="">
          <BankData
            @event="prev()"
            @continue="donationComplete"
            :isPreview="true"
          ></BankData>
        </form>
      </section>
    </transition>
  </section>
  <section class="congrats-seeling-donation" v-if="hasSeenCongrats">
    <div class="alert alert-success" role="alert">
      <span>Informações cadastradas com sucesso!</span>
      <router-link to="/" class="return-home">
        <span>Ir para a página inicial</span>
        <img src="../../assets/arrow-right.svg" alt="" />
      </router-link>
    </div>
  </section>
</template>

<script>
import BankData from "./BankData.vue";
export default {
  components: { BankData },
  props: {
    type: Object,
  },
  data: () => {
    return {
      steps: {},
      step: 1,
      book: {
        bookTitle: "",
        bookCategory: "",
        bookDescription: "",
        bookPicture: "",
        bookPrice: 0.0,
      },
      personalData: {
        personalInfo: {
          dateBirth: "",
          cpf: "",
          phoneNumber: "",
        },
        address: {
          cep: "",
          number: 0,
          addressName: "",
          complement: "",
          neighborhood: "",
          city: "",
          state: "",
        },
      },
      hasSeenCongrats: false,
      categories: [
        { id: 1, name: "Romance" },
        { id: 2, name: "Ficção científica" },
        { id: 3, name: "Mistério" },
        { id: 4, name: "Fantasia" },
        { id: 5, name: "História" },
        { id: 6, name: "Autoajuda" },
        { id: 7, name: "Biografia" },
        { id: 8, name: "Negócios" },
        { id: 9, name: "Psicologia" },
        { id: 10, name: "Política" },
      ],
    };
  },
  methods: {
    prev() {
      this.step--;
    },

    next() {
      this.step++;
    },

    donationComplete: function () {
      this.hasSeenCongrats = true;
    },
    handleImageChange(event) {
      const file = event.target.files[0];
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => {
        this.book.bookPicture = reader.result;
      };
    },
  },
};
</script>
<style scoped>
body {
  background-color: #decffb;
}

.bookPreview {
  border: 1px solid black;
}

.alert-success {
  display: flex;
  justify-content: space-between;
  margin: 1.8rem auto 0px;
  /* margin-left: 9.5rem; */
  max-width: 80%;
  text-transform: uppercase;
}

.return-home {
  cursor: pointer;
  color: #000;
  text-transform: capitalize;
}

.return.home img {
  fill: #000;
}

.register,
.information-about-congrats {
  display: block;
  max-width: 80%;
  margin: 2rem auto;
  padding: 2rem;
  background: #decffb;
  text-align: center;
}

.information-about-congrats {
  display: flex;
  flex-direction: column;
}

.main-text-congrat {
  font-size: 25px;
  margin: 3rem;
}

.product-details h3 {
  margin-top: 3.75rem;
  margin-bottom: 1.25rem;
}

.register-icon {
  display: flex;
  background: white;
  border-radius: 2rem;
  width: 50px;
  height: 50px;
  padding: 1rem;
  margin: -50px auto 20px;
}
.register-item {
  width: 100%;
}

.btn-primary {
  display: inline-block;
  background: #432876;
  color: #e9dffc;
  padding: 10px 20px;
  border-radius: 4px;
  transition: 0.5s;
  border: #432876;
}

.btn-primary:active {
  background-color: #e9dffc;
  color: #432876;
  border: #432876 1px solid;
}

.col-12 {
  display: flex;
  align-items: flex-start;
  flex-direction: row;
  text-align: center;
  justify-content: center;
}

.register-title {
  font-weight: 300;
  font-size: 1.5rem;
  letter-spacing: 0.2rem;
  text-align: center;
  color: #000;
  padding: 0 2rem;
  margin-top: 2rem;
}

.register-stepper {
  display: flex;
  justify-content: space-evenly;
  width: 100%;
  position: relative;
  margin: 1.5rem auto 1.5em;
}
.register::before {
  position: relative;
  z-index: 0;
  content: "";
  display: block;
  height: 2px;
  background: #decffb;
  width: calc(43% - 85px);
  left: 32%;
  bottom: 90px;
}

.form-check-label {
  font-weight: normal;
}
.step {
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2;
  background-color: white;
  border-radius: 50%;
  min-width: 45px;
  min-height: 45px;
  line-height: 20px;
  font-size: 16px;
}

.step-active {
  background-color: #432876;
  border-color: #ffffff;
}

.step-done {
  background-color: #432876;
}

.forms ul {
  list-style: none;
  padding: 0px;
  margin: 0px;
  width: 500px;
  margin: 0 auto;
}

.forms label {
  padding: 0px;
  margin-bottom: 8px;
  margin-right: 8px;
}

.forms input {
  padding: 5px 10px;
  background: #ffffff;
  border: 1px solid #ced4da;
  border-radius: 4px;
  margin-bottom: 22px;
  width: 100%;
}

.forms {
  width: 100%;
}

.forms-personalData {
  display: grid;
  justify-content: center;
}

.forms-personalData li {
  display: grid;
}

.personalData-addressNumber {
  display: flex;
  justify-content: space-between;
  gap: 22px;
}

.personalData-addressNumber li {
  display: flex;
}

.personalData-addressInfo {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 22px;
}

.form {
  display: flex;
  flex-flow: row;
  justify-content: space-between;
  align-items: baseline;
  flex-wrap: wrap;
}

label {
  text-align: left;
  font-size: 1.1rem;
  line-height: 1.1;
  padding-bottom: 0.5rem;
  color: #000;
  font-size: medium;
  font-weight: 600;
}

.input-price {
  border: 0px;
}

.form.cta-step {
  color: black;
  justify-content: space-between;
}
.slide-fade-enter-active {
  transition: all 0.3s ease;
}
.slide-fade-leave-active {
  display: none;
  transition: all 0.4s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-fade-enter,
.slide-fade-leave-to {
  transform: translateX(10px);
  opacity: 0;
}
</style>
