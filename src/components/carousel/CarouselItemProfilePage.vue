<template>
  <div class="container">
    <div class="delete-button-modal-activate">
      <button
        type="button"
        class="btn btn-danger"
        data-bs-toggle="modal"
        :data-bs-target="'#deletebookmodal-' + book.id"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="currentColor"
          class="bi bi-trash"
          viewBox="0 0 16 16"
        >
          <path
            d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5Zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5Zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6Z"
          />
          <path
            d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1ZM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118ZM2.5 3h11V2h-11v1Z"
          />
        </svg>
      </button>
    </div>

    <div class="image">
      <button class="icon-reproduzir" :id="book.id" @click="playDescription()">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="currentColor"
          class="bi bi-volume-up-fill"
          viewBox="0 0 16 16"
        >
          <path
            d="M11.536 14.01A8.473 8.473 0 0 0 14.026 8a8.473 8.473 0 0 0-2.49-6.01l-.708.707A7.476 7.476 0 0 1 13.025 8c0 2.071-.84 3.946-2.197 5.303l.708.707z"
          />
          <path
            d="M10.121 12.596A6.48 6.48 0 0 0 12.025 8a6.48 6.48 0 0 0-1.904-4.596l-.707.707A5.483 5.483 0 0 1 11.025 8a5.483 5.483 0 0 1-1.61 3.89l.706.706z"
          />
          <path
            d="M8.707 11.182A4.486 4.486 0 0 0 10.025 8a4.486 4.486 0 0 0-1.318-3.182L8 5.525A3.489 3.489 0 0 1 9.025 8 3.49 3.49 0 0 1 8 10.475l.707.707zM6.717 3.55A.5.5 0 0 1 7 4v8a.5.5 0 0 1-.812.39L3.825 10.5H1.5A.5.5 0 0 1 1 10V6a.5.5 0 0 1 .5-.5h2.325l2.363-1.89a.5.5 0 0 1 .529-.06z"
          />
        </svg>
      </button>
      <img :src="book.image_url" :alt="'capa do livro ' + book.title" />
    </div>
    <div class="information">
      <span class="bookName"
        ><strong> {{ book.title }}</strong></span
      >
    </div>
    <div class="button" v-if="isOnProfile">
      <span class="informationAboveButton" v-if="book.type_book !== 'donation'"
        ><strong> R$ {{ book.price }}</strong></span
      >
      <button
        class="btn btn-outline"
        data-bs-toggle="modal"
        :data-bs-target="'#editbookmodal-' + book.id"
        @click="insertDataInBooks"
        type="submit"
      >
        Editar
      </button>
    </div>
  </div>

  <div
    class="modal fade"
    :id="'editbookmodal-' + book.id"
    tabindex="-1"
    aria-labelledby="modalEditBookInfo"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="modalEditBookInfo">Editar informações</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="form-group required">
            <label class="control-label">Título</label>
            <input
              type="text"
              class="form-control"
              required
              v-model="bookEdit.title"
            />
          </div>
          <div class="form-group required">
            <label class="control-label">Descrição</label>
            <textarea
              class="form-control"
              required
              maxlength="150"
              v-model="bookEdit.description"
            ></textarea>
          </div>
          <div
            class="form-group required"
            v-if="bookEdit.type_book !== 'donation'"
          >
            <label for="bookPrice" class="control-label">Valor</label>
            <div class="form-control">
              <span>R$ </span>
              <input
                class="input-price"
                type="number"
                step="0.01"
                v-model="bookEdit.price"
                id="bookPrice"
                placeholder="0,00"
              />
            </div>
          </div>
          <div class="form-group required">
            <label for="category" class="control-label"
              >Categoria do Livro</label
            >
            <select
              name="category"
              id="category"
              v-model="bookEdit.category_id"
              autocomplete="book.categoria.name"
              class="form-selected form-control"
              required
            >
              <option disabled selected>{{ categoryName }}</option>
              <option
                v-for="categoria in categories"
                :key="categoria"
                :value="categoria.id"
              >
                {{ categoria.name }}
              </option>
            </select>
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
            @click="editBookInfo()"
          >
            Editar
          </button>
        </div>
      </div>
    </div>
  </div>
  <div
    class="modal fade"
    :id="'deletebookmodal-' + book.id"
    tabindex="-1"
    aria-labelledby="modalDeleteBookInfo"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="modalEditBookInfo">Deletar Livro</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div>
            Você tem certeza que deseja deletar o livro
            <strong>{{ this.book.title }}</strong> ?
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
              class="btn btn-danger"
              data-bs-dismiss="modal"
              @click="deleteBook()"
            >
              Deletar
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import api from "@/services/api";
import { request } from "@/services/request";

export default {
  name: "CarouselItemProfilePage",
  props: {
    book: Object,
    isDonation: Boolean,
    isOnProfile: Boolean,
  },
  data: () => {
    return {
      bookEdit: {
        id: 0,
        title: "",
        category_id: 0,
        description: "",
        image: "",
        type_book: "",
        price: 0,
      },
      categories: [],
      categoryName: "",
    };
  },
  mounted() {
    this.getAllCategories();
  },

  methods: {
    editBookInfo() {
      request("put", `/books/${this.book.id}`, JSON.stringify(this.bookEdit));
      window.location.reload();
    },
    deleteBook() {
      request("delete", `/books/${this.book.id}`);
      window.location.reload();
    },
    getAllCategories() {
      api
        .getAllCategories()
        .then((response) => {
          this.categories = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    insertDataInBooks() {
      this.bookEdit.title = this.book.title;
      this.bookEdit.description = this.book.description;
      this.bookEdit.category_id = this.book.category_id;
      this.bookEdit.price = this.book.price;
      this.bookEdit.type_book = this.book.type_book;
      this.bookEdit.image = this.book.image;
      this.bookEdit.id = this.book.id;
      this.getCategoryById();
    },
    playDescription() {
      const desc = new SpeechSynthesisUtterance(this.book.title);
      window.speechSynthesis.speak(desc);
    },
    getCategoryById() {
      api.getCategoryById(this.book.category_id).then((res) => {
        this.categoryName = res.data.name;
      });
    },
  },
};
</script>

<style scoped>
.container {
  background-color: #e9dffc;
  width: 185px;
  padding: 1rem;
  border-radius: 5px;
  min-height: 26.75rem;
  position: relative;
  margin-top: inherit;
}

.delete-button-modal-activate {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 1rem;
}

.bookName {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  max-width: 150px;
  font-size: 15px;
}

a {
  color: #000;
}

.icon-reproduzir {
  position: absolute;
  top: 18px;
  left: 20px;
  color: #fff;
  background-color: #000;
  border-radius: 50%;
  padding: 3px;
}

img {
  width: 155px;
  height: 222px;
}
.information {
  display: flex;
  flex-direction: column;
  margin: 1rem;
  text-align: center;
}
.btn-outline {
  border: 3px solid #432876;
  color: #432876;
  font-weight: bolder;
  width: 8rem;
}
.button {
  display: flex;
  flex-direction: column;
  position: absolute;
  bottom: 1rem;
  right: 15%;
  flex-wrap: nowrap;
  justify-content: center;
  align-items: center;
}
</style>
