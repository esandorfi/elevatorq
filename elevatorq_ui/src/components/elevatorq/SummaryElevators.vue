<template>
  <div class="d-flexp-3">
    <ul class="list-group list-group-flush">
      <li
        v-for="elevator in building_elevators"
        :key="elevator.name"
        class="list-group-item d-flex justify-content-start align-items-start"
      >
        <span class="badge bg-dark rounded-pill">{{ elevator.name }}</span>
        <div class="ms-5 me-auto">
          <span>waiting indicator : coming to lobby (in nnn seconds)</span><br />
          <span class="techmsg"
            >current_floor: {{ elevator.current_floor }} - current_direction :
            {{ elevator.current_direction }}</span
          >
        </div>
      </li>
    </ul>

    <div class="techmsg pt-3">
      buildinq api or mock json: <br />
      {{ building_elevators }}
    </div>
  </div>
</template>			
<script>
import { mapGetters } from "vuex";

// import building_json from "../../json/building.json";
// console.log(building_json);
export default {
  data() {
    return {
      hello: "people"
    };
  },
  computed: {
    ...mapGetters(["building_elevators", "building_elevators_network_error"])
    // building() {
    //   return building_json;
    // }
  },
  created() {
    this.$store.dispatch("getBuildingElevators");
  }
};
</script>
<style>
.techmsg {
  color: darkgray;
  font-size: 0.8rem;
}
.techsize {
  font-size: 0.8rem;
}
</style>