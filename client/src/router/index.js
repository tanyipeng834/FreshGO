import { createRouter, createWebHistory } from 'vue-router'
// import every page you have here & add the routes
import HomeView from '../views/HomeView.vue'
import CartPage from '../views/CartPage.vue'
import ProductDetailsPage from '../views/ProductDetailsPage.vue'
import ProductsPage from '../views/ProductsPage.vue'
import NotFoundPage from '../views/NotFoundPage.vue'
import PaymentPage from '../views/PaymentPage.vue'

const routes = [
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
    path: '/cart/payment',
    name: 'Payment',
    component: PaymentPage,
  },
  //{
  //  path: '/about',
  //  name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
  
  //}, 
  {
    //keep it last, if there is no link found
    path: '/:pathMatch(.*)*',
    component: NotFoundPage,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
