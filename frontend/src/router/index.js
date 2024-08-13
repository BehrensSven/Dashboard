import { createRouter, createWebHistory } from 'vue-router';
import Login from '../components/LoginComponent.vue';
import Register from '../components/RegisterComponent.vue';
import Logout from '../components/LogoutComponent.vue';

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/logout', component: Logout },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;