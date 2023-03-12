<template>
  <nav></nav>
  <navbar />
  <router-view />

</template>

<script>
  import navbar from "./components/nav-bar.vue"
  export default {
    name: "App",
    components: {
      navbar,
    }
  };

</script>

<style></style>
