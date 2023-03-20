<template>
  <div class="formBox py-3 mx-3">
    <div class="mt-4">
      <h4 class="text-primary text-center"></h4>
      <div class="image"></div>
    </div>
    <div class="body-form">
      <form>
        <h3 class="mb-3">Choose Your Profile</h3>
        <div
          class="d-flex justify-content-around mb-3"
          role="group"
          aria-label="Basic radio toggle button group"
        >
          <input
            type="radio"
            class="btn-check"
            name="btnradio"
            id="btnradio1"
            autocomplete="off"
            value="customer"
            v-model="this.userType"
            checked
          />
          <label class="btn btn-outline-dark" for="btnradio1">Customer</label>

          <input
            type="radio"
            class="btn-check"
            name="btnradio"
            id="btnradio2"
            value="farmer"
            v-mdoel="this.userType"
            autocomplete="off"
          />
          <label class="btn btn-outline-dark" for="btnradio2">Farmer</label>

          <input
            type="radio"
            class="btn-check"
            name="btnradio"
            id="btnradio3"
            autocomplete="off"
            value="staff"
            v-model="this.userType"
          />
          <label class="btn btn-outline-dark" for="btnradio3"
            >Delivery Staff</label
          >
        </div>

        <div class="input-group mb-3">
          <div class="input-group-prepend">
            <span class="input-group-text">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                style="fill: rgba(0, 0, 0, 1); transform: ; msfilter: "
              >
                <path
                  d="m18.73 5.41-1.28 1L12 10.46 6.55 6.37l-1.28-1A2 2 0 0 0 2 7.05v11.59A1.36 1.36 0 0 0 3.36 20h3.19v-7.72L12 16.37l5.45-4.09V20h3.19A1.36 1.36 0 0 0 22 18.64V7.05a2 2 0 0 0-3.27-1.64z"
                ></path>
              </svg>
            </span>
          </div>
          <input
            type="text"
            class="form-control"
            placeholder="Email"
            name="email"
            v-model="email"
          />
        </div>
        <div class="input-group mb-3">
          <div class="input-group-prepend">
            <span class="input-group-text">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                style="fill: rgba(0, 0, 0, 1); transform: ; msfilter: "
              >
                <path
                  d="M12 2C9.243 2 7 4.243 7 7v3H6a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8a2 2 0 0 0-2-2h-1V7c0-2.757-2.243-5-5-5zM9 7c0-1.654 1.346-3 3-3s3 1.346 3 3v3H9V7zm4 10.723V20h-2v-2.277a1.993 1.993 0 0 1 .567-3.677A2.001 2.001 0 0 1 14 16a1.99 1.99 0 0 1-1 1.723z"
                ></path>
              </svg>
            </span>
          </div>
          <input
            type="password"
            class="form-control"
            placeholder="Password"
            name="password"
            v-model="password"
          />
        </div>

        <div class="input-group mb-3" v-if="this.signUp">
          <div class="input-group-prepend">
            <span class="input-group-text">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                style="fill: rgba(0, 0, 0, 1); transform: ; msfilter: "
              >
                <path
                  d="M12 2C9.243 2 7 4.243 7 7v3H6a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8a2 2 0 0 0-2-2h-1V7c0-2.757-2.243-5-5-5zM9 7c0-1.654 1.346-3 3-3s3 1.346 3 3v3H9V7zm4 10.723V20h-2v-2.277a1.993 1.993 0 0 1 .567-3.677A2.001 2.001 0 0 1 14 16a1.99 1.99 0 0 1-1 1.723z"
                ></path>
              </svg>
            </span>
          </div>
          <!-- Check if the confirm password field is the same as the password field -->
          <input
            type="password"
            class="form-control"
            placeholder="Confirm Password"
            name="password"
          />
        </div>

        <button
          type="button"
          class="login-button"
          @click="login()"
          v-if="this.signUp == false"
        >
          LOGIN
        </button>
        <button
          type="button"
          class="login-button"
          @click="createNewAccount()"
          v-else
        >
          Signup
        </button>

        <div class="">
          <div v-if="this.signUp == false">
            New user?
            <a @click="newUser()"> <b>Sign up</b> </a>
          </div>
          <div v-else>
            Have an Account?
            <a @click="newUser()"> <b>Sign In</b> </a>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "LoginForm",
  data() {
    return {
      email: "",
      password: "",
      signUp: false,
      userType: "customer",
    };
  },
  methods: {
    newUser() {
      this.signUp = !this.signUp;
      console.log(this.signUp);
    },
    // This is the code for users to sign in to the
    signIn() {
      axios
        .post(`http://127.0.0.1:5003/create/${this.userType}/${this.email}`, {
          key: value,
        })
        .then((response) => {
          // console.log(response.data);
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
    createNewAccount() {
      axios
        .post(`http://127.0.0.1:5003/create/${this.userType}/${this.email}`, {
          password: this.password,
          profile_type: this.userType,
        })
        .then((response) => {
          console.log(response.data);
          alert("Account Succesfully Created");
        })
        .catch((error) => {
          console.log(error.message);
          alert("Email already exisits");
        });
    },
  },
};
</script>

<style scoped>
.formBox {
  background-color: #19de9c;
  border-radius: 15px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.body-form {
  width: 380px;
  height: auto;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  border-radius: 2%;
  text-align: center;
}
.login-button {
  margin-top: 5%;
  border-radius: 10px;
  border-color: #253f63;
  background-color: #010101;
  color: #fff;
  font-family: Montserrat, sans-serif;
  font-weight: 700;
  width: 65%;
  height: 50%;
}
.message {
  text-decoration: none;
  background-color: none;
  font-weight: 800;
}
a:link {
  text-decoration: none;
}
a {
  color: #0579fd;
}
a:hover {
  text-shadow: 1px 1px 2px rgb(130, 130, 130);
  transition: 0.4s;
}
.login-button:hover,
.login-button:focus {
  box-shadow: 0 0.5em 0.5em -0.4em rgb(141, 140, 140);
  transform: translateY(-0.25em);
  transition: 0.4s;
}
</style>
