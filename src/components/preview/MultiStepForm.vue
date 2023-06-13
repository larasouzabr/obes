<template>
  <div class="register-title" v-if="!hasSeenCongrats">
    <h1>
      {{
        step === 1
          ? type[0].isSelling
            ? "Vender um Livro"
            : "Doar um Livro"
          : "Preview"
      }}
    </h1>

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
        <form
          class="form"
          method="post"
          action="#"
          @submit.prevent="next"
          enctype="multipart/form-data"
        >
          <div class="col-md-8">
            <label for="bookName" class="form-label">Título do livro</label>
            <input
              class="form-control"
              id="bookName"
              type="text"
              v-model="book.title"
              autocomplete="book.title"
              placeholder="Digite o título do livro"
              required
            />
          </div>
          <div class="col-md-4">
            <label for="category" class="form-label">Categoria do Livro</label>
            <select
              name="category"
              id="category"
              v-model="book.category_id"
              autocomplete="book.categoria.name"
              class="form-selected form-control"
              required
            >
              <option disabled selected>Selecione uma categoria</option>
              <option
                v-for="categoria in categories"
                :key="categoria"
                :value="categoria.id"
              >
                {{ categoria.name }}
              </option>
            </select>
          </div>
          <div class="mb-3 mt-3 col-12">
            <div class="mb-3 mt-3" style="width: inherit">
              <label for="description" class="form-label">Descrição</label>
              <textarea
                class="form-control"
                id="description"
                rows="6"
                v-model="book.description"
                autocomplete="book.description"
                placeholder="Adicione informações relevantes como: 
- Autor: 
- Editora:
- Ano:
- Número de páginas:"
                minlength="20"
                required
              ></textarea>
            </div>
          </div>

          <div class="form-group col-12">
            <div class="mb-3">
              <label for="image" class="form-label"
                >Envie uma foto da capa do livro</label
              >
              <input
                class="form-control"
                type="file"
                ref="fileInput"
                accept="image/*"
                @change="handleFileChange"
              />
            </div>
          </div>

          <div class="col-12" v-if="type[0].isSelling">
            <div class="mb-3">
              <label for="bookPrice" class="form-label">Valor</label>
              <div class="form-control">
                <span>R$ </span>
                <input
                  class="input-price"
                  type="number"
                  step="0.01"
                  v-model="book.price"
                  id="bookPrice"
                  placeholder="0,00"
                />
              </div>
            </div>
          </div>

          <div class="col-12 mt-5">
            <div class="form-check">
              <input
                class="form-check-input"
                type="checkbox"
                value=""
                id="invalidCheck"
                required
              />
              <label class="form-check-label" for="invalidCheck">
                Li e concordo com os <strong>Termos de Doação</strong>
              </label>
              <div class="invalid-feedback">
                você precisa concordar antes de enviar
              </div>
            </div>
          </div>
          <div class="col-12">
            <button class="btn btn-primary" type="submit">Próximo</button>
          </div>
        </form>
      </section>
    </transition>
    <transition name="slide-fade">
      <section v-show="step === 2">
        <form action="">
          <preview-book
            :book="book"
            @event="prev()"
            @continue="donationComplete"
            :isPreview="true"
          ></preview-book>
        </form>
      </section>
    </transition>
  </section>
  <section class="congrats-seeling-donation" v-if="hasSeenCongrats">
    <div class="alert alert-success" role="alert">
      <span>Obrigado por {{ type[0].typeofAction }} no OBES!</span>
      <router-link to="/" class="return-home">
        <span>Ir para a página inicial</span>
        <img src="../../assets/arrow-right.svg" alt="" />
      </router-link>
    </div>
    <div class="information-about-congrats">
      <span class="main-text-congrat"
        ><strong>{{ type[0].congratTextMain }}</strong></span
      >
      <span>{{ type[0].congratTextUnder }}</span>

      <div class="product-details">
        <h3><strong>Detalhes do Pedido</strong></h3>
        <div class="bookPreview">
          <preview-book
            :book="book"
            @event="prev()"
            :isPreview="false"
          ></preview-book>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import PreviewBook from "./PreviewBook.vue";
import api from "@/services/api";
import { requestFormData } from "@/services/request";

export default {
  components: { PreviewBook },
  props: {
    type: Object,
  },
  data: () => {
    return {
      steps: {},
      step: 1,
      book: {
        title: "",
        category_id: 0,
        description: "",
        image: "",
        type_book: "",
        price: 0,
      },
      hasSeenCongrats: false,
      categories: [],
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
      this.postInfo();
    },
    async postInfo() {
      const file = this.$refs.fileInput.files[0];
      const formData = new FormData();
      formData.append("image", file);
      formData.append("title", this.book.title);
      formData.append("category_id", this.book.category_id);
      formData.append("description", this.book.description);
      formData.append("price", this.book.price);

      if (this.book.price == 0) {
        this.book.type_book = "donation";
      } else {
        this.book.type_book = "sale";
      }

      formData.append("type_book", this.book.type_book);
      console.log(JSON.stringify(formData));
      requestFormData("/books", formData);
    },
    handleFileChange(event) {
      const file = event.target.files[0];
      this.book.image = URL.createObjectURL(file);
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
  text-transform: uppercase;
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
