<template>
  <div class="main-content">
    <div class="background"></div>

    <header>
      <nav aria-label="primary">
        <ul>
          <li><a href="#">Sobre Nós</a></li>
          <li><a href="#">Contato</a></li>
          <li><a href="#">Entrar</a></li>
        </ul>
      </nav>
    </header>

    <main>
      <img src="../assets/obes.svg" alt="Logo Obes" />

      <p>
        <strong
          >Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sapiente
          alias velit ratione enim veniam ad aspernatur voluptate exercitationem
          obcaecati cumque perspiciatis nostrum minus libero.</strong
        >
      </p>

      <a href="/">Vamos lá!</a>
    </main>

    <footer>
      <a href="#"
        ><img src="../assets/icon-facebook.svg" alt="Ícone do Facebook"
      /></a>
      <a href="#"
        ><img src="../assets/icon-twitter.svg" alt="Ícone do Twitter"
      /></a>
      <a href="#"
        ><img src="../assets/icon-instagram.svg" alt="Ícone do Instagram"
      /></a>
    </footer>
  </div>
</template>

<script>
export default {
  name: "LoginPage",
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.main-content {
  font-family: "Poppins", sans-serif;
  margin: 0px;
  display: grid;
  gap: 30px;
  align-content: space-between;
  justify-content: space-between;
  grid-template-columns: 1fr 2fr;
  height: 100vh;
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

header {
  display: grid;
  justify-content: end;
  margin: 45px 65px 0px 0px;
  font-size: 1.25rem;
  font-weight: bold;
}

header nav ul {
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: 30px;
  padding: 0px;
  margin: 0px;
  align-items: center;
}

header a {
  color: #432876;
  transition: 0.5s;
}

header a:hover {
  color: #432876e3;
}

header ul li:last-child a {
  display: inline-block;
  background: #432876;
  color: #e9dffc;
  padding: 10px 20px;
  border-radius: 4px;
  transition: 0.5s;
}

header ul li:last-child a:hover {
  background: #432876e3;
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

footer {
  margin: 0px 65px 45px 0px;
  display: flex;
  gap: 20px;
  align-items: center;
  justify-content: end;
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
