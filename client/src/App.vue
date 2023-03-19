<template>
  <!---<nav></nav>--->
  <!--<div>
        <div v-if="firstNavbar">
            <FirstNav />
        <div>
        <div v-if="secondNavbar">
            <SecondNav />
        </div>
       <router-view />
  </div>-->
  <CustomerNavBar />
  <router-view />

</template>

<script>
  import CustomerNavBar from "./components/CustomerNavBar.vue"
  
  export default {
    name: "App",
    components: {
      CustomerNavBar,
    }
  };

</script>

<style></style>
