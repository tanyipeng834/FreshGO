<template>
  <div class="container-fluid">
    <!-- Only show when status button is clicked -->
    <!-- End of hidden div & table -->

    <div class="row">
      <table class="table table-hover">
        <thead>
          <tr>
            <th scope="col">Crop Name</th>
            <th scope="col">Crop Quantity</th>
            <th scope="col">Recommend Water</th>
            <th scope="col">Recommended Fertiliser</th>
            <th scope="col">Estimated Height</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>{{ this.name }}</td>
            <td>{{ this.quantity }}</td>
            <td>{{ this.water * 10 }} litres</td>
            <td>{{ this.fertiliser }}kg</td>
            <td>{{ this.height }} cm</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Crop Recommendation",
  data() {
    return {
      name: "",
      fertiliser: "",
      water: "",
      estimatedHeight: 0,
    };
  },

  mounted() {
    this.name = localStorage.getItem("cropName");
    this.quantity = localStorage.getItem("cropQuantity");
    axios
      .get(`http://localhost:5007/recommend/${this.name}`)
      .then((response) => {
        console.log(response.data);
        this.fertiliser = response.data.fertiliser;
        this.water = response.data.water;
        this.height = response.data.height;
        this.height = this.height.toFixed(2);
      })
      .catch((error) => {
        console.log(error.message);
      });
  },
};
//
</script>
