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
     beforeEnter: function (to, from, next) {
        const token = localStorage.getItem('user-token')

        if (!token) {
          next('/login')
        } else {
          next()
        }
      },
    component: () => import("../view/DonateABook.vue"),
  },
  {
    path: "/profile/sellabook",
    name: "Sell",
     beforeEnter: function (to, from, next) {
        const token = localStorage.getItem('user-token')

        if (!token) {
          next('/login')
        } else {
          next()
        }
      },
    component: () => import("../view/SellABook.vue")
  },
  { path: "/book-detail",
    name: "BookDetail",
    component: () => import("../view/BookDetailPage.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
