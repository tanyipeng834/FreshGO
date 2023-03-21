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
                  d="M12 2c-4.963 0-9 4.038-9 9v8h.051c.245 1.691 1.69 3 3.449 3 1.174 0 2.074-.417 2.672-1.174a3.99 3.99 0 0 0 5.668-.014c.601.762 1.504 1.188 2.66 1.188 1.93 0 3.5-1.57 3.5-3.5V11c0-4.962-4.037-9-9-9zm7 16.5c0 .827-.673 1.5-1.5 1.5-.449 0-1.5 0-1.5-2v-1h-2v1c0 1.103-.897 2-2 2s-2-.897-2-2v-1H8v1c0 1.845-.774 2-1.5 2-.827 0-1.5-.673-1.5-1.5V11c0-3.86 3.141-7 7-7s7 3.14 7 7v7.5z"
                ></path>
                <circle cx="9" cy="10" r="2"></circle>
                <circle cx="15" cy="10" r="2"></circle>
              </svg>
            </span>
          </div>
          <!-- Check if the confirm password field is the same as the password field -->
          <input
            type="text"
            class="form-control"
            placeholder="Name"
            name="name"
            v-model="this.name"
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
                  d="M20 10.999h2C22 5.869 18.127 2 12.99 2v2C17.052 4 20 6.943 20 10.999z"
                ></path>
                <path
                  d="M13 8c2.103 0 3 .897 3 3h2c0-3.225-1.775-5-5-5v2zm3.422 5.443a1.001 1.001 0 0 0-1.391.043l-2.393 2.461c-.576-.11-1.734-.471-2.926-1.66-1.192-1.193-1.553-2.354-1.66-2.926l2.459-2.394a1 1 0 0 0 .043-1.391L6.859 3.513a1 1 0 0 0-1.391-.087l-2.17 1.861a1 1 0 0 0-.29.649c-.015.25-.301 6.172 4.291 10.766C11.305 20.707 16.323 21 17.705 21c.202 0 .326-.006.359-.008a.992.992 0 0 0 .648-.291l1.86-2.171a1 1 0 0 0-.086-1.391l-4.064-3.696z"
                ></path>
              </svg>
            </span>
          </div>
          <!-- Check if the confirm password field is the same as the password field -->
          <input
            type="text"
            class="form-control"
            placeholder="Phone"
            name="Phone"
            v-model="this.phone"
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
                  d="m20.772 10.156-1.368-4.105A2.995 2.995 0 0 0 16.559 4H7.441a2.995 2.995 0 0 0-2.845 2.051l-1.368 4.105A2.003 2.003 0 0 0 2 12v5c0 .753.423 1.402 1.039 1.743-.013.066-.039.126-.039.195V21a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-2h12v2a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-2.062c0-.069-.026-.13-.039-.195A1.993 1.993 0 0 0 22 17v-5c0-.829-.508-1.541-1.228-1.844zM4 17v-5h16l.002 5H4zM7.441 6h9.117c.431 0 .813.274.949.684L18.613 10H5.387l1.105-3.316A1 1 0 0 1 7.441 6z"
                ></path>
                <circle cx="6.5" cy="14.5" r="1.5"></circle>
                <circle cx="17.5" cy="14.5" r="1.5"></circle>
              </svg>
            </span>
          </div>
          <!-- Check if the confirm password field is the same as the password field -->
          <input
            type="text"
            class="form-control"
            placeholder="Address"
            name="Address"
            v-model="this.address"
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
          id="btnlogin"
          @click="signIn()"
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
import router from "@/router";
export default {
  name: "LoginForm",
  data() {
    return {
      email: "",
      password: "",
      signUp: false,
      userType: "customer",
      name: "",
      address: "",
      phone: "",
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
        .post(`http://127.0.0.1:5003/signIn/${this.userType}`, {
          email: this.email,
          password: this.password,
        })
        .then((response) => {
          console.log(response);
          if (response.data.code == 200) {
            alert("Account Credentials are Correct");
            // Now we will start going to the correct route
            router.push("/customer");
            localStorage.set("userId", response.data.userId);
          }
          // console.log(response.data);
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
    createNewAccount() {
      axios
        .post(`http://127.0.0.1:5003/create/${this.userType}/${this.email}`, {
          email: this.email,
          password: this.password,
          profile_type: this.userType,
          name: this.name,
          phone: this.phone,
          address: this.address,
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
