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
              <td>{{ crop.quantity }}</td>
              <td>${{ crop.quantity * crop.price }}</td>
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
        <h3>Customer Information</h3>
        <form>
          <div class="form-group">
            <label for="exampleFormControlInput1">Email address</label>
            <input
              type="email"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="name@example.com"
            />
          </div>
          <div class="form-group">
            <label for="exampleFormControlSelect1">Example select</label>
            <select class="form-control" id="exampleFormControlSelect1">
              <option>1</option>
              <option>2</option>
              <option>3</option>
              <option>4</option>
              <option>5</option>
            </select>
          </div>
          <div class="form-group">
            <label for="exampleFormControlSelect2"
              >Example multiple select</label
            >
            <select
              multiple
              class="form-control"
              id="exampleFormControlSelect2"
            >
              <option>1</option>
              <option>2</option>
              <option>3</option>
              <option>4</option>
              <option>5</option>
            </select>
          </div>
          <div class="form-group">
            <label for="exampleFormControlTextarea1">Example textarea</label>
            <textarea
              class="form-control"
              id="exampleFormControlTextarea1"
              rows="3"
            ></textarea>
          </div>
        </form>

        <div class="text-center">
          <button
            type="button"
            class="btn btn-primary mt-3"
            @click="submitPurchaseActivity()"
          >
            Pay With Stripe
          </button>
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
    };
  },
  methods: {
    submitPurchaseActivity() {
      const customerId = this.$route.params.id;
      axios
        .get(`http://127.0.0.1:5003/profile/${customerId}`)
        .then((response) => {
          return axios.post("http://127.0.0.1:5006/purchase_request", {
            cart_item: this.crops,
            customer_location: response.data.data.address,
            customer_name: response.data.data.name,
            customer_phone: response.data.data.phone,
            customer_id: customerId,
            transaction_amt: this.price,
          });
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
    this.crops = localStorage.getItem("cropsPurchased");
    this.crops = JSON.parse(this.crops);
    for (const crop of this.crops) {
      this.price += crop.price * crop.quantity;
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
</style>
