<template>
    <div id="signup">
        <h1>Sign Up</h1>
        <div class="form-inputs">
            <label for="email">Email</label>
            <p><input type="text" id="email" v-model="email" placeholder="Email" /></p>
        </div>
        <div class="form-inputs">
            <label for="password">Password</label>
            <input type="password" id="password" v-model="password" placeholder="Password" />
        </div>
        <div class="form-inputs">
            <label for="cpassword">Confirm Password</label>
            <input type="password" id="cpassword" name="cpassword" placeholder="Confirm Password" />
        </div>
        <div class="form-inputs">
            <label for="password">Confirm Password</label>
            <input type="password" id="cpassword" name="cpassword" placeholder="Confirm Password" />
        </div>
        <div>
    <router-link
      to="/MoreInfo"
      custom
      v-slot="{ navigate }"
    >
      <button
        @click="register"
        role="link"
      >
        Signup
      </button>
    </router-link>
  </div>
        <br>
        Already have an account? Log in <router-link to="/Login">Here</router-link>
    </div>
</template>

<style>
#signup .form-inputs {
  padding-bottom: 10px;
}

#signup .form-inputs label {
  padding-right: 10px;
}
</style>

<script setup>
import { ref } from "vue";
import { getAuth, createUserWithEmailAndPassword } from "@firebase/auth";
import { useRouter } from "vue-router"
const email = ref("");
const password = ref("");
const router = useRouter()

const register = () =>{
  createUserWithEmailAndPassword(getAuth(), email.value, password.value)
    .then((data)=>{
      console.log("Successfully registered")
      router.push('/MoreInfo')
    })
    .catch((error)=>{
      console.log(error.code);
      alert(error.message);
    })
};
</script>