<template>
  <table class="table table-hover">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Order ID</th>
        <th scope="col">Customer ID</th>
        <th scope="col">Delivery Address</th>
        <th scope="col">More Details</th>
        <th scope="col">Status</th>
      </tr>
    </thead>
    <tbody class="table-group-divider">
      <tr
        v-for="deliveryRequest in deliveryRequests"
        class="delivery-item"
        v-bind:key="deliveryRequest.orderId"
      >
        <th scope="row">count</th>
        <td>{{ deliveryRequest.orderId }}</td>
        <td>{{ deliveryRequest.customerId }}</td>
        <td>{{ deliveryRequest.deliveryLocation }}</td>
        <td>
          <router-link v-bind:to="'/delivery/' + deliveryRequest.orderId">
            <button class="btn btn-success">View Details</button>
          </router-link>
        </td>
        <td>
          <button class="btn btn-outline-success">Accept</button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  name: "DeliveryRequests",
  data() {
    return {
      deliveryRequests,
    };
  },
};
</script>

<style></style>
