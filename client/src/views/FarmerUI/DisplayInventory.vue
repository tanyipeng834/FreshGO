<!-- For Scenerio 2 -->
<template>
    <div class="container-fluid">
        <table class="table table-hover">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Crop Name</th>
                    <th scope="col">Quantity</th>
                    <th scope="col">Supply Level</th>
                </tr>
            </thead>
            <tbody>
                <!-- <tr
                v-for="item in inventoryList"
                class="inventory-item"
                v-bind:key="item.orderId"
                > -->
                <tr>
                    <th scope="row">1</th> <!-- To be replaced with a count fuction -->
                    <td>cropName</td>
                    <td>qty</td>
                    <td><button class="btn btn-success">Low</button></td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
  name: 'DisplayInventory',
};
</script>

<style scoped>
</style>