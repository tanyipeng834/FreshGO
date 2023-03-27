<template>
    <div class="container-fluid">
        <!-- Only show when status button is clicked -->
        <!-- End of hidden div & table -->

        <div class="row">
        <table class="table table-hover">
            <thead>
                <tr>
                    <th scope="col">Type of plant</th>
                    <th scope="col">Amount to plant</th>
                    
                </tr>
            </thead>
            <tbody>
                <tr
                    v-for="total in Object.keys(totals)">
                        <td>{{ total }}</td>
                        <td v-if="totals[total]-quantity>0">{{ totals[total]-cropquantity }} KG</td>
                        <td v-else>0 KG (Less sold last month than amount in inventory)</td>    
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
        activity:[],
        weather:[],
        weatherForecast: false,
        totals: {}
    };
  },
  methods: {
    viewWeather() {
        axios
        .get("https://api.data.gov.sg/v1/environment/4-day-weather-forecast")
        .then(response => {
                this.weather = response.data.items[0].forecasts;
            })
        .catch(error => {
            console.log(error.message)
        });
    },
    viewactivity(){
        axios
        .get("http://127.0.0.1:5006/purchase_request")
        .then((response) => {
            this.activity = response.data.data["Purchase Requests"];
            this.totals = {}
            for(this.i in this.activity){
                this.crops = this.activity[this.i].crop_purchased
                //only uncomment below when there is complete status plants
                //if(this.valid==this.productname){
                    for(this.j in this.crops){
                        this.quantity=this.crops[this.j]['Quantity']
                        this.name=this.crops[this.j]['Crop Name']
                        if(this.name == this.productname){
                            if (isNaN(this.totals[this.name] )){
                                this.totals[this.name]=this.quantity
                            }
                            else{
                                this.totals[this.name]+= this.quantity
                            }
                        }
                    }
                    
                //}
                
            }
            if(Object.keys(this.totals).length==0){
                this.totals[this.productname]=0
            }
        })
        .catch((error) => {
            console.log(error.message);
        });
    }
  },
  mounted() {
    axios
      .get("http://127.0.0.1:5000/inventory")
      .then((response) => {
        this.products = response.data.data.inventory;
        console.log(this.products)
        this.cropquantity = 0
        for(this.product of this.products){
            if (this.product.name==this.productname){
                this.cropquantity += this.product.quantity
            }
        }
        console.log(this.cropquantity)
      })
      .catch((error) => {
        console.log(error.message);
      });

    this.viewWeather()
    this.viewactivity()
    this.productname=localStorage.getItem('name')
  },
  
};
</script>