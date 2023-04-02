<template>
  <div class="container-fluid">
    <!-- Only show when status button is clicked -->
    <!-- End of hidden div & table -->

    <div class="row">
      <table class="table table-hover">
        <thead>
          <tr>
            <th scope="col">Crop Name</th>
            <th scope="col">Crops Sold Last Month</th>
            <th scope="col">Current Amount Of Crops in Inventory</th>
            <th scope="col">Current Amount Of On-Growing Crops</th>
            <th scope="col">Recommended Amount of Crops to Grow</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>{{ this.name }}</td>
            <td>{{ this.purchase }}</td>
            <td>{{ this.inventory }}</td>
            <td>{{ this.onGrowing }}</td>
            <td>
              {{ this.totalCrop }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "DisplayInventory",
  data() {
    return {
      name: "",
      inventory: 0,
      purchase: 0,
      onGrowing: 0,
      totalCrop: 0,
    };
  },
  mounted() {
    this.name = localStorage.getItem("name");
    const query = `
  query {
    manager(name: "${this.name}"){
    code
    ongrowingCrops
    inventory
    purchaseActivity
    totalCrop


 
    }
  }
`;

    // Define your GraphQL API endpoint
    const url = "http://localhost:8000/api/v1/inventory_manager";

    // Make a POST request to the GraphQL API endpoint with the query as the body
    axios
      .post(url, { query })
      .then((response) => {
        // Handle the response from the GraphQL API endpoint

        const data = response.data.data.manager;

        this.inventory = data.inventory;
        this.purchase = data.purchaseActivity;
        this.onGrowing = data.ongrowingCrops;
        this.totalCrop = data.totalCrop;
      })
      .catch((error) => {
        // Handle any errors that occurred during the request
        console.error(error);
      });
  },

  // mounted() {
  //   this.name = localStorage.getItem("name");
  //   axios
  //     .post(`http://localhost:5010/manager`,
  //     {
  //       name:this.name

  //     })
  //     .then((response) => {
  //
  //     })
  //     .catch((error) => {
  //       console.log(error.message);
  //     });
  // },
};
//
</script>
