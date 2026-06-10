<template>
  <!-- Top announcement bar -->
  <div class="hidden bg-slate-900 px-4 py-2 text-center text-xs text-slate-300 md:block">
    🇧🇩 KSI Bangladesh — Construction · Supplier · Digital Content · IT · AgriCare &nbsp;
    <router-link to="/contact" class="font-semibold text-primary underline underline-offset-2 hover:text-blue-400">Get in touch →</router-link>
  </div>

  <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-sm border-b border-slate-100 shadow-sm">
    <div class="mx-auto flex max-w-7xl items-center justify-between px-4 py-3 sm:px-6 lg:px-8">

      <!-- Logo -->
      <router-link to="/" class="select-none">
        <KSILogo />
      </router-link>

      <!-- Desktop nav -->
      <nav class="hidden items-center gap-1 lg:flex">

        <!-- 1. Home -->
        <router-link :to="{ name: 'Home' }" class="nav-link" :class="activeRoute('Home')">Home</router-link>

        <!-- 2. Business Unit dropdown -->
        <div ref="businessRef" class="relative">
          <button @click="toggleDropdown('business')" class="nav-link inline-flex items-center gap-1" :class="showBusiness ? 'text-primary' : ''">
            Business Unit
            <svg :class="showBusiness ? 'rotate-180' : ''" class="h-3.5 w-3.5 transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
            </svg>
          </button>
          <Transition enter-active-class="transition duration-150 ease-out" enter-from-class="opacity-0 translate-y-1" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-100 ease-in" leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-1">
            <div v-if="showBusiness" class="absolute left-0 top-full z-50 mt-2 min-w-[220px] rounded-2xl border border-slate-100 bg-white p-2 shadow-xl">
              <router-link v-for="item in businessUnits" :key="item.name" :to="item.link" @click="closeAll" class="flex items-center gap-2.5 rounded-xl px-4 py-2.5 text-sm font-medium text-slate-700 transition hover:bg-blue-50 hover:text-primary">
                <span class="text-base">{{ item.icon }}</span>{{ item.name }}
              </router-link>
            </div>
          </Transition>
        </div>

        <!-- 3. Sister Concern dropdown -->
        <div ref="sisterRef" class="relative">
          <button @click="toggleDropdown('sister')" class="nav-link inline-flex items-center gap-1" :class="showSister ? 'text-primary' : ''">
            Sister Concern
            <svg :class="showSister ? 'rotate-180' : ''" class="h-3.5 w-3.5 transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
            </svg>
          </button>
          <Transition enter-active-class="transition duration-150 ease-out" enter-from-class="opacity-0 translate-y-1" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-100 ease-in" leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-1">
            <div v-if="showSister" class="absolute left-0 top-full z-50 mt-2 min-w-[220px] rounded-2xl border border-slate-100 bg-white p-2 shadow-xl">
              <router-link v-for="item in sisterConcerns" :key="item.name" :to="item.link" @click="closeAll" class="flex items-center gap-2.5 rounded-xl px-4 py-2.5 text-sm font-medium text-slate-700 transition hover:bg-blue-50 hover:text-primary">
                <span class="text-base">{{ item.icon }}</span>{{ item.name }}
              </router-link>
            </div>
          </Transition>
        </div>

        <!-- 4. Management -->
        <router-link to="/management" class="nav-link" :class="activeRoute('Management')">Management</router-link>

        <!-- 5. Contact Us -->
        <router-link to="/contact" class="nav-link" :class="activeRoute('Contact')">Contact Us</router-link>

        <!-- 6. About Us -->
        <router-link to="/about" class="nav-link" :class="activeRoute('About')">About Us</router-link>

        <div class="ml-3 flex items-center gap-2">
          <template v-if="!isAuthenticated">
            <router-link to="/signup" class="btn btn-outline">Sign Up</router-link>
            <router-link to="/login" class="btn btn-primary">Login</router-link>
          </template>
          <template v-else>
            <router-link :to="dashboardLink" class="btn btn-primary">Dashboard</router-link>
          </template>
        </div>
      </nav>

      <!-- Mobile menu button -->
      <button class="inline-flex items-center gap-2 rounded-full border border-slate-200 bg-white px-3 py-2 text-sm font-medium text-slate-700 lg:hidden" @click="showMobile = !showMobile" aria-label="Toggle menu">
        <svg v-if="!showMobile" class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
        <svg v-else class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
        <span>{{ showMobile ? 'Close' : 'Menu' }}</span>
      </button>
    </div>

    <!-- Mobile menu -->
    <Transition enter-active-class="transition duration-200 ease-out" enter-from-class="opacity-0 -translate-y-2" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-150 ease-in" leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 -translate-y-2">
      <div v-if="showMobile" class="border-t border-slate-100 bg-white px-4 py-4 lg:hidden">
        <div class="space-y-1">
          <router-link to="/" @click="showMobile=false" class="mobile-link">Home</router-link>
        </div>

        <!-- Business Unit mobile -->
        <div class="mt-3 border-t border-slate-100 pt-3">
          <p class="mb-2 px-3 text-[10px] font-bold uppercase tracking-[0.2em] text-slate-400">Business Unit</p>
          <router-link v-for="item in businessUnits" :key="item.name" :to="item.link" @click="showMobile=false" class="flex items-center gap-2.5 rounded-xl px-3 py-2 text-sm font-medium text-slate-700 hover:bg-blue-50">
            <span>{{ item.icon }}</span>{{ item.name }}
          </router-link>
        </div>

        <!-- Sister Concern mobile -->
        <div class="mt-3 border-t border-slate-100 pt-3">
          <p class="mb-2 px-3 text-[10px] font-bold uppercase tracking-[0.2em] text-slate-400">Sister Concern</p>
          <router-link v-for="item in sisterConcerns" :key="item.name" :to="item.link" @click="showMobile=false" class="flex items-center gap-2.5 rounded-xl px-3 py-2 text-sm font-medium text-slate-700 hover:bg-blue-50">
            <span>{{ item.icon }}</span>{{ item.name }}
          </router-link>
        </div>

        <div class="mt-3 space-y-1 border-t border-slate-100 pt-3">
          <router-link to="/management" @click="showMobile=false" class="mobile-link">Management</router-link>
          <router-link to="/contact" @click="showMobile=false" class="mobile-link">Contact Us</router-link>
          <router-link to="/about" @click="showMobile=false" class="mobile-link">About Us</router-link>
        </div>

        <div class="mt-4 flex flex-col gap-2 border-t border-slate-100 pt-4">
          <template v-if="!isAuthenticated">
            <router-link to="/signup" @click="showMobile=false" class="btn btn-outline text-center">Sign Up</router-link>
            <router-link to="/login" @click="showMobile=false" class="btn btn-primary text-center">Login</router-link>
          </template>
          <template v-else>
            <router-link :to="dashboardLink" @click="showMobile=false" class="btn btn-primary text-center">Dashboard</router-link>
          </template>
        </div>
      </div>
    </Transition>
  </header>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRoute } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import KSILogo from './KSILogo.vue'

