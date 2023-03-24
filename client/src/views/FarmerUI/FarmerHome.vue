<template>
    <div class="container">
        <div class="row">
            <router-link v-bind:to="'/inventory'">
            <button class="btn btn-success">View Inventory</button>
          </router-link>
        </div>
        <div class="row">
            <router-link v-bind:to="'/crops'">
            <button class="btn btn-success">View Crops</button>
          </router-link>
        </div>
    </div>
</template>

<script>
export default {
  name: 'FarmerHome',
};
</script>

<style scoped>
</style>