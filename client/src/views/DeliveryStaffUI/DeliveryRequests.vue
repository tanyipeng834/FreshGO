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
          <button
            class="btn btn-success"
            @click="
              setDestination(
                deliveryRequest.customerLocation,
                deliveryRequest.id
              )
            "
          >
            Accept
          </button>
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
  methods: {
    setDestination(location, id) {
      localStorage.setItem("destination", location);

      const staff = this.$route.params.staffId;
      axios
        .delete("http://127.0.0.1:5005/delivery/delete", {
          data: {
            staffId: staff,
            deliveryId: id,
          },
        })
        .then((response) => {
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error.message);
        });
      this.$router.push(`http://127.0.0.1:5005/delivery/${id}`);
    },
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
