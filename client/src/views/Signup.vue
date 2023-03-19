<template>
    <div id="signup">
        <h1>Sign Up</h1>
        <div class="form-inputs">
            <label for="email">Email</label>
            <input type="text" id="email" name="email" placeholder="Email" />
        </div>
        <div class="form-inputs">
            <label for="password">Password</label>
            <input type="password" id="password" name="password" placeholder="Password" />
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

<style>
#signup .form-inputs {
  padding-bottom: 10px;
}

#signup .form-inputs label {
  padding-right: 10px;
}
</style>
