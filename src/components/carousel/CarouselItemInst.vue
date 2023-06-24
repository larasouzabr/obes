<template>
  <div class="container">
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
      <img :src="book.book.image_url" :alt="'capa do livro ' + book.title" />
    </div>
    <div class="information">
      <span class="bookName"
        ><strong> {{ book.book.title }}</strong></span
      >
    </div>
    <div class="status">
      <button class="btn-outline" type="submit">
        {{ book.status == "PENDING" ? "Solicitado" : "Finalizado" }}
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    book: Object,
  },
  methods: {
    playDescription() {
      const desc = new SpeechSynthesisUtterance(this.book.title);
      window.speechSynthesis.speak(desc);
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
  min-height: 22.75rem;
  position: relative;
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

img {
  width: 155px;
  height: 222px;
}

.status {
  display: flex;
  flex-direction: row;
  justify-content: center;
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
