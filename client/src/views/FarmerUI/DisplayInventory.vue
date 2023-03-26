<!-- For Scenerio 2 -->
<template>
    <div class="container-fluid">
        <div v-show="weatherForecast" class="row">
            <table class="table table-success table-bordered">
                <thead>
                    <tr><th colspan="4" style="background-color: aquamarine;">Weather Forecast (4 Days)</th></tr>
                    <tr>
                        <th>Date</th>
                        <th>Forecast</th>
                        <th>Relative Humidity</th>
                        <th>Temperature</th>
                    </tr>
                </thead>
                <tbody>
                    <tr
                    v-for="item in weather"
                    v-bind:key="item.date">
                        <th>{{ item.date }}</th>
                        <td>{{ item.forecast }}</td>
                        <td>High: {{ item.relative_humidity.high }}% | Low: {{ item.relative_humidity.low }}%</td>
                        <td>High: {{ item.temperature.high }}°C | Low: {{ item.temperature.low }}°C</td>
                    </tr>
                </tbody>
            </table>
            <br>
        </div>
        <div class="row">
        <table class="table table-hover">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Crop Name</th>
                    <th scope="col">Quantity</th>
                    <th scope="col">Supply Level</th>
                </tr>
            </thead>
            <tbody>
                <tr
                v-for= "(product, index) in products"
                class="inventory-item"
                v-bind:key="product.name"
                >
                    <th scope="row">{{ index + 1 }}</th>
                    <td>{{ product.name }}</td>
                    <td>{{ product.quantity }} kg</td>
                    <td>
                        <!-- To add more onClick event just insert ";" then the function at @click
                        e.g. @click=" viewWeather(); weatherForecast=true"; newFunction() -->
                        <button id="statusBtn" 
                        ref="statusBtn" 
                        :class="`btn btn-${product.status}`"
                        @click=" viewWeather(); weatherForecast=true">
                        {{ product.status }}
                        </button>
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
  name: 'DisplayInventory',
  data() {
    return {
        products: [],
        weather:[],
        weatherForecast: false
    };
  },
  methods: {
    viewWeather() {
        axios
        .get("https://api.data.gov.sg/v1/environment/4-day-weather-forecast")
        .then(response => {
                this.weather = response.data.items[0].forecasts;
                console.log(this.weather)
            })
        .catch(error => {
            console.log(error.message)
        });
    }
  },
  mounted() {
    axios
      .get("http://127.0.0.1:5000/inventory")
      .then((response) => {
        this.products = response.data.data.inventory;
      })
      .catch((error) => {
        console.log(error.message);
      });
  },
};
</script>

<style scoped>
    .btn-Low{
        background-color: red;
        color: white;
    }
    
    .btn-Medium{
        background-color: yellow;
        color: white;
        /* To disable button */
        pointer-events: none;
    }

    .btn-High{
        background-color: green;
        color: white;
        pointer-events: none;
    }
</style>