<template>
  <div id="page-wrap">
    <div class="grid-wrap">
      <div
        v-for="product in products"
        class="product-item"
        :key="product.name"
      >
        <img src="../../assets/caixinhua.jpg" />
        <h3 class="product-name">{{ product.name }}</h3>
        <p class="product-price">${{ product.price }}</p>
        <p class="product-price">{{ product.type }}</p>
        <div class="input-group mb-3">
          <span class="input-group-text">Quantity</span>
          <input
            v-model="product.quantity"
            type="number"
            class="form-control"
            aria-label="Quantity"
          />
        </div>
      </div>
    </div>
    <button
      class="btn btn-outline-success w-25 text-align-right"
      @click="purchaseProducts"
    >
      Purchase
    </button>
  </div>
</template>

<script>
import axios from "axios";
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
        this.products = response.data.data.inventory.map((product) => ({
          ...product,
          quantity: 0,
        }));
      })
      .catch((error) => {
        console.log(error.message);
      });
  },
  methods: {
    purchaseProducts() {
      const productsToPurchase = this.products
        .filter((product) => product.quantity > 0)
        .map(({ name, price, quantity }) => ({
          name,
          price,
          quantity,
        }));

      localStorage.setItem(
        "cropsPurchased",
        JSON.stringify(productsToPurchase)
      );
      console.log(productsToPurchase);
      const userId = this.$route.params.id;
      this.$router.push(`/customers/${userId}/payment`);
    },
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
