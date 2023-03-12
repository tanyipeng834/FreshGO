<template>
    <div class="header" id="navbar">
        <a href="#default" class="logo">CompanyLogo</a>
        <div class="header-right">
            <a class="active" href="#home">Home</a>
            <a href="#contact">Contact</a>
            <a href="#about">About</a>
        </div>
    </div>
</template>

<style scoped>
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