<template>
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
</template>

<script>
export default {
  name: "FooterMain",
};
</script>

<style scoped>
footer {
  margin: 0px 65px 45px 0px;
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  align-items: center;
  justify-content: end;
}
</style>
