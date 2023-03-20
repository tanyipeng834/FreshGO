<template>
  <!---<nav></nav>--->
  <!--Option 1: compute the route<div>
        <div v-if="firstNavbar">
            <FirstNav />
        <div>
        <div v-if="secondNavbar">
            <SecondNav />
        </div>
       <router-view />
  </div>-->
  <!--Option 2: add nav bar compnonet in index.js<router-view name="navbar"></router-view>-->
  <!-- <CustomerNavBar /> -->
  <router-view />

</template>

<script>
  import CustomerNavBar from "./components/CustomerNavBar.vue"
  import BeforeLogInNavBar from "./components/BeforeLogInNavBar.vue";
  import DeliveryStaffNavBar from "./components/DeliveryStaffNavBar.vue";
  import FarmerNavBar from "./components/FarmerNavBar.vue";
  
  export default {
    name: "App",
    components: {
      CustomerNavBar,
      BeforeLogInNavBar,
      DeliveryStaffNavBar,
      FarmerNavBar,
    }
  };

</script>

<style></style>
