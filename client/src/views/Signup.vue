<template>
    <div id="signup">
        <h1>Sign Up</h1>
        <div class="form-inputs">
            <label for="email">Email</label>
            <input type="text" id="email" name="email" v-model="input.email" placeholder="Email" />
        </div>
        <div class="form-inputs">
            <label for="password">Password</label>
            <input type="password" id="password" name="password" v-model="input.password" placeholder="Password" />
        </div>
        <div class="form-inputs">
            <label for="cpassword">Confirm Password</label>
            <input type="password" id="cpassword" name="cpassword" v-model="input.cpassword" placeholder="Confirm Password" />
        </div>
        <div class="form-inputs">
            <label for="password">Confirm Password</label>
            <input type="password" id="cpassword" name="cpassword" v-model="input.cpassword" placeholder="Confirm Password" />
        </div>
        <div>
    <router-link
      to="/MoreInfo"
      custom
      v-slot="{ navigate }"
    >
      <button
        @click="navigate"
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

<script>
    export default {
        name: 'Login',
        data() {
            return {
                input: {
                    username: "",
                    password: ""
                }
            }
        },
        methods: {
            login() {
                if(this.input.username != "" && this.input.password != "") {
                    // This should actually be an api call not a check against this.$parent.mockAccount
                    if(this.input.username == this.$parent.mockAccount.username && this.input.password == this.$parent.mockAccount.password) {
                        this.$emit("authenticated", true);
                        this.$router.replace({ name: "Secure" });
                    } else {
                        console.log("The username and / or password is incorrect");
                    }
                } else {
                    console.log("A username and password must be present");
                }
            }
        }
    }
</script>

<style>

#signup .form-inputs {
    padding-bottom: 10px;
}

#signup .form-inputs label {
    padding-right: 10px;
}

</style>