<template>
  <div class="container-fluid payment">
    <div class="row login">
      <div class="col-md-6 col-sm-12 left-side">
        <h3>Purchased Products</h3>

        <table class="table table-striped table-dark">
          <thead>
            <tr>
              <th scope="col">Purchase Item No</th>
              <th scope="col">Crop Name</th>
              <th scope="col">Unit Price</th>
              <th scope="col">Quantity</th>
              <th scope="col">Price</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(crop, index) in this.crops">
              <th scope="row">{{ index + 1 }}</th>
              <td>{{ crop.name }}</td>
              <td>${{ crop.price }}</td>
              <td>{{ crop.orderNo }}</td>
              <td>${{ crop.orderNo * crop.price }}</td>
            </tr>
            <tr>
              <td>Total Price</td>
              <td colspan="4">${{ this.price }}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div
        class="col-md-6 col-sm-12 right-side mb-4 d-flex flex-column justify-content-center"
      >
        <div v-if="this.waiting == false">
          <h3>Customer Information</h3>
          <form>
            <div class="form-group">
              <label for="exampleFormControlInput1">Customer Name</label>
              <input
                type="email"
                class="form-control"
                id="exampleFormControlInput1"
                placeholder="name@example.com"
                v-model="this.customer_name"
              />
            </div>
            <div class="form-group">
              <label for="exampleFormControlInput1">Customer Phone</label>
              <input
                type="email"
                class="form-control"
                id="exampleFormControlInput1"
                placeholder="name@example.com"
                v-model="this.customer_phone"
              />
            </div>
            <div class="form-group">
              <label for="exampleFormControlInput1">Customer Address </label>
              <input
                type="email"
                class="form-control"
                id="exampleFormControlInput1"
                placeholder="name@example.com"
                v-model="this.customer_location"
              />
            </div>
          </form>

          <div class="text-center">
            <button
              type="button"
              class="btn btn-primary mt-5"
              @click="submitPurchaseActivity()"
            >
              Pay With Stripe
            </button>
          </div>
        </div>
        <div class="loading-screen" v-else>
          <span class="loader"></span>
          <h3>Waiting For Delivery Driver to Pick Up</h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      crops: [],
      price: 0,
      customer_location: "",
      customer_phone: "",
      customer_name: "",
      waiting: false,
    };
  },
  methods: {
    submitPurchaseActivity() {
      const customerId = this.$route.params.id;
      this.waiting = true;

      axios
        .post("http://127.0.0.1:5006/purchase_request", {
          // Check for order no
          cart_item: this.crops,
          customer_location: this.customer_location,
          customer_name: this.customer_name,
          customer_phone: this.customer_phone,
          customer_id: customerId,
          transaction_amt: this.price,
        })

        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
  },

  mounted() {
    const customerId = this.$route.params.id;

    axios
      .get(`http://127.0.0.1:5003/profile/${customerId}`)
      .then((response) => {
        this.customer_location = response.data.data.address;
        this.customer_name = response.data.data.name;
        this.customer_phone = response.data.data.phone;
      })
      .catch((error) => {
        console.log(error.message);
      });
    this.crops = localStorage.getItem("cropsPurchased");
    this.crops = JSON.parse(this.crops);
    for (const crop of this.crops) {
      this.price += crop.price * crop.orderNo;
      console.log(this.price);
      // Now post the price to delivery ms
    }

    // Get the customer details
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap");
.payment {
  margin: 0;
  padding: 0;
  height: 100vh;
}
.left-side {
  height: 100vh;
  background-color: #f8faf9ba;
  text-align: center;
}
.right-side {
  position: relative;
  height: 100vh;
  background-color: rgb(38, 224, 128);
}
#hero {
  font-weight: bold;
  text-align: center;
  font-size: 80px;
}
.loading-screen {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 30vw;
  height: 30vh;
  background-color: rgb(38, 224, 128);
}

.loader {
  --loader-size: 50px;
  --loader-border-size: 4px;
  --loader-border-color: white;
  width: var(--loader-size);
  height: var(--loader-size);
  border: var(--loader-border-size) solid var(--loader-border-color);
  border-top-color: transparent;
  border-right-color: transparent;
  border-bottom-color: transparent;
  background-color: transparent;
  border-radius: 50%;
  position: relative;
  animation: rotateX 1s infinite linear;
}

.loader::before {
  content: "";
  border: var(--loader-border-size) solid var(--loader-border-color);
  border-top-color: transparent;
  border-left-color: transparent;
  border-bottom-color: transparent;
  background-color: transparent;
  border-radius: 50%;
  position: absolute;
  top: 2px;
  left: 2px;
  right: 2px;
  bottom: 2px;
  animation: rotateX 0.5s infinite linear reverse;
}

@keyframes rotateX {
  from {
    transform: rotateZ(0deg);
  }
  to {
    transform: rotateZ(360deg);
  }
}
</style>
