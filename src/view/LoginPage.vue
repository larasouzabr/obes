<template>
  <div class="main-content">
    <div class="background"></div>

    <HeaderMain />

    <main>
      <img src="../assets/obes.svg" alt="Logo Obes" />

      <blockquote>
        <p>
          <q
            >Todo mundo é um leitor em potencial, alguns apenas não encontraram
            o seu livro preferido ainda.</q
          >
        </p>
        <cite>- Anderson Davidye</cite>
      </blockquote>

      <router-link to="/">Vamos lá!</router-link>
    </main>

    <FooterMain />
  </div>
</template>

<script>
import HeaderMain from "../components/HeaderMain.vue";
import FooterMain from "../components/FooterMain.vue";

export default {
  name: "LoginPage",
  props: {
    msg: String,
  },
  components: {
    HeaderMain,
    FooterMain,
  },
  mounted() {
    document.body.style.background =
      "linear-gradient(135deg, #be9ff6, #decffb) no-repeat";
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.main-content {
  display: grid;
  gap: 30px;
  align-content: space-between;
  justify-content: space-between;
  grid-template-columns: 1fr 2fr;
  height: 100vh;
  /* background-color: #decffb; */
}

p {
  margin: 0px;
}

a {
  text-decoration: none;
}

.background {
  grid-row: 1 / -4;
  background-image: url("../assets/background-main.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: bottom right;
  max-height: inherit;
}

main {
  margin: 0px 65px 0px 0px;
  display: grid;
  gap: 45px;
  justify-items: end;
  text-align: right;
}

main img {
  max-width: 85vw;
}

main p {
  font-size: 1.5rem;
  line-height: 150%;
}

main a {
  display: inline-block;
  background: #432876;
  color: #fff;
  font-size: 1.5rem;
  padding: 35px 95px;
  border-radius: 4px;
  font-weight: bold;
  margin: auto 0;
  transition: 0.5s;
}

main a:hover {
  background: #432876e3;
}

@media (max-width: 635px) {
  header,
  main,
  footer {
    justify-content: center;
  }

  main {
    justify-items: center;
    text-align: center;
  }
}
</style>
