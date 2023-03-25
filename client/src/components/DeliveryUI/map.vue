<template>
  <div id="map" class="w-25"></div>
</template>

<script>
export default {
  name: "Map",
  mounted() {
    this.initMap();
    console.log(localStorage.getItem);
  },
  props: {
    destinationLocation: String,
  },
  methods: {
    initMap() {
      const directionsService = new google.maps.DirectionsService();
      const directionsRenderer = new google.maps.DirectionsRenderer();
      const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 14,
        center: { lat: 1.290059, lng: 103.821983 }, // Facotry Location
      });
      // Pass in props to change the origin and destination
      directionsRenderer.setMap(map);
      directionsService.route(
        {
          origin: "102 Henderson Road",
          destination: localStorage.getItem("destination"),
          travelMode: "DRIVING",
        },
        (response, status) => {
          if (status === "OK") {
            directionsRenderer.setDirections(response);
          }
        }
      );
    },
  },
};
</script>

<style scoped>
#map {
  height: 500px;
}
</style>
