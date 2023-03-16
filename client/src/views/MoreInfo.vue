<template>
    <div id="signup">
        <h1>Sign Up</h1>
        <div class="form-inputs">
            User Type:<input type="radio" id="Farmer" name="usertype" v-model="input.usertype" value="Farmer">
            <label for='Farmer'>Farmer</label>
            <input type="radio" id="Customer" name="usertype" v-model="input.usertype" value="Customer">
            <label for='Customer'>Customer</label>
        </div>
        <div class="form-inputs">
            <label for="name">Fullname</label>
            <input type="text" id="name" name="name" v-model="input.name" placeholder="Fullname" />
        </div>
        <div class="form-inputs">
            <label for="address">Address</label>
            <input type="text" id="password" name="password" v-model="input.password" placeholder="Password" />
        </div>
        <div class="form-inputs">
            <label for="phone">Phone No.</label>
            <input type="number" id="phone" name="phone" v-model="input.phone" placeholder="+65 ********" />
        </div>
        <div class="form-inputs">
            User Type:<input type="radio" id="usertype" name="usertype" v-model="input.usertype" value="Farmer">
            <label for='Farmer'>Farmer</label>
            <input type="radio" id="usertype" name="usertype" v-model="input.usertype" value="Customer">
            <label for='Customer'>Customer</label>
        </div>
        <button type="button" v-on:click="updateinfo()">Sign Up</button>
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