<template>
  <div class="container-fluid home">
    <div class="row home">
      <div class="collapse" id="navbarToggleExternalContent">
        <div class="bg-light shadow-3 p-4">
          <button class="btn btn-link btn-block border-bottom m-0">
            Link 1
          </button>
          <button class="btn btn-link btn-block border-bottom m-0">
            Link 2
          </button>
          <button class="btn btn-link btn-block m-0">Link 3</button>
        </div>
      </div>
      <table class="table table-success table-bordered">
        <thead>
          <tr>
            <th colspan="4" style="background-color: aquamarine">
              Weather Forecast (4 Days)
            </th>
          </tr>
          <tr>
            <th>Date</th>
            <th>Forecast</th>
            <th>Relative Humidity</th>
            <th>Temperature</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in weather" v-bind:key="item.date">
            <th>{{ item.date }}</th>
            <td>{{ item.forecast }}</td>
            <td>
              High: {{ item.relative_humidity.high }}% | Low:
              {{ item.relative_humidity.low }}%
            </td>
            <td>
              High: {{ item.temperature.high }}°C | Low:
              {{ item.temperature.low }}°C
            </td>
          </tr>
        </tbody>
      </table>
      <div class="col-md-6 button-left">
        <button class="btn btn-success" @click="redirectInventory()">
          View Current Inventory
        </button>
      </div>

      <div class="col-md-6 button-right">
        <button class="btn btn-success" @click="redirectCrops()">
          View On-Growing Crops
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "FarmerHome",
  data() {
    return {
      weather: [],
    };
  },
  methods: {
    redirectInventory() {
      const userId = this.$route.params.id;
      this.$router.push(`${userId}/inventory`);
    },
    redirectCrops() {
      const userId = this.$route.params.id;
      this.$router.push(`${userId}/crops`);
    },
  },
  mounted() {
    // Send a reminder to uncomment this shit important!!!!!
    // axios
    //   .get("http://localhost:5005/check_status")
    //   .then((response) => {
    //     console.log(response.data);
    //   })
    //   .catch((error) => {
    //     console.log(error.message);
    //   });

    axios
      .get("https://api.data.gov.sg/v1/environment/4-day-weather-forecast")
      .then((response) => {
        this.weather = response.data.items[0].forecasts;
        console.log(this.weather);
      })
      .catch((error) => {
        console.log(error.message);
      });

    //
  },

  // do a twilio call
};
</script>

<style scoped>
.button-left {
  position: fixed;
  top: 90%;
  left: 5%;
}

.button-right {
  position: fixed;
  top: 90%;
  left: 70%;
}
.home {
  margin: 0;
  padding: 0;
  height: 100vh;
}
</style>
