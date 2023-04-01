<!-- For Scenerio 3 -->
<template>
  <div class="container-fluid">
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">Crop Name</th>
          <th scope="col">Crop Batch</th>
          <th scope="col">Crop Quantity</th>
          <th scope="col">Batch Fertiliser Used(Daily)</th>
          <th scope="col">Batch Water Used (Daily)</th>
          <th scope="col">Batch Crop Height (Average)</th>
          <th scope="col">Recommnded Inputs</th>
          <th scope="col">Harvest</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in this.batches" :key="index">
          <td>{{ item.name }}</td>
          <td>{{ item.batch }}</td>
          <td>{{ item.quantity }}</td>
          <td>{{ item.fertiliser }}g</td>
          <td>{{ item.water }}ml</td>
          <td>{{ item.height }}cm</td>
          <td>
            <button
              type="button"
              class="btn btn-success"
              @click="recommend(item.name, item.quantity)"
            >
              Recommend
            </button>
          </td>
          <td>
            <button
              type="button"
              class="btn btn-success"
              @click="harvestCrops(item.name, item.batch)"
            >
              Harvest
            </button>
          </td>
        </tr>
      </tbody>
    </table>
    <div class="row d-flex align-items-end justify-content-end">
      <!-- Button trigger modal -->
      <button
        type="button"
        class="btn btn-primary mt-5"
        data-bs-toggle="modal"
        data-bs-target="#exampleModal"
      >
        Add Batch
      </button>

      <!-- Modal -->
      <div
        class="modal fade"
        id="exampleModal"
        tabindex="-1"
        aria-labelledby="exampleModalLabel"
        aria-hidden="true"
      >
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">
                Insert New Batch
              </h5>
              <button
                type="button"
                class="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              ></button>
            </div>
            <div class="modal-body">
              <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label"
                  >Name</label
                >
                <input
                  type="text"
                  class="form-control"
                  id="exampleFormControlInput1"
                  placeholder="Name"
                  v-model="this.name"
                />
              </div>
              <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label"
                  >Quantity</label
                >
                <input
                  type="number"
                  class="form-control"
                  id="exampleFormControlInput1"
                  placeholder="Quantity"
                  v-model="this.quantity"
                />
              </div>
              <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label"
                  >Fertiliser(g)</label
                >
                <input
                  type="number"
                  class="form-control"
                  id="exampleFormControlInput1"
                  placeholder="Fertiliser"
                  v-model="this.fertiliser"
                />
              </div>
              <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label"
                  >Water(ml)</label
                >
                <input
                  type="number"
                  class="form-control"
                  id="exampleFormControlInput1"
                  placeholder="Water"
                  v-model="this.water"
                />
              </div>
              <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label"
                  >Height(cm)</label
                >
                <input
                  type="number"
                  class="form-control"
                  id="exampleFormControlInput1"
                  placeholder="Height"
                  v-model="this.height"
                />
              </div>
            </div>
            <div class="modal-footer">
              <button
                type="button"
                class="btn btn-secondary"
                data-bs-dismiss="modal"
              >
                Close
              </button>
              <button
                type="button"
                class="btn btn-primary"
                @click="createNewBatch()"
                data-bs-dismiss="modal"
              >
                Save changes
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "OngoingCrops",
  data() {
    return {
      batches: [],
      name: "",
      quantity: 0,
      fertiliser: 0,
      water: 0,
      height: 0,
      componentKey: 0,
    };
  },
  mounted() {
    axios
      .get(`http://localhost:8000/api/v1/crop_management`)
      .then((response) => {
        console.log(response.data);
        this.batches = response.data.data;
      })
      .catch((error) => {
        console.log(error.message);
      });
  },
  methods: {
    createNewBatch() {
      axios
        .post("http://localhost:8000/api/v1/crop_management", {
          name: this.name,
          water: this.water,
          fertiliser: this.fertiliser,
          height: this.height,
          water: this.water,
          quantity: this.quantity,
        })
        .then((response) => {
          console.log(response.data);

          this.componentKey += 1;
        })
        .catch((error) => {
          console.log(error.message);
        });
    },

    harvestCrops(name, batch) {
      axios
        .delete("http://localhost:8000/api/v1/crop_management", {
          data: {
            name: name,
            batch: batch,
          },
        })
        .then((response) => {
          console.log(response.data);
          alert("Crop Harvested");
          location.reload();
          this.componentKey += 1;
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
    recommend(name, quantity) {
      const farmerId = this.$route.params.id;
      localStorage.setItem("cropQuantity", quantity);

      localStorage.setItem("cropName", name);
      this.$router.push(`/farmer/${farmerId}/crops/${name}`);
    },
  },
};
</script>

<style scoped></style>
