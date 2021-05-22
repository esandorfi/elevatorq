<template>
  <div>
    <nav-bar></nav-bar>

    <div class="hero">
      <img alt="logo" src="./assets/elevator-svgrepo-com.svg" width="250" />
      <h1>Elevator Q</h1>

      <h4>Waiting to use ? Get a journey outside first.</h4>
      <p>Of course, you have the architecture ready to read, if you like now.</p>
      <p>
        <strong>Saturday alert !</strong> Preparing monday coding, we got one step further
        in the elevator product.
      </p>
    </div>

    <div class="container-fluid mt-5 p-5 bg-dark text-light bg-gradient">
      <h3 align="center" class="mb-3">Welcome to Marriott Marquis downtown Lobby</h3>
      <system-on-off></system-on-off>
    </div>
    <div class="container-fluid px-5 pb-5 bg-dark text-light">
      <div class="row">
        <div class="col-12 col-md-6 bg-dark">
          <h4 class="mb-5 text-center">Queues</h4>

          <div class="form-group">
            <label for="pressbtnqFormControlTextarea">(pressbtnq)</label>
            <textarea
              class="form-control"
              id="pressbtnqFormControlTextarea1"
              rows="10"
            ></textarea>
          </div>
          <div class="form-group mt-3">
            <label for="elevatorqFormControlTextarea">(elevatorq)</label>
            <textarea
              class="form-control"
              id="elevatorqFormControlTextarea1"
              rows="10"
            ></textarea>
          </div>
        </div>

        <div class="col-12 col-md-6">
          <h4 class="mb-5 text-center">Building elevators</h4>
          <p>You are at the Lobby - floor 0</p>
          <summary-elevators></summary-elevators>
        </div>
      </div>
    </div>

    <alerts></alerts>
  </div>
</template>

<script setup>
import NavBar from "./components/NavBar.vue";
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
