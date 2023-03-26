import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "bootstrap/dist/css/bootstrap.min.css";

import "bootstrap";
createApp(App).use(router).mount("#app");

import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyB0bc09YJwsBqmnU4tjCNDM_bgrTxJGlgY",
  authDomain: "esdg1t1.firebaseapp.com",
  projectId: "esdg1t1",
  storageBucket: "esdg1t1.appspot.com",
  messagingSenderId: "524713522180",
  appId: "1:524713522180:web:d3c6ab3a14cf2c8e0fb151",
  measurementId: "G-X1TEY91TWX",
};

// Initialize Firebase
initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
