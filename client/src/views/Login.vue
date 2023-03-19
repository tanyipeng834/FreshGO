<template>
    <div id="login">
        <h1>Login</h1>
        <div class="form-inputs">
            <input type="radio" id="Farmer" name="usertype" v-model="input.usertype" value="Farmer">
            <label for='Farmer'>Farmer</label>
            <input type="radio" id="Customer" name="usertype" v-model="input.usertype" value="Customer">
            <label for='Customer'>Customer</label>
        </div>
        <div class="form-inputs">
            <label for="email">Email</label>
            <input type="text" id="email" name="email" v-model="input.email" placeholder="email@example.com" />
        </div>
        <div class="form-inputs">
            <label for="password">Password</label>
            <input type="password" id="password" name="password" v-model="input.password" placeholder="Password" />
        </div>
        <button type="button" v-on:click="login()">Login</button>
        <br>
        Don't have an account? Sign up <router-link to="/Signup">Here</router-link>
    </div>

    <!--<div class="dropdown-menu">
    <form class="px-4 py-3">
        <div class="mb-3">
        <label for="email" class="form-label">Email address</label>
        <input type="email" class="form-control" id="email" name="email" v-model="input.email" placeholder="email@example.com">
        </div>
        <div class="mb-3">
        <label for="password" class="form-label">Password</label>
        <input type="password" class="form-control" id="password" name="Password" v-model="input.password" placeholder="Password">
        </div>

        <button type="button" v-on:click="login()" class="btn btn-success">Sign in</button>
    </form>
    <div class="dropdown-divider"></div>
    Don't have an account? Sign up <router-link to="/Signup">Here</router-link>
    <a class="dropdown-item" href="#">Forgot password?</a>
</div>-->
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

#login .form-inputs {
    padding-bottom: 10px;
}

#login .form-inputs label {
    padding-right: 10px;
}

</style>