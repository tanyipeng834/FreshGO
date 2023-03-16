import { createRouter, createWebHistory } from 'vue-router'
// import every page you have here & add the routes
//Customer UI
import CartPage from '../views/CustomerUI/CartPage.vue'
import ProductDetailsPage from '../views/CustomerUI/ProductDetailsPage.vue'
import ProductsPage from '../views/CustomerUI/ProductsPage.vue'
import PaymentPage from '../views/CustomerUI/PaymentPage.vue'
//Unrelated to any UIs
import Home from '../views/Home.vue'
import HomeView from '../views/HomeView.vue'
import NotFoundPage from '../views/NotFoundPage.vue'


const routes = [
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/About.vue')
    }
  },
  {
    path: '/secure',
    name: 'Secure',
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/Secure.vue')
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/Login.vue')
    }
  },
  {
    path: '/Signup',
    name: 'Signup',
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/Signup.vue')
    }
  },
  {
    path: '/MoreInfo',
    name: 'MoreInfo',
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/MoreInfo.vue')
    }
  },
  {
    path: '/home',
    name: 'HomeView',
    component: HomeView,
  },
  {
    // home page
    path: '/',
    redirect: '/products',
  },
  {
    path: '/products',
    name: 'Products',
    component: ProductsPage,
    meta: {
      title: 'Products'
    }
  },
  {
    path: '/products/:id',
    // :id is a URL parameter, use it to choose the data that you want to display
    name: 'ProductDetails',
    component: ProductDetailsPage,
    meta: {
      title: 'Product Details'
    }
  },
  {
    path: '/cart',
    name: 'Cart',
    component: CartPage,
    meta: {
      title: 'Shopping Cart'
    }
  },
  {
    path: '/cart/payment',
    name: 'Payment',
    component: PaymentPage,
    meta: {
      title: 'Payment'
    }
  },
  {
    //keep it last, if there is no link found
    path: '/:pathMatch(.*)*',
    component: NotFoundPage,
    meta: {
      title: '404 Page Not Found'
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

//for dynamically changing page title
router.beforeEach((to, from) => {
  document.title = to.meta?.title ?? 'Default Title'
})

export default router

