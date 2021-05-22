<template>
  <div>
    <nav class="navbar navbar-light bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">
          Elevator Q <small class="techmsg">v1.1</small></a
        >
        <div class="d-flex">
          <a href="/admin" class="btn btn-dark me-2">admin</a>
          <div class="dropdown me-2">
            <button
              class="btn btn-outline-dark dropdown-toggle"
              type="button"
              id="dropdownMenuButton1"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              api
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
              <li><a class="dropdown-item" href="/api/building/">api building</a></li>
              <li><a class="dropdown-item" href="/api/elevatorq/">api elevatorq</a></li>
              <li><a class="dropdown-item" href="/api/pressbtnq/">api pressbtnq</a></li>
            </ul>
          </div>
          <a
            href="https://gitlab.com/esandorfi/elevatorq/-/tree/master/docs/iter3"
            class="btn btn-outline-dark"
            >readme</a
          >
        </div>
      </div>
    </nav>
    <div class="d-flex justify-content-end me-3">
      <small class="techmsg">user: admin / pwd: admin</small>
    </div>
  </div>
</template>