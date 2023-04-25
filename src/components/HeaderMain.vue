<template>
  <header>
    <nav aria-label="primary">
      <ul>
        <li><a href="#">Sobre Nós</a></li>
        <li><a href="#">Contato</a></li>
        <li><router-link to="/sign-up" class="enter">Entrar</router-link></li>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {
  name: "MenuMain",
};
</script>

<style scoped>
header {
  display: grid;
  justify-content: end;
  margin: 45px 65px 0px 0px;
  font-size: 1.25rem;
  font-weight: bold;
}

nav ul {
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: 30px;
  padding: 0px;
  margin: 0px;
  align-items: center;
}

li a {
  color: #432876;
}

.enter {
  display: inline-block;
  background: #432876;
  color: #e9dffc;
  padding: 10px 20px;
  border-radius: 4px;
  transition: 0.5s;
}

.enter:hover {
  background: #432876e3;
}
</style>
