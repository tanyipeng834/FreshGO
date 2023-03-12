import { createRouter, createWebHistory } from 'vue-router'
// import every page you have here & add the routes
import HomeView from '../views/HomeView.vue'
import CartPage from '../views/CartPage.vue'
import ProductDetailsPage from '../views/ProductDetailsPage.vue'
import ProductsPage from '../views/ProductsPage.vue'

const routes = [
  {
    path: '/home',
    name: 'HomeView',
    component: HomeView,
  },
  {
    path: '/',
    redirect: '/products',
  },
  {
    path: '/products',
    name: 'Products',
    component: ProductsPage,
  },
  {
    path: '/products/:id',
    // :id is a URL parameter, use it to choose the data that you want to display
    name: 'ProductDetails',
    component: ProductDetailsPage,
  },
  {
    path: '/cart',
    name: 'Cart',
    component: CartPage,
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
  
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
