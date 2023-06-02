import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../view/HomePage.vue";
import { isSignedIn, getUserLoggedInfo } from "../services/auth";

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
    path: "/books",
    name: "Books",
    component: () => import("../view/FindBooksPage.vue"),
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
    beforeEnter(_, __, next) {
      if (isSignedIn()) {
        // const user = getUserLoggedInfo();
        // if (user.phone_number == null) {
        //   next("/fill-info");
        // }
        next();
        return;
      }
      next("/sign-in");
    },
    component: () => import("../view/DonateABook.vue"),
  },
  {
    path: "/profile/sellabook",
    name: "Sell",
    beforeEnter(_, __, next) {
      if (isSignedIn()) {
        next();
        return;
      }
      next("/sign-in");
    },
    component: () => import("../view/SellABook.vue"),
  },
  {
    path: "/book-detail/:id",
    name: "BookDetail",
    component: () => import("../view/BookDetailPage.vue"),
    props: true,
  },
  {
    path: "/fill-info",
    name: "RegistrationInfo",
    component: () => import("../view/RegistrationPersonalInfo.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
