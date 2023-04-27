<template>
  <section class="header-main">
    <header class="header">
      <div class="pic-and-info">
        <span :style="containerStyle"></span>
        <div class="information-together">
          <div class="information-main">
            <span class="profile-name">Lara LINDA</span>
            <span class="profile-city-and-state">
              <img
                src="../../assets/geo-alt.svg"
                alt="Localização do usuário"
              />
              <label class="city">Quixada - CE</label>
            </span>
          </div>
          <div class="about-me-and-rating">
            <span class="rating">
              <img
                src="../../assets/star-fill.svg"
                alt="Avaliação geral do usuário"
              />
              <span class="actual-rating">4.9</span>
            </span>
            <span style="color: #a0a0a0"> Sobre mim: </span>
            <br />
            <span style="color: #29154d">
              Apaixonada por livros de romance e aventura!!! Escritora
              entusiasta.
            </span>
          </div>
        </div>
      </div>
      <div class="buttons">
        <button type="button" class="btn btn-purple btn-lg">Quero doar</button>
        <button type="button" class="btn btn-purple btn-lg">
          Quero vender
        </button>
      </div>
    </header>
  </section>
</template>

<script>
export default {
  name: "profileHeader",
  props: {
    imageUrl: {
      type: String,
      required: true,
    },
  },
  computed: {
    containerStyle() {
      return {
        width: "120px",
        height: "120px",
        MaxWidth: "150px",
        MaxHeight: "150px",
        borderRadius: "50%",
        backgroundImage: `url(${this.imageUrl})`,
        backgroundSize: "cover",
        backgroundPosition: "center",
      };
    },
  },
};
</script>

<style lang="css" scoped>
.profile-city-and-state {
  display: flex;
  flex-direction: row;
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
  margin-left: 5px;
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
  align-items: flex-start;
}
.header-main {
  margin-top: 4rem;
  margin-bottom: 4rem;
}
</style>
