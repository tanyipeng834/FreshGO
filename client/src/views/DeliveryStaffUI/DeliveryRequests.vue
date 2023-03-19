<template>
    <table class="table">
        <thead>
            <tr>
            <th scope="col">#</th>
            <th scope="col">Order ID</th>
            <th scope="col">Customer ID</th>
            <th scope="col">Delivery Address</th>
            <th scope="col">More Details</th>
            <th scope="col">Status</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="deliveryRequest in deliveryRequests" class="delivery-item" v-bind:key="deliveryRequest.orderId">
                <th scope="row">count</th>
                <td>{{ deliveryRequest.orderId }}</td>
                <td>{{ deliveryRequest.customerId }}</td>
                <td>{{ deliveryRequest.deliveryLocation }}</td>
                <td> 
                    <router-link v-bind:to="'/delivery/' + deliveryRequest.orderId">
                        <button>View Details</button>
                    </router-link>
                </td>
                <td>
                    <button>Accept</button>
                </td>
            </tr>
        </tbody>
    </table>

</template>

<script>
import {deliveryRequests} from '../../fakeDeliveryRequestsData'
export default {
    name: "DeliveryRequests",
    data() {
        return {
            deliveryRequests,
        };
    }
} ;
</script>

<style>
</style>