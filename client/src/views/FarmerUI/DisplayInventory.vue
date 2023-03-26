<!-- For Scenerio 2 -->
<template>
    <div class="container-fluid">
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
                        <button id="statusBtn" 
                        ref="statusBtn" 
                        :class="`btn btn-${product.status}`">
                        {{ product.status }}
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import axios from "axios";
export default {
  name: 'DisplayInventory',
  data() {
    return {
        products: [],
    };
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