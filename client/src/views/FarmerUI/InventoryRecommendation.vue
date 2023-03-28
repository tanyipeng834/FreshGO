<template>
    <div class="container-fluid">
        <!-- Only show when status button is clicked -->
        <!-- End of hidden div & table -->

        <div class="row">
        <table class="table table-hover">
            <thead>
                <tr>
                    <th scope ="col">Crop Name</th>
                    <th scope="col">Crops Sold Last Month</th>
                    <th scope="col">Current Amount Of Crops in Inventory</th>
                    <th scope="col">Recommnded Amount of Crops to Grow</th>
                    
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                   
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
        name :"",
        current:0,
        
    };
  },
  computed:{

    recommendAmount(){
        return this.previous - this.current
    }


  },

   
  mounted() {
    this.name = localStorage.getItem("name");
    axios.get(`http://localhost:5000/inventory/${this.name}`)
        .then(response => {
            console.log(reponse.data);
            this.current = response.data.data.quantity;

           return axios.get(`http://localhost:5006/purchase_request/${this.name}`)
               .then(response => {
                   let purchaseHistory = response.data.
               })
               .catch( error => {
                   console.log(error.message);
               });
        })
        .catch( error => {
            console.log(error.message);
        });
    
  },
  
};
</script>