import { createRouter, createWebHistory } from "vue-router";
// import every page you have here & add the routes
//Before Login UI
//Customer UI
import CartPage from "../views/CustomerUI/CartPage.vue";
import ProductDetailsPage from "../views/CustomerUI/ProductDetailsPage.vue";
import ProductsPage from "../views/CustomerUI/ProductsPage.vue";
import PaymentPage from "../views/CustomerUI/PaymentPage.vue";
//Delivery Staff UI
import DeliveryRequests from "../views/DeliveryStaffUI/DeliveryRequests";
import DeliveryRequestDetails from "../views/DeliveryStaffUI/DeliveryRequestDetails";
//Unrelated to any UIs
import Home from "../views/Home.vue";
import HomeView from "../views/HomeView.vue";
import NotFoundPage from "../views/NotFoundPage.vue";
//Ignore below for testing
// import Map from "../views/DeliveryStaffUI/Map.vue";

const routes = [
  {
    path: "/home",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "Login",
    component: function () {
      return import(/* webpackChunkName: "about" */ "../views/Login.vue");
    },
    meta: {
      title: "Login",
    },
  },
  {
    path: "/MoreInfo",
    name: "MoreInfo",
    component: function () {
      return import(/* webpackChunkName: "about" */ "../views/MoreInfo.vue");
    },
    meta: {
      title: "MoreInfo",
    },
  },
  {
    path: "/home",
    name: "HomeView",
    component: HomeView,
  },
  {
    path: "/dashboard",
    name: "dashboard",
    component: function () {
      return import(/* webpackChunkName: "about" */ "../views/Dashboard.vue");
    },
    meta: {
      title: "Dashboard",
    },
  },
  {
    path: "/Entry",
    name: "Entry",
    component: function () {
      return import(/* webpackChunkName: "about" */ "../views/Entry.vue");
    },
    meta: {
      title: "Entry",
    },
  },
  // Customer UI
  {
    // home page
    path: "/customer",
    redirect: "/customer/products",
  },
  {
    path: "/customer/products",
    name: "Products",
    component: ProductsPage,
    meta: {
      title: "Products",
    },
  },
  {
    path: "/products/:id",
    // :id is a URL parameter, use it to choose the data that you want to display
    name: "ProductDetails",
    component: ProductDetailsPage,
    meta: {
      title: "Product Details",
    },
  },
  {
    path: "/cart",
    name: "Cart",
    component: CartPage,
    meta: {
      title: "Shopping Cart",
    },
  },
  {
    path: "/cart/payment",
    name: "Payment",
    component: PaymentPage,
    meta: {
      title: "Payment",
    },
  },
  // Delivery Staff UI
  {
    path: "/delivery",
    name: "DeliveryRequests",
    component: DeliveryRequests,
    meta: {
      title: "Delivery Requests",
    },
  },
  {
    path: "/delivery/:id",
    name: "DeliveryRequestDetails",
    component: DeliveryRequestDetails,
    meta: {
      title: "Delivery Request Details",
    },
  },
  // {
  //   path: "/map",
  //   name: "Map",
  //   component: Map,
  //   meta: {
  //     title: "Test Map",
  //   },
  // },
  {
    //keep it last, if there is no link found
    path: "/:pathMatch(.*)*",
    component: NotFoundPage,
    meta: {
      title: "404 Page Not Found",
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

//for dynamically changing page title
router.beforeEach((to, from) => {
  document.title = to.meta?.title ?? "Default Title";
});

export default router;
