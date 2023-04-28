<template>
  <section class="header-main">
    <header>
      <div class="pic-and-info">
        <div :style="containerStyle"></div>
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
          <div>
            <span class="rating">
                <img
                src="../../assets/star-fill.svg"
                alt="Avaliação geral do usuário"
              />
                <span class="actual-rating">4.9</span>
            </span>
          </div>
        </div>
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
        width: "160px",
        height: "160px",
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

.elipse {
  background-color: #45597e;
  height: fit-content;
  width: fit-content;
  border-radius: 50%;
}

.profile-city-and-state {
  display: flex;
  flex-direction: row;
}


.profile-name {
  font-size: 36px;
  font-weight: 700;
  line-height: 54px;
  letter-spacing: 0em;
  text-align: left;
  margin-right: 2rem;
}

.information-together{
    margin-left: 3rem;
}

.city, .actual-rating {
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
  width: 126vh;
  display: flex;
  flex-direction: row;
  align-content: center;
  flex-wrap: nowrap;
  align-items: flex-start;
}
.header-main {
  margin: 4rem;
}
</style>
