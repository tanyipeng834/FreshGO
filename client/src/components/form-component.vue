<template>
  <form method="POST">
    <div class="form-group">
      <label for="exampleInputEmail1">Crop Name</label>
      <input
        type="text"
        class="form-control"
        id="exampleInputEmail1"
        aria-describedby="emailHelp"
        placeholder="Crop Name"
        v-model="cropName"
      />
    </div>
    <div class="form-group">
      <label for="exampleInputPassword1">Shell Life</label>
      <input
        type="text"
        class="form-control"
        id="exampleInputPassword1"
        placeholder="Password"
        v-model="shellLife"
      />
    </div>
    <div class="form-group">
      <label for="exampleInputPassword1">Price($)</label>
      <input
        type="number"
        class="form-control"
        id="exampleInputPassword1"
        placeholder="Price"
        v-model="price"
      />
    </div>
    <div class="form-group">
      <label for="exampleInputPassword1">Quantity</label>
      <input
        type="number"
        class="form-control"
        id="exampleInputPassword1"
        placeholder="Price"
        v-model="quantity"
      />
    </div>
    <div class="form-group">
      <label for="exampleInputPassword1">Height</label>
      <input
        type="number"
        class="form-control"
        id="exampleInputPassword1"
        placeholder="Height"
        v-model="height"
      />
    </div>
    <button type="submit" class="btn btn-primary mx-auto" @click="submitForm()">
      Submit
    </button>
  </form>
</template>

<script>
import axios from "axios";
export default {
  name: "form",
  data() {
    return {
      cropName: "",
      shellLife: "",
      price: "",
      quantity: "",
      height: "",
    };
  },

  props: {
    msg: String,
  },
  methods: {
    submitForm() {
      console.log(this.cropName);
      axios
        .post("http://127.0.0.1:5000/inventory", {
          crop: `${this.cropName}`,
          shellLife: `${this.shellLife}`,
          price: `${this.price}`,
          quantity:`${this.quantity}`,
          height : `${this.height}`
          
        })
        .then((response) => {
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
