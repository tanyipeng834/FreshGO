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
            <label for="password">Confirm Password</label>
            <input type="password" id="cpassword" name="cpassword" v-model="input.cpassword" placeholder="Confirm Password" />
        </div>
        <div class="form-inputs">
            <label for="password">Confirm Password</label>
            <input type="password" id="cpassword" name="cpassword" v-model="input.cpassword" placeholder="Confirm Password" />
        </div>
        <div class="form-inputs">
            User Type:<input type="radio" id="Farmer" name="usertype" v-model="input.usertype" value="Farmer">
            <label for='Farmer'>Farmer</label>
            <input type="radio" id="Customer" name="usertype" v-model="input.usertype" value="Customer">
            <label for='Customer'>Customer</label>
        </div>
        <button type="button" v-on:click="signup()">Sign Up</button>
        <br>
        Already have an account? Log in <router-link to="/Login">Here</router-link>
    </div>
</template>