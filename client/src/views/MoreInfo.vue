<template>
    <div id="entry">
        <h1>New entry</h1>
        <div class="form-inputs">
            User Type:
            <input type="radio" id="Farmer" name="usertype"  value="Farmer">
            <label for='Farmer'>Farmer</label>
            <input type="radio" id="Customer" name="usertype" value="Customer">
            <label for='staff'>Customer</label>
            <input type="radio" id="staff" name="usertype" value="staff">
            <label for='staff'>Staff</label>
        </div>
        <div class="form-inputs">
            <label for="name">Fullname</label>
            <input type="text" id="name" name="name"  placeholder="Fullname" />
        </div>
        <div class="form-inputs">
            <label for="address">Address</label>
            <input type="text" id="password" name="password"  placeholder="Password" />
        </div>
        <div class="form-inputs">
            <label for="phone">Phone No.</label>
            <input type="number" id="phone" name="phone" placeholder="+65 ********" />
        </div>  
        <button type="button">Sign Up</button>
        <br>
    <router-link
      to="/MoreInfo"
      custom
      v-slot="{ navigate }"
    >
      <button
        @click="navigate"
        role="link"
      >
        Add new entry
      </button>
    </router-link>
  </div>
</template>