<!-- For Scenerio 3 -->
<template>
    <div class="container-fluid">
        <table class="table table-hover">
            <thead>
                <tr>
                    <th scope="col">Batch Number</th>
                    <th scope="col">Crop Name</th>
                    <th scope="col">Crop Height</th>
                    <th scope="col">Recommended Water</th>
                    <th scope="col">Recommended Fertilizers</th>
                </tr>
            </thead>
            <tbody>
                <!-- <tr
                v-for="item in cropList"
                class="crop-item"
                v-bind:key="item.batchId"
                > -->
                <tr>
                    <th scope="row">Batch Number</th> <!-- To be replaced with a count fuction -->
                    <td>cropName</td>
                    <td>
                        <input
                        type="number"
                        class="form-control"
                        aria-label="cropHeight"
                        value="99"/>
                    </td>
                    <td>water</td>
                    <td>fertilizers</td>
                </tr>
            </tbody>
        </table>
        <div class="row d-flex align-items-end justify-content-end">
            <button class="btn btn-success" style="width: 10%;">Submit</button>
        </div>
    </div>
</template>

<script>
export default {
  name: 'OngoingCrops',
};
</script>

<style scoped>
</style>