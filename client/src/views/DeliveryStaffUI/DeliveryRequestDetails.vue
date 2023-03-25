<template>
  <div class="container-fluid">
    <div class="row justify-content-center">
      <Map />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Map from "../../components/DeliveryUI/map.vue";
export default {
  name: "DeliveryRequestDetails",
  components: {
    Map,
  },
  data() {
    return {
      factoryLocation: "102 Henderson Road",
    };
  },
};
</script>

<style></style>
