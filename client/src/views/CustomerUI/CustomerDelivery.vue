<template>
  <div class="container-fluid">
    <div class="alert alert-success" role="alert" v-if="this.completed">
      Delivery Order Completed! We are redirecting you to the home screen!
    </div>
    <div class="row justify-content-center">
      <ul class="list-group">
        <li class="list-group-item">
          Delivery Staff Name :{{ this.staffName }}
        </li>
        <li class="list-group-item">
          Delivery Staff Phone:{{ this.staffPhone }}
        </li>
      </ul>

      <Map />
      <button type="button" class="btn btn-success" @click="redirectHome()">
        Order Completed
      </button>
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
      staffName: "",
      staffPhone: "",
      completed: false,
    };
  },
  mounted() {
    var staffDetails = localStorage.getItem("staffDetails");
    staffDetails = JSON.parse(staffDetails);
    console.log(staffDetails.name);
    this.staffName = staffDetails["name"];
    this.staffPhone = staffDetails["phone"];
  },
  methods: {
    redirectHome() {
      const customerId = this.$route.params.id;
      this.completed = true;
      this.$router.push(`/customer/${customerId}/`);
    },
  },
};
</script>

<style></style>
