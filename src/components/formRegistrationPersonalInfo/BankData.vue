<template>
  <div class="main">
    <form class="forms" action="#" method="post">
      <ul>
        <li>
          <label for="cardNumber">Número do Cartão</label>
          <input
            type="text"
            name="cardNumber"
            id="cardNumber"
            placeholder="0000-0000-0000-0000"
            v-model="bankData.cardNumber"
            required
          />
        </li>
        <ul class="forms-flex">
          <li>
            <label for="securityCode">Código de Segurança</label>
            <input
              type="text"
              maxlength="3"
              name="securityCode"
              id="securityCode"
              placeholder="***"
              v-model="bankData.securityCode"
              required
            />
          </li>
          <li>
            <label for="validityDate">Data de Validade</label>
            <input
              type="date"
              name="validityDate"
              id="validityDate"
              v-model="bankData.validityDate"
              required
            />
          </li>
        </ul>
        <li>
          <label for="holderName">Nome do Titular</label>
          <input
            type="text"
            name="holderName"
            id="holderName"
            v-model="bankData.holderName"
            required
          />
        </li>
      </ul>

      <div class="information">
        <div class="col-12" v-if="isPreview">
          <button
            class="btn btn-outline-primary"
            @click.prevent="$emit('event')"
          >
            Voltar
          </button>
          <button
            class="btn btn-primary"
            type="submit"
            @click.prevent="$emit('continue')"
          >
            Salvar dados
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import user from "../../../public/fake-data/profile.json";

export default {
  name: "bankData",
  props: {
    isPreview: { type: Boolean },
  },
  data: () => {
    return {
      user,
      bankData: {
        cardNumber: "",
        securityCode: "",
        validityDate: "",
        holderName: "",
      },
    };
  },
};
</script>

<style scoped>
.btn-primary {
  display: inline-block;
  background: #432876;
  color: #e9dffc;
  padding: 10px 20px;
  border-radius: 4px;
  transition: 0.5s;
  border: #432876;
  white-space: nowrap;
}

.btn-outline-primary {
  display: inline-block;
  color: #432876;
  padding: 10px 20px;
  border-radius: 4px;
  transition: 0.5s;
  border: #432876 2px solid;
  white-space: nowrap;
  margin: 10px;
}

.btn-outline-primary:hover,
.btn-primary:hover {
  background-color: #6a41b6;
  display: inline-block;
  color: #e9dffc;
  padding: 10px 20px;
  border-radius: 4px;
  transition: 0.5s;
  border: #532e98 2px solid;
  white-space: nowrap;
}

.btn-primary:active {
  background-color: #e9dffc;
  color: #432876;
  border: #432876 1px solid;
}

.information {
  display: grid;
  align-content: space-between;
  text-align: center;
  font-size: 1.5rem;
}

.user-information {
  margin: 3rem;
  display: flex;
  flex-direction: column;
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
  text-align: left;
  width: 100%;
}

.forms-flex {
  display: flex;
  gap: 22px;
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

span {
  font-weight: 700;
}
</style>
