<!-- <template>

    <div class="dropdown-menu">
        <h1>Login</h1>
        <form class="px-4 py-3">
            <div class="mb-3">
            <label for="email" class="form-label">Email address</label>
            <input type="email" class="form-control" id="email" name="email" placeholder="email@example.com">
            </div>
            <div class="mb-3">
            <label for="password" class="form-label">Password</label>
            <input type="password" class="form-control" id="password" name="password"  placeholder="Password">
            </div>
            <button type="button" class="btn btn-success">Sign in</button>
        </form>
        <div class="dropdown-divider"></div>
        Don't have an account? Sign up <router-link to="/Signup">Here</router-link>
        <a class="dropdown-item" href="#">Forgot password?</a>
    </div>
</template>  -->

<template>
    <!--<div id="login">
        <h1>Login</h1>
        <div class="form-inputs">
            <input type="radio" id="Farmer" name="usertype" value="Farmer">
            <label for='Farmer'>Farmer</label>
            <input type="radio" id="Customer" name="usertype" value="Customer">
            <label for='Customer'>Customer</label>
            <input type="radio" id="staff" name="usertype" value="staff">
            <label for='staff'>Staff</label>
        </div>
        <div class="form-inputs">
            <label for="email">Email</label>
            <input type="text" id="email" name="email" placeholder="email@example.com" />
        </div>
        <div class="form-inputs">
            <label for="password">Password</label>
            <input type="password" id="password" name="password" placeholder="Password" />
        </div>
        <button type="button" v-on:click="login()">Login</button>
        <br>
        Don't have an account? Sign up <router-link to="/Signup">Here</router-link>
    </div>-->

    <!--Need to edit to fit context-->
    <section class="vh-100" >
        <div class="container py-5 h-100">
            <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col col-xl-10">
                <div class="card" style="border-radius: 1rem; background-color: black; height: 20%;">
                <div class="row g-0">
                    <div class="col-md-6 col-lg-5 d-none d-md-block">
                    <img src="../assets/vegetables_background.jpg"
                        alt="login form" class="img-fluid" style="border-radius: 1rem 0 0 1rem; height: 100%; object-fit: cover;" />
                    </div>
                    <div class="col-md-6 col-lg-7 d-flex align-items-center">
                    <div class="card-body p-4 p-lg-5 text-white">

                        <form>

                        <div class="d-flex align-items-center mb-3 pb-1">
                            <i class="fas fa-cubes fa-2x me-3" style="color: #ff6219;"></i>
                            <!--<span class="h1 fw-bold mb-0">Logo</span>-->
                            <img src="../assets/logo/FreshGoWhite.png" alt="" class="img-fluid">
                        </div>

                        <h5 class="fw-normal mb-3 pb-3" style="letter-spacing: 1px;">Sign into your account</h5>

                        <div class="form-inputs mb-4">
                            <input type="radio" id="Farmer" name="usertype" v-model="input.usertype" value="Farmer">
                            <label for='Farmer'>Farmer</label>
                            <input type="radio" id="Customer" name="usertype" v-model="input.usertype" value="Customer">
                            <label for='Customer'>Customer</label>
                            <input type="radio" id="staff" name="usertype" v-model="input.usertype" value="staff">
                            <label for='staff'>Staff</label>
                        </div>

                        <div class="form-outline mb-4">
                            <input type="email" id="form2Example17" class="form-control form-control-lg" />
                            <label class="form-label text-white" for="form2Example17">Email address</label>
                        </div>

                        <div class="form-outline mb-4">
                            <input type="password" id="form2Example27" class="form-control form-control-lg" />
                            <label class="form-label text-white" for="form2Example27">Password</label>
                        </div>

                        <div class="pt-1 mb-4">
                            <button class="btn btn-outline-light btn-lg btn-block" type="button">Login</button>
                        </div>

                        <a class="small text-muted" href="#!">Forgot password?</a>
                        <p class="mb-5 pb-lg-2 text-white" >Don't have an account? <router-link to="/Signup" style="color: #096A2E;">Register Here</router-link></p>
                        </form>

                    </div>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
  name: "Login",
};
</script>

<<<<<<< HEAD
<style>
#login .form-inputs {
  padding-bottom: 10px;
}

#login .form-inputs label {
  padding-right: 10px;
}
</style>
=======
<style scoped>

#signup .form-inputs {
    padding-bottom: 10px;
}

#signup .form-inputs label {
    padding-right: 10px;
}

</style>
>>>>>>> 305c0a92437a03f602d43cd138f364021e2afdf9
