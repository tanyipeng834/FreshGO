<template>
  <table class="table table-hover">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Customer Name</th>
        <th scope="col">Customer Phone</th>
        <th scope="col">Delivery Location</th>
        <th scope="col">Delivery Reward</th>
        <th scope="col">Status</th>
      </tr>
    </thead>
    <tbody class="table-group-divider">
      <tr
        v-for="(deliveryRequest, index) in delivery"
        class="delivery-item"
        v-bind:key="deliveryRequest.id"
      >
        <th scope="row">{{ index + 1 }}</th>
        <td>{{ deliveryRequest.customerName }}</td>
        <td>{{ deliveryRequest.customerPhone }}</td>
        <td>{{ deliveryRequest.customerLocation }}</td>
        <td>${{ deliveryRequest.deliveryCharge }}</td>
        <td>
          <router-link v-bind:to="'/delivery/' + deliveryRequest.id">
            <button class="btn btn-success" @click="setDestination(deliveryRequest.customerLocation)">Accept</button>
          </router-link>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import axios from "axios";
export default {
  name: "DeliveryRequests",
  data() {
    return {
      delivery: [],
    };
  },
  methods:{
    setDestination(location){
      localStorage.setItem("destination",location);
    }

  },
  mounted() {
    axios
      .get("http://127.0.0.1:5005/delivery")
      .then((response) => {
        this.delivery = response.data.data.delivery;
        console.log(this.delivery);
      })
      .catch((error) => {
        console.log(error.message);
      });
  },
};
</script>

<style></style>
