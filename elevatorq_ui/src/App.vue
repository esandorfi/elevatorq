<template>
<div>
	<NavBar></NavBar>
	<system-on-off></system-on-off>
	<div class="hero">
		<img alt="logo" src="./assets/elevator-svgrepo-com.svg" width="300" />
		<h1>Elevator Q</h1>
		<h4>Waiting to use ? Get a journey outside first.</h4>
		<p>Of course, you have the architecture ready to read, if you like now.</p>
	</div>  


  </div>
</template>

<script setup>
import HelloWorld from './components/HelloWorld.vue'
import NavBar from './components/NavBar.vue'
import SystemOnOff from './components/elevatorq/SystemOnOff.vue'

// This starter template is using Vue 3 experimental <script setup> SFCs
// Check out https://github.com/vuejs/rfcs/blob/script-setup-2/active-rfcs/0000-script-setup.md
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.hero {   text-align: center;
  color: #2c3e50;
  margin-top: 20px;
 }
</style>
