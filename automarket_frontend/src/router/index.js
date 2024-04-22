import { createRouter, createWebHistory, RouterView } from 'vue-router'
import Trans from '@/i18n/translation'
import HomeView from '../views/HomeView.vue'
import CarView from '../views/CarsView.vue'
import Login from '../views/LoginView.vue'
import Signup from '../views/SignupView.vue'
import Add from '../views/AddView.vue'
import Blogs from '../views/BlogsView.vue'
import Search from '../views/SearchView.vue'
import Settings from '../views/SettingsView.vue'
import Profile from '../views/ProfileView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/:locale?",
      component: RouterView,
      beforeEnter: Trans.routeMiddleware,
      children: [
        {
          path: '',
          name: 'home',
          component: HomeView
        },
        {
          path: 'about',
          name: 'about',
          component: CarView
        },
        {
          path: 'login',
          name: 'login',
          component: Login
        },
        {
          path: 'signup',
          name: 'signup',
          component: Signup
        },
        {
          path: 'add',
          name: 'add',
          component: Add
        },
        {
          path: 'settings',
          name: 'settings',
          component: Settings
        },
        {
          path: 'profile',
          name: 'profile',
          component: Profile
        },
        {
          path: 'blogs',
          name: 'blogs',
          component: Blogs,
          beforeEnter: (to, from, next) => {
            // Scroll to the top of the page
            window.scrollTo(0, 0);
            next();
          }
        },
        {
          path: 'search',
          name: 'search',
          component: Search,
          },
      ]
    }
  ],
});

export default router
