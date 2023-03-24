Manually set route 
<template>
    <div class="container justify-content-md-center">
        
        <!-- Ask for API KEY -->
        <GoogleMap api-key="APIKEY" style="width: 100%; height: 500px" :center="farm" :zoom="15">
        <!-- Marker -->
        <!-- <Marker :options="markerOptions" /> -->
        <Marker :options="{position: farm}" />
        <Marker :options="{position: deliveryDestination}" />
        <!-- Route -->
        <Polyline :options="deliveryPath" />
        </GoogleMap>
    </div>
</template>
  
<script>
import { defineComponent } from "vue";
// Refer to https://www.npmjs.com/package/vue3-google-map for guide on using vue3-google-maps
import { GoogleMap, Marker, Polyline } from "vue3-google-map";
  
export default defineComponent({
    components: { GoogleMap, Marker, Polyline },
    setup() {
        // SG Lat Lng, where to focus
        const center = { lat: 1.3521, lng: 103.8198 };
        // Coordinates of Local SG Farm ComCrop
        const farm = { lat: 1.448877461145454, lng: 103.80970858106836 };
        // Set Coordinates of Delivery Destination, used J8 as example
        const deliveryDestination = { lat: 1.3509382195266157, lng: 103.84875236757773 };
        // Set Marker
        const markerOptions = [
            { position: farm, label: "", title: "ComCrop" },
            { position: deliveryDestination, label: "", title: "Destination" }
        ];

        // Route coordinates, this is not edited yet
        const deliveryCoordinates = [
        { lat: 37.772, lng: -122.214 },
        { lat: 21.291, lng: -157.821 },
        { lat: -18.142, lng: 178.431 },
        { lat: -27.467, lng: 153.027 },
        ];

        // Routh Line Style
        const deliveryPath = {
            path: deliveryCoordinates,
            geodesic: true,
            strokeColor: "#FF0000",
            strokeOpacity: 1.0,
            strokeWeight: 2,
        };

        return { center, farm, deliveryDestination, deliveryPath, markerOptions };
    },
});
</script>