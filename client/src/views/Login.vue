<!-- <template>

    <div class="dropdown-menu">
        <h1>Login</h1>
        <form class="px-4 py-3">
            <div class="mb-3">
            <label for="email" class="form-label">Email address</label>
            <input type="email" class="form-control" id="email" name="email" placeholder="email@example.com">
            </div>
            <div class="mb-3">
            <label for="password" class="form-label">Password</label>
            <input type="password" class="form-control" id="password" name="password"  placeholder="Password">
            </div>
            <button type="button" class="btn btn-success">Sign in</button>
        </form>
        <div class="dropdown-divider"></div>
        Don't have an account? Sign up <router-link to="/Signup">Here</router-link>
        <a class="dropdown-item" href="#">Forgot password?</a>
    </div>
</template>  -->

<template>
    <div id="login">
        <h1>Login</h1>
        <div class="form-inputs">
            <input type="radio" id="Farmer" name="usertype" value="Farmer">
            <label for='Farmer'>Farmer</label>
            <input type="radio" id="Customer" name="usertype" value="Customer">
            <label for='Customer'>Customer</label>
            <input type="radio" id="staff" name="usertype" value="staff">
            <label for='staff'>Staff</label>
        </div>
        <div class="form-inputs">
            <label for="email">Email</label>
            <input type="text" id="email" name="email" placeholder="email@example.com" />
        </div>
        <div class="form-inputs">
            <label for="password">Password</label>
            <input type="password" id="password" name="password" placeholder="Password" />
        </div>
        <div>
    <router-link
      to="/Homeview"
      custom
      v-slot="{ navigate }"
    >
      <button
        @click="navigate"
        role="link"
      >
        Log In
      </button>
    </router-link>
  </div>
  Don't have an account? Sign up <router-link to="/Signup">Here</router-link>
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