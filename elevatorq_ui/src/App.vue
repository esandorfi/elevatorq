<template>
  <div>
    <nav-bar></nav-bar>
    <system-on-off></system-on-off>
    <div class="hero">
      <img alt="logo" src="./assets/elevator-svgrepo-com.svg" width="200" />
      <h1>Elevator Q</h1>
      <h4>Waiting to use ? Get a journey outside first.</h4>
      <p>Of course, you have the architecture ready to read, if you like now.</p>
      <p>
        _v1.0 : launch<br />
        _v1.1 : add summary, fetch api buildingq, error alerts and mock result
      </p>
    </div>
    <div class="container-fluid mt-5 p-5 bg-light bg-gradient">
      <div class="row">
        <div class="col">(q)</div>
        <div class="col">
          <h3>Marriott Marquis Lobby</h3>
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
