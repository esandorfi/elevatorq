<template>
  <div
    v-if="building_elevators_network_error != 'OK'"
    class="position-fixed top-0 end-0"
    style="z-index: 5"
  >
    <div class="alert alert-danger alert-dismissible fade show techsize" role="alert">
      <strong> building_elevators_network_error </strong><br />
      {{ building_elevators_network_error }}
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="alert"
        aria-label="Close"
      ></button>
    </div>
  </div>
</template>			
<script>
import { mapGetters } from "vuex";
export default {
  computed: {
    ...mapGetters(["building_elevators_network_error"])
  }
};
</script>
