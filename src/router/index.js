import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../view/HomePage.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomePage,
  },
  {
    path: "/profile",
    name: "Profile",
    component: () =>
      import(
        /* webpackChunkName: "about" */ "../view/ProfilePageCommonUser.vue"
      ),
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("../view/LoginPage.vue"),
  },
  {
    path: "/sign-up",
    name: "SignUp",
    component: () => import("../view/SignUpPage.vue"),
  },
  {
    path: "/register",
    name: "Register",
    component: () => import("../view/RegisterPage.vue"),
  },
  {
    path: "/profile/donateabook",
    name: "Donation",
    component: () => import("../view/DonateABook.vue"),
  },
  {
    path: "/profile/sellabook",
    name: "Sell",
    component: () => import("../view/SellABook.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
