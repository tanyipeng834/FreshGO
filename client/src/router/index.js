import { createRouter, createWebHistory } from "vue-router";
// import every page you have here & add the routes
//Before Login UI
//Customer UI

import ProductsPage from "../views/CustomerUI/ProductsPage.vue";
import PaymentPage from "../views/CustomerUI/PaymentPage.vue";
//Delivery Staff UI
import DeliveryRequests from "../views/DeliveryStaffUI/DeliveryRequests";
import DeliveryRequestDetails from "../views/DeliveryStaffUI/DeliveryRequestDetails";
// Farmer UI
import FarmerHome from "../views/FarmerUI/FarmerHome.vue";
import DisplayInventory from "../views/FarmerUI/DisplayInventory.vue";
import OngoingCrops from "../views/FarmerUI/OngoingCrops.vue";
//Unrelated to any UIs
import Home from "../views/Home.vue";
import HomeView from "../views/HomeView.vue";
import NotFoundPage from "../views/NotFoundPage.vue";
import CustomerDelivery from "../views/CustomerUI/CustomerDelivery.vue";
//Ignore below for testing

const routes = [
  {
    path: "/home",
    name: "Home",
    component: Home,
  },
  {
    path: "/",
    name: "Login",
    component: function () {
      return import(/* webpackChunkName: "about" */ "../views/Login.vue");
    },
    meta: {
      title: "Login",
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
    path: "/customer/:id",
    name: "Products",
    component: ProductsPage,
    meta: {
      title: "Products",
    },
  },

  {
    path: "/customers/:id/payment",
    name: "Payment",
    component: PaymentPage,
    meta: {
      title: "Payment",
    },
  },

  {
    path: "/customers/:id/:deliveryId",
    name: "Customer Delivery",
    component: CustomerDelivery,
    meta: {
      title: "Customer Delivery",
    },
  },
  // Delivery Staff UI
  {
    path: "/delivery/:staffId",
    name: "DeliveryRequests",
    component: DeliveryRequests,
    meta: {
      title: "Delivery Requests",
    },
  },
  {
    path: "/delivery/:staffId/:deliveryId",
    name: "DeliveryRequestDetails",
    component: DeliveryRequestDetails,
    meta: {
      title: "Delivery Request Details",
    },
  },
  // Below for testing

  //Farmer UI

  {
    path: "/recommend",
    name: "InventoryRecommend",
    component: function () {
      return import(
        /* webpackChunkName: "about" */ "../views/FarmerUI/InventoryRecommendation.vue"
      );
    },
    meta: {
      title: "Recommendation",
    },
  },
  {
    path: "/crops",
    name: "OngoingCrops",
    component: OngoingCrops,
    meta: {
      title: "Crops",
    },
  },
  {
    path: "/farmer/:id",
    name: "FarmerHome",
    component: FarmerHome,
    meta: {
      title: "Home",
    },
  },
  {
    path: "/farmer/:id/inventory",
    name: "DisplayInventory",
    component: DisplayInventory,
    meta: {
      title: "Inventory",
    },
  },
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
