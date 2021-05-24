<template>
  <div>
    <nav-bar></nav-bar>
    <hero class="d-none"></hero>

    <div class="container-fluid p-5 bg-dark text-light text-center">
      <h1 align="center" class="mb-3">Welcome to NYC Marriott Marquis</h1>
      <img
        alt="logo"
        src="./assets/elevator-svgrepo-com.svg"
        fill="fff"
        width="200"
        style="background-color: #fff; padding: 3px; border-radius: 50%"
      />

      <h2>Elevator Q</h2>

      <system-on-off></system-on-off>
    </div>
    <div class="container-fluid px-5 pb-5 bg-dark text-light">
      <div class="row">
        <div class="col-12 col-md-8 p-5">
          <h4 class="mb-5 text-center">Welcome to the Lobby - floor 0</h4>
          <div class="techmsg">(buildingelevators summary)</div>
          <summary-elevators></summary-elevators>
        </div>

        <div class="col-12 col-md-4">
          <div class="form-group">
            <label for="pressbtnqFormControlTextarea" class="techmsg">(pressbtnq)</label>
            <textarea
              class="form-control bg-light"
              id="pressbtnqFormControlTextarea1"
              rows="10"
            ></textarea>
          </div>
          <div class="form-group mt-3">
            <label for="elevatorqFormControlTextarea" class="techmsg">(elevatorq)</label>
            <textarea
              class="form-control bg-light"
              id="elevatorqFormControlTextarea1"
              rows="10"
            ></textarea>
          </div>
        </div>
      </div>
    </div>

    <alerts></alerts>
  </div>
</template>

<script setup>
import NavBar from "./components/NavBar.vue";
import Hero from "./components/Hero.vue";
import SystemOnOff from "./components/elevatorq/SystemOnOff.vue";
import Alerts from "./components/elevatorq/Alerts.vue";
import SummaryElevators from "./components/elevatorq/SummaryElevators.vue";
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.hero {
  text-align: center;
  color: #2c3e50;
  margin-top: 20px;
}
</style>
