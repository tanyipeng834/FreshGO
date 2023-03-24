<template>
    <div class="container-fluid">
        <div class="row justify-content-center">
            <h1>Delivery Distance in m: {{ travel }}m</h1>
            <h1>Delivery Distance in km: {{ toKm }}km</h1>
            <h1>Delivery Price: ${{ deliveryPrice }}</h1>
        </div>
    </div>
</template>
    
<script>
import axios from "axios"
export default {
    name: "DeliveryRequestDetails",
    data()
    {
        return {
            //travel: this.travel,
            travel: {},
        };
    },

    mounted() {
        axios
            .get("https://api.distancematrix.ai/maps/api/distancematrix/json?origins=2 Gambas Cres, Singapore 757044&destinations=9 Bishan Pl, Singapore 579837&key=DnWDU3yyV9JiLvLEEq61ZGWdVUGXD")
            // format of this api: https://api.distancematrix.ai/maps/api/distancematrix/json?origins={Origin Address}&destinations={Destination Address}&key={API KEY}
            // .then(response => {this.distance = response.data.rows[0].elements[0].distance})
            .then(response => {
                // console.log(response.data.rows[0].elements[0].distance)
                this.travel = response.data.rows[0].elements[0].distance.value
                //console.log(this.travel)
            })
            .catch(error => {
                console.log(error.message)
           });
    },

    computed: {
        // first 3km, flat rate $2, every km after, add $0.20
        deliveryPrice: function() {
            if(this.travel<=3000) {
                return 2.00;
            } else{
                if(((this.travel - 3000)/1000).toFixed(0)<1){
                    return 2 + 0.20;
                } else {
                    return (2 + ((this.travel - 3000)/1000).toFixed(0) * 0.2).toFixed(2);
                }
            }
        },

        toKm: function() {
            return (this.travel/1000).toFixed(2);
        },
    },
} ;
</script>

<style>
</style>
