<template>
  <main>
    <img src="../../assets/obes.svg" alt="Logo Obes" />

    <form action="" method="post">
      <label for="name">Nome Completo</label>
      <input
        type="text"
        name="name"
        id="name"
        placeholder="Digite seu nome completo"
        required
      />

      <label for="email">E-mail</label>
      <input
        type="email"
        name="email"
        id="email"
        placeholder="Digite seu e-mail"
        required
      />

      <label for="password">Senha</label>
      <input
        type="password"
        name="password"
        id="password"
        placeholder="Digite sua senha"
        required
      />

      <label for="password-confirm">Confirmação da senha</label>
      <input
        type="password"
        name="password-confirm"
        id="password-confirm"
        placeholder="Digite sua senha novamente"
        required
      />

      <div class="buttons">
        <router-link to="/login" class="button cancel">Cancelar</router-link>
        <button type="submit" class="button create">Criar conta</button>
      </div>
    </form>

    <div class="info">
      <p>
        Já possui cadastro?
        <span
          ><router-link to="/sign-up" class="sign"
            >Acesse sua conta</router-link
          ></span
        >.
      </p>
      <p>
        Ao seguir com o cadastro, você concorda com os
        <span>Termos de Uso</span> e <span>Política de Privacidade</span>
      </p>
    </div>
  </main>
</template>

<script>
export default {
  name: "RegisterPerson",
};
</script>

<style scoped>
main img {
  max-width: 85vw;
}

main form {
  width: 100%;
  display: grid;
}

main input {
  display: block;
  margin-bottom: 10px;
  width: 100%;
  height: 40px;
  border: 1px solid #432876;
  border-radius: 4px;
  padding: 10px;
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

.button.create {
  border: 0px;
  background: #432876;
  color: #e9dffc;
  transition: 0.5s;
}

.button.create:hover {
  background: #432876e3;
}

.info {
  text-align: center;
}

.info span {
  color: #432876;
  font-weight: bold;
}

.info .sign {
  color: #432876;
  transform: 0.5s;
}

.info .sign:hover {
  color: #432876e3;
}

@media (max-width: 636px) {
  header {
    justify-content: center;
  }
}
</style>
