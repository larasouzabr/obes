<template>
  <section class="header-main">
    <header class="header">
      <div class="pic-and-info">
        <span class="img">
          <img :src="user.image" alt="" />
        </span>
        <div class="information-together">
          <div class="information-main">
            <span class="profile-name">{{ user.name }}</span>
            <span class="profile-city-and-state">
              <img
                src="../../assets/geo-alt.svg"
                alt="Localização do usuário"
              />
              <label class="city">{{ user.city }} - {{ user.state }}</label>
            </span>
          </div>
          <div class="about-me-and-rating">
            <span class="rating">
              <img
                src="../../assets/star-fill.svg"
                alt="Avaliação geral do usuário"
              />
              <span class="actual-rating">{{ user.rating }}</span>
            </span>
            <span style="color: #a0a0a0"> Sobre mim: </span>
            <br />
            <span style="color: #29154d">
              {{ user.about }}
            </span>
          </div>
        </div>
      </div>
      <div class="buttons">
        <router-link class="btn btn-purple btn-lg" to="/profile/donateabook"
          >Quero doar</router-link
        >
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
    user: Object,
  },
};
</script>

<style lang="css" scoped>
.profile-city-and-state {
  display: flex;
  flex-direction: row;
  white-space: nowrap;
}

.img > img {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  background-size: cover;
  background-position: center;
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
  white-space: nowrap;
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
