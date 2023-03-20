<template>
  <div id="page-wrap">
    <div class="grid-wrap">
      <div
        v-for="product in this.products"
        class="product-item"
        v-bind:key="product.CropName"
      >
        <img v-bind:src="product.imageURL" />
        <h3 class="product-name">{{ product.CropName }}</h3>
        <p class="product-price">${{ product.Price }}</p>
        <router-link v-bind:to="'/products/' + product.CropName">
          <button class="btn btn-outline-success">View Details</button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { createDOMCompilerError } from "@vue/compiler-dom";
import axios from "axios";
import { products } from "../../fakeProductsData.js";

export default {
  name: "ProductsPage",
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
        console.log(this.products);
      })
      .catch((error) => {
        console.log(error.message);
      });
  },
};
</script>

<style scoped>
.grid-wrap {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin-top: 16px;
}

.product-item {
  align-items: center;
  border-radius: 8px;
  box-shadow: 0px 2px 5px #888;
  display: flex;
  flex-direction: column;
  margin-bottom: 2%;
  padding: 20px;
  position: relative;
  width: 32%;
}

.product-name {
  margin-bottom: 0;
}

img {
  height: 200px;
  width: 200px;
}

a {
  width: 100%;
}

button {
  width: 100%;
}
</style>
