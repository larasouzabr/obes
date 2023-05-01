<template>
  <div class="main">
    <div class="imgBook">
      <img
        :src="book.bookPicture"
        alt=""
        :style="{
          width: '430px',
          height: '640px',
        }"
      />
    </div>
    <div class="information">
      <span>Título</span>
      <div>{{ book.bookTitle }}</div>
      <span>Categoria</span>
      <div>{{ book.bookCategory.name }}</div>
      <span>Descrição</span>
      <div class="description">{{ book.bookDescription }}</div>
      <div class="price" v-if="book.bookPrice != 0">
        <span>Valor</span>
        <p>R$ {{ book.bookPrice }}</p>
      </div>
      <div class="user-information">
        <span
          >{{ book.bookPrice === 0.0 ? "Doador(a)" : "Vendedor(a)" }}:
          <label>Roberta Rafaella </label>
        </span>
        <span>Contato: <label>9999999999</label> </span>
        <span>Cidade: <label>Quixadá - CE</label> </span>
      </div>
      <div class="col-12" v-if="isPreview">
        <button class="btn btn-outline-primary" @click.prevent="$emit('event')">
          Voltar
        </button>
        <button
          class="btn btn-primary"
          type="submit"
          @click.prevent="$emit('continue')"
        >
          Colocar em doação
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import user from "../../../public/fake-data/profile.json";

export default {
  name: "previewBook",
  props: {
    book: Object,
    isPreview: { type: Boolean },
  },
  data: () => {
    return user;
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

.main {
  /* display: flex;
  flex-direction: row; */
  display: grid;
  grid-template-columns: 1fr 1fr;
  justify-content: space-between;
  gap: 20px;
  padding: 32px;
}

.information {
  /* max-width: 60%;
  margin: 0 0 4rem 4rem;
  display: flex;
  flex-direction: column; */
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

label {
  font-weight: normal;
}

.description {
  font-size: large;
  max-width: 650px;
  text-align: justify;
}
span {
  font-weight: 700;
}
</style>
