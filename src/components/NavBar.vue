<template>
  <nav class="navbar navbar-expand-lg">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">
        <img src="../assets/obes.svg" alt="OBES Logo" width="123" height="39" />
      </a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <div>
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active fs-5" aria-current="page" href="#"
                >Início</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link fs-5" href="#">Categorias</a>
            </li>
          </ul>
        </div>
        <form class="d-flex" role="search">
          <input
            class="form-control me-2"
            type="search"
            placeholder="O que você está procurando?"
            aria-label="O que você está procurando?"
          />
          <button class="btn btn-outline" type="submit">Pesquisar</button>
        </form>
        <div class="user-info">
          <ul class="navbar-nav user-information-ul me-auto mb-2 mb-lg-0 d-flex d-row">
            <img
              src="../assets/avatar.png"
              alt="Avatar"
              width="45"
              height="32"
            />
            <li>
              <a class="nav-link active" aria-current="page" href="#"
                >Olá, usuário!</a
              >
            </li>
          </ul>
        </div>
      </div>
    </div>
  </nav>
</template>

<style scoped>
form {
  justify-content: center;
}
.form-control {
  width: 50vh;
}
.navbar {
  background-color: #decffb;
}

.user-information-ul{
    display: flex;
    flex-wrap: nowrap;
    align-items: center;
}

li > img {
  height: 32px;
}
.btn-outline {
  border: 1px solid #432876;
  color: #432876;
}

.colapse {
  justify-content: space-between;
}

.user-info {
  color: #432876;
}

.nav-item {
  color: #724fb2;
}
.nav-item:active {
  color: #432876;
}
</style>
