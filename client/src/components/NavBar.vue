<template>
    <div class="header" id="navbar">
        <router-link to="/products"><h1>AppName</h1>
        </router-link>
        <div class="header-right">
            <router-link to="/cart" >
                <button id="shoppingCartButton">Shopping Cart</button>
            </router-link>
        </div>
    </div>
</template>

<script>
export default {
    name:'NavBar',
}
</script>

<style scoped>
    #shoppingCartButton {
        background-color: #ffffff00; 
        border: none;
        color: black;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
    }

    #navbar{
        overflow: hidden;
        background-color: #77DD77;
        padding: 20px 10px;
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
        background-color: #bbffbb;
        color: black;
    }

    .header a.active {
        background-color: #539f53;
        color: white;
    }

    .header-right {
        float: right;
    }
</style>