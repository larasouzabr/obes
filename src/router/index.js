import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../view/HomePage.vue";

import {
  isSignedIn,
  getUserTypeLogged,
  hasInfoCompleted,
} from "../services/auth";

/* import { isSignedIn } from "../services/auth"; */

const routes = [
  {
    path: "/",
    name: "Home",
    alias: "/home",
    component: HomePage,
  },
  {
    path: "/profile",
    name: "Profile",
    beforeEnter(_, __, next) {
      if (isSignedIn()) {
        const userType = getUserTypeLogged();

        if (userType === "common") {
          next("/profile/common-user");
        } else if (userType === "institutional") {
          next("/profile/institucional-user");
        }
      }
    },
  },

  {
    path: "/profile/common-user",
    name: "ProfileCommonUser",
    component: () =>
      import(
        /* webpackChunkName: "profile-common" */ "../view/ProfilePageCommonUser.vue"
      ),
    meta: {
      requeresAuth: true,
    },
  },

  {
    path: "/profile/institucional-user",
    name: "ProfileInstitucionalUser",
    component: () =>
      import(
        /* webpackChunkName: "profile-institucional" */ "../view/ProfilePageInstitucionalUser.vue"
      ),
    meta: {
      requeresAuth: true,
    },
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
    async beforeEnter(_, __, next) {
      if (isSignedIn()) {
        (await hasInfoCompleted())
          ? next()
          : next({ name: "RegistrationInfo" });
      } else next("/sign-in");
    },
    component: () => import("../view/DonateABook.vue"),
  },
  {
    path: "/profile/sellabook",
    name: "Sell",
    async beforeEnter(_, __, next) {
      if (isSignedIn()) {
        (await hasInfoCompleted())
          ? next()
          : next({ name: "RegistrationInfo" });
      } else next("/sign-in");
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
  {
    path: "/:pathMatch(.*)*",
    name: "NotFound",
    component: () => import("../view/ErrorPage.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
