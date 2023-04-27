<template>
  <div class="main-content">
    <div class="background"></div>

    <main>
      <img src="../assets/obes.svg" alt="Logo Obes" />
      <form action="" method="post">
        <label for="email">E-mail</label>
        <input
          type="email"
          name="email"
          id="email"
          placeholder="Digite seu e-mail"
          required
        />
        <label for="password">Senha</label>
        <input type="password" name="password" id="password" required />

        <div class="buttons">
          <router-link to="/login" class="button cancel">Cancelar</router-link>
          <button type="submit" class="button enter">Entrar</button>
        </div>
      </form>

      <p>
        Não tem cadastro?
        <router-link to="/register" class="register"
          >Crie uma conta</router-link
        >
      </p>
    </main>
  </div>
</template>

<script>
export default {
  name: "SignUpPage",
};
</script>

<style scoped>
.main-content {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 30px;
  height: 100vh;
}

.background {
  background-image: url("../assets/background-main.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: bottom right;
  max-height: inherit;
}

main {
  display: grid;
  gap: 40px;
  place-content: center;
  justify-items: center;
  margin-right: 60px;
}

main img {
  max-width: 85vw;
}

form {
  width: 100%;
  font-size: 1rem;
}

input {
  display: block;
  margin-bottom: 30px;
  width: 100%;
  height: 40px;
  border: 1px solid #432876;
  border-radius: 4px;
}

.buttons {
  display: flex;
  gap: 20px;
  justify-content: space-between;
}

.button {
  padding: 10px 0px;
  border-radius: 4px;
  font-weight: bold;
  width: 100%;
  text-align: center;
}

.button.cancel {
  cursor: pointer;
  border: 2px solid #432876;
  color: #432876;
  transition: 0.5s;
}

.button.cancel:hover {
  border: 2px solid #432876e3;
  color: #432876e3;
}

.button.enter {
  border: 0px;
  background: #432876;
  color: #e9dffc;
  transition: 0.5s;
}

.button.enter:hover {
  background: #432876e3;
}

.register {
  color: #432876;
  transition: 0.5s;
}

.register:hover {
  color: #432876e3;
}
</style>
