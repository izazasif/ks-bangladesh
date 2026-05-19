import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const routes = [
  { path: '/', name: 'Home', component: () => import('../views/Home.vue') },
  { path: '/services', name: 'Services', component: () => import('../views/services/Services.vue') },
  { path: '/about', name: 'About', component: () => import('../views/About.vue') },
  { path: '/contact', name: 'Contact', component: () => import('../views/Contact.vue') },
  { path: '/signup', name: 'SignUp', component: () => import('../views/SignUp.vue') },
  { path: '/login', name: 'Login', component: () => import('../views/Login.vue') },
  {
    path: '/sectors/agriculture',
    name: 'Agriculture',
    component: () => import('../views/sectors/Agriculture.vue'),
  },
  {
    path: '/sectors/it',
    name: 'IT',
    component: () => import('../views/sectors/IT.vue'),
  },
  {
    path: '/sectors/construction',
    name: 'Construction',
    component: () => import('../views/sectors/Construction.vue'),
  },
  {
    path: '/sectors/transportation',
    name: 'Transportation',
    component: () => import('../views/sectors/Transportation.vue'),
  },
  {
    path: '/dashboard/user',
    name: 'UserDashboard',
    component: () => import('../views/dashboard/UserDashboard.vue'),
    meta: { requiresAuth: true },
  },
  {
    path: '/dashboard/admin',
    name: 'AdminDashboard',
    component: () => import('../views/dashboard/AdminDashboard.vue'),
    meta: { requiresAuth: true, requiresAdmin: true },
  },
  {
    path: '/profile/edit',
    name: 'ProfileEdit',
    component: () => import('../views/dashboard/ProfileEdit.vue'),
    meta: { requiresAuth: true },
  },
  { path: '/:pathMatch(.*)*', redirect: '/' },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() {
    return { top: 0, behavior: 'smooth' }
  },
})

router.beforeEach(async (to) => {
  const authStore = useAuthStore()
  if (!authStore.isAuthenticated) {
    await authStore.restoreSession()
  }
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    return { name: 'Login', query: { redirect: to.fullPath } }
  }
  if (to.meta.requiresAdmin && authStore.user?.role !== 'admin') {
    return { name: 'UserDashboard' }
  }
  if ((to.name === 'Login' || to.name === 'SignUp') && authStore.isAuthenticated) {
    return { name: authStore.user?.role === 'admin' ? 'AdminDashboard' : 'UserDashboard' }
  }
})

export default router