const showMobile = ref(false)
const showBusiness = ref(false)
const showSister = ref(false)
const businessRef = ref(null)
const sisterRef = ref(null)
const route = useRoute()
const authStore = useAuthStore()

const businessUnits = [
  { name: 'First Class Contractor', icon: '🏗️', link: '/business-unit/first-class-contractor' },
  { name: 'Supplier', icon: '📦', link: '/business-unit/supplier' },
  { name: 'IT & Technology', icon: '💻', link: '/business-unit/it' },
  { name: 'Digital Content', icon: '🎬', link: '/business-unit/digital-content' },
]

const sisterConcerns = [
  { name: 'KSI AgriCare', icon: '🌾', link: '/sister-concern/ksi-agricare' },
  { name: 'Kazi Corporation', icon: '🏢', link: '/sister-concern/kazi-corporation' },
]

const isAuthenticated = computed(() => authStore.isAuthenticated)
const dashboardLink = computed(() => (authStore.user?.role === 'admin' ? '/dashboard/admin' : '/dashboard/user'))
const activeRoute = (name) => route.name === name ? 'text-primary font-semibold' : ''

const toggleDropdown = (which) => {
  if (which === 'business') { showBusiness.value = !showBusiness.value; showSister.value = false }
  if (which === 'sister') { showSister.value = !showSister.value; showBusiness.value = false }
}

const closeAll = () => { showBusiness.value = false; showSister.value = false }

const handleOutsideClick = (e) => {
  if (businessRef.value && !businessRef.value.contains(e.target)) showBusiness.value = false
  if (sisterRef.value && !sisterRef.value.contains(e.target)) showSister.value = false
}

onMounted(() => document.addEventListener('click', handleOutsideClick))
onUnmounted(() => document.removeEventListener('click', handleOutsideClick))
</script>

<style scoped>
.nav-link { color: #475569; padding: 0.45rem 0.85rem; border-radius: 9999px; font-size: 0.875rem; font-weight: 500; transition: color 0.15s, background-color 0.15s; cursor: pointer; border: none; background: none; }
.nav-link:hover { color: #1A56DB; background-color: #EBF3FF; }
.mobile-link { display: block; border-radius: 0.75rem; padding: 0.5rem 0.75rem; font-size: 0.875rem; font-weight: 500; color: #475569; transition: background-color 0.15s; }
.mobile-link:hover { background-color: #f1f5f9; }
.btn { display: inline-flex; align-items: center; justify-content: center; border-radius: 9999px; padding: 0.55rem 1.2rem; font-size: 0.875rem; font-weight: 600; transition: all 0.15s; }
.btn-primary { background-color: #1A56DB; color: white; }
.btn-primary:hover { background-color: #1648c0; }
.btn-outline { border: 1.5px solid #1A56DB; color: #1A56DB; }
.btn-outline:hover { background-color: #EBF3FF; }
</style>
