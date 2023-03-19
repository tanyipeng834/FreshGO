<template>
    <div class="header sticky-sm-top" id="navbar">
        <router-link to="/delivery">
            <img src="../assets/logo/FreshGoWhite.png" style="width:100px">
        </router-link>
        <div class="header-right">
            <router-link to="/login" >
                <button id="shoppingCartButton">Log Out</button>
            </router-link>
        </div>
    </div>
</template>

<script>
export default {
    name:'DeliveryStaffNavBar',
}
</script>

<style scoped>
    #shoppingCartButton {
        background-color: #ffffff00; 
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
    }
    
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