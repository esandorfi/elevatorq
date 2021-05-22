<template>
  <div
    v-if="building_elevators_network_error != 'OK'"
    class="position-fixed bottom-0 end-0"
    style="z-index: 5"
  >
    <div class="alert alert-dark alert-dismissible fade show techmsg" role="alert">
      <strong> building_elevators_network_error </strong>
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
