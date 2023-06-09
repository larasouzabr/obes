<template>
  <div class="main">
    <div class="imgBook">
      <img
        :src="book.image"
        alt=""
        :style="{
          width: '430px',
          height: '640px',
        }"
      />
    </div>
    <div class="information">
      <span>Título</span>
      <div>{{ book.title }}</div>
      <span>Categoria</span>
      <div class="category">{{ categoryName }}</div>
      <span>Descrição</span>
      <div class="description">{{ book.description }}</div>
      <div class="price" v-if="book.price != 0">
        <span>Valor</span>
        <p>R$ {{ book.price }}</p>
      </div>
      <div class="user-information">
        <span
          >{{ book.price === 0.0 ? "Doador(a)" : "Vendedor(a)" }}:
          <label>{{ sellerUser.name }} </label>
        </span>
        <span
          >Contato: <label>{{ sellerUser.phone_number }}</label>
        </span>
        <span
          >Cidade:
          <label
            >{{ sellerUser.address?.city }} -
            {{ sellerUser.address?.state }}</label
          >
        </span>
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
          {{ book.price == 0 ? "Colocar em doação" : "Colocar à venda" }}
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import api from "@/services/api";
export default {
  name: "previewBook",
  props: {
    book: Object,
    isPreview: { type: Boolean },
  },
  data() {
    return {
      user: JSON.parse(localStorage.getItem("user")),
      sellerUser: [],
      categoryName: "",
    };
  },
  watch: {
    "book.category_id": {
      immediate: true,
      handler(newVal) {
        this.getCategoryName(newVal);
      },
    },
  },
  mounted() {
    api
      .getUserById(this.user.id)
      .then((response) => {
        this.sellerUser = response.data;
      })
      .catch((error) => {
        console.error(error);
      });
  },

  methods: {
    getCategoryName(id) {
      if (id !== 0) {
        api
          .getCategoryById(id)
          .then((response) => {
            this.categoryName = response.data.name;
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },
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
