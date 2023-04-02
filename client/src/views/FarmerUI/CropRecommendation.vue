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
            <td>{{ this.water * 10 }} ml</td>
            <td>{{ this.fertiliser }}g</td>
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
      .post(`http://localhost:8000/api/v1/recommend`, {
        cropName: this.name,
      })
      .then((response) => {
        console.log(response.data);
        if (response.data.fertiliser < 0) {
          this.fertiliser = response.data.fertiliser * -1;
        } else {
          this.fertiliser = response.data.fertiliser;
        }
        this.fertiliser = this.fertiliser.toFixed(2);
        if (response.data.water < 0) {
          this.water = response.data.water * -1;
        } else {
          this.water = response.data.water;
        }
        if (response.data.height < 0) {
          this.height = response.data.height * -1;
        } else {
          this.height = response.data.height;
        }

        this.height = this.height.toFixed(2);
      })
      .catch((error) => {
        console.log(error.message);
      });
  },
};
//
</script>
