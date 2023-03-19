<template>
    <div class="header" id="navbar">
        <router-link to="/products">
            <img src="../assets/logo/FreshGoWhite.png" style="width:100px">
        </router-link>
    </div>
</template>

<script>
export default {
    name:'DeliveryStaffNavBar',
}
</script>

<style scoped>
    #navbar{
        overflow: hidden;
        background-color: #729343;
        padding: 20px 10px;
        border-bottom: 3px solid #096A2E;
    }

    .header a {
        float: left;
        color: black;
        text-align: center;
        padding: 12px;
        text-decoration: none;
        font-size: 18px;
        line-height: 25px;
        border-radius: 4px;
    }   

    .header a.logo {
        font-size: 25px;
        font-weight: bold;
    }

    .header a:hover {
        background-color: #096A2E;
        color: black;
    }

    .header a.active {
        background-color: #096A2E;
        color: white;
    }

    .header-right {
        float: right;
    }
</style>