<template>
  <div class="container-fluid login">
    <div class="row login">
      <div class="col-md-6 col-sm-12 left-side">
        <div
          id="carouselExampleSlidesOnly"
          class="carousel slide"
          data-bs-ride="carousel"
          data-bs-interval="2000"
        >
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img
                src="../assets/LoginPage/fresh.jpg"
                class="d-block w-100 h-100"
                alt="Fresh Fruits"
              />
              <h3 class="carousel-text mt-4">
                Want to have fruits and vegetables freshly delivered to your
                house?
              </h3>
            </div>
            <div class="carousel-item">
              <img
                src="../assets/LoginPage/crops.jpg"
                class="d-block w-100 h-100"
                alt="Crops Grown"
              />
              <h3 class="carousel-text mt-4">
                Want to montior the produce grown?
              </h3>
            </div>
            <div class="carousel-item">
              <img
                src="../assets/LoginPage/delivery_staff.jpg"
                class="d-block w-100 h-100"
                alt="Delivery Staff"
              />
              <h3 class="carousel-text mt-4">
                Want to earn some side cash as a Delivery Staff?
              </h3>
            </div>
          </div>
        </div>
      </div>

      <div
        class="col-md-6 col-sm-12 right-side mb-4 d-flex flex-column justify-content-center"
      >
        <div class="text-center">
          <img
            src="../assets/logo/FreshGoNormal.png"
            class="animate__animated animate__bounce bird mb-5"
            style="height: 100px; width: auto"
          />
        </div>
        <div class="login-form">
          <LoginForm />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import "animate.css";

import LoginForm from "../components/CustomerUI/LoginPage/LoginForm.vue";
export default {
  name: "Login",
  components: {
    LoginForm,
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap");

.login {
  margin: 0;
  padding: 0;
  height: 100vh;
}
.left-side {
  height: 100vh;
  background-color: #4fb91e;
  display: flex;
  text-align: center;
  align-items: center;
}
.right-side {
  position: relative;
  height: 100%;
  background-color: white;
}
#hero {
  font-weight: bold;
  text-align: center;
  font-size: 80px;
}
.carousel-text {
  color: white;
  font-weight: 700;
}
.bird:hover {
  animation-name: flip;
  animation-duration: 1s;
}

.right-side {
  position: relative;
  height: 100%;
  background-color: white;
  order: 1;
}
</style>
