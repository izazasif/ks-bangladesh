<template>
  <!-- Top announcement bar -->
  <div class="hidden bg-slate-900 px-4 py-2 text-center text-xs text-slate-300 md:block">
    🇧🇩 Serving Agriculture · IT · Construction · Transportation across Bangladesh &nbsp;
    <router-link to="/contact" class="font-semibold text-primary underline underline-offset-2 hover:text-blue-400">Get in touch →</router-link>
  </div>

  <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-sm border-b border-slate-100 shadow-sm">
    <div class="mx-auto flex max-w-7xl items-center justify-between px-4 py-3 sm:px-6 lg:px-8">

      <!-- Logo -->
      <router-link to="/" class="flex items-center gap-3 select-none">
        <svg width="46" height="46" viewBox="0 0 46 46" fill="none" xmlns="http://www.w3.org/2000/svg">
          <!-- Blue rounded square background -->
          <rect width="46" height="46" rx="12" fill="#1A56DB"/>
          <!-- White K letterform -->
          <rect x="11" y="9" width="5.5" height="28" rx="2.5" fill="white"/>
          <polygon points="16.5,23 23,23 37,9 30.5,9" fill="white"/>
          <polygon points="16.5,23 23,23 37,37 30.5,37" fill="white"/>
          <!-- Green accent dot — makes logo distinctive -->
          <circle cx="38.5" cy="37.5" r="4" fill="#22c55e"/>
        </svg>
        <div class="flex flex-col leading-none">
          <span class="text-[22px] font-black tracking-[-0.03em] text-slate-900">KSI</span>
          <span class="text-[9px] font-bold uppercase tracking-[0.28em] text-primary -mt-0.5">Bangladesh</span>
        </div>
      </router-link>

      <!-- Desktop nav -->
      <nav class="hidden items-center gap-1 md:flex">
        <router-link :to="{ name: 'Home' }" class="nav-link" :class="activeRoute('Home')">Home</router-link>
        <router-link to="/services" class="nav-link" :class="activeRoute('Services')">Services</router-link>

        <!-- Sectors dropdown — click based -->
        <div ref="sectorRef" class="relative">
          <button
            @click="showSectors = !showSectors"
            class="nav-link inline-flex items-center gap-1"
            :class="showSectors ? 'text-primary' : ''"
          >
            Sectors
            <svg
              :class="showSectors ? 'rotate-180' : ''"
              class="h-3.5 w-3.5 transition-transform duration-200"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2.5"
            >
              <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
            </svg>
          </button>

          <Transition
            enter-active-class="transition duration-150 ease-out"
            enter-from-class="opacity-0 translate-y-1"
            enter-to-class="opacity-100 translate-y-0"
            leave-active-class="transition duration-100 ease-in"
            leave-from-class="opacity-100 translate-y-0"
            leave-to-class="opacity-0 translate-y-1"
          >
            <div
              v-if="showSectors"
              class="absolute left-0 top-full z-50 mt-2 min-w-[200px] rounded-2xl border border-slate-100 bg-white p-2 shadow-xl"
            >
              <router-link
                v-for="sector in sectors"
                :key="sector.name"
                :to="sector.link"
                @click="showSectors = false"
                class="flex items-center gap-2.5 rounded-xl px-4 py-2.5 text-sm font-medium text-slate-700 transition hover:bg-lightblue hover:text-primary"
              >
                <span class="text-base">{{ sector.icon }}</span>
                {{ sector.name }}
              </router-link>
            </div>
          </Transition>
        </div>

        <router-link to="/contact" class="nav-link" :class="activeRoute('Contact')">Contact Us</router-link>
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
      <button
        class="inline-flex items-center gap-2 rounded-full border border-slate-200 bg-white px-3 py-2 text-sm font-medium text-slate-700 md:hidden"
        @click="showMobile = !showMobile"
        aria-label="Toggle menu"
      >
        <svg v-if="!showMobile" class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
        <svg v-else class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
        <span>{{ showMobile ? 'Close' : 'Menu' }}</span>
      </button>
    </div>

    <!-- Mobile menu -->
    <Transition
      enter-active-class="transition duration-200 ease-out"
      enter-from-class="opacity-0 -translate-y-2"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition duration-150 ease-in"
      leave-from-class="opacity-100 translate-y-0"
      leave-to-class="opacity-0 -translate-y-2"
    >
      <div v-if="showMobile" class="border-t border-slate-100 bg-white px-4 py-4 md:hidden">
        <div class="space-y-1">
          <router-link to="/" @click="showMobile=false" class="mobile-link">Home</router-link>
          <router-link to="/services" @click="showMobile=false" class="mobile-link">Services</router-link>
        </div>
        <div class="mt-3 border-t border-slate-100 pt-3">
          <p class="mb-2 px-3 text-[10px] font-bold uppercase tracking-[0.2em] text-slate-400">Sectors</p>
          <router-link
            v-for="sector in sectors"
            :key="sector.name"
            :to="sector.link"
            @click="showMobile=false"
            class="flex items-center gap-2.5 rounded-xl px-3 py-2 text-sm font-medium text-slate-700 hover:bg-lightblue"
          >
            <span>{{ sector.icon }}</span>{{ sector.name }}
          </router-link>
        </div>
        <div class="mt-3 space-y-1 border-t border-slate-100 pt-3">
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

const showMobile = ref(false)
const showSectors = ref(false)
const sectorRef = ref(null)
const route = useRoute()
const authStore = useAuthStore()

const sectors = [
  { name: 'Agriculture', icon: '🌾', link: '/sectors/agriculture' },
  { name: 'IT', icon: '💻', link: '/sectors/it' },
  { name: 'Construction', icon: '🏗️', link: '/sectors/construction' },
  { name: 'Transportation', icon: '🚛', link: '/sectors/transportation' },
]

const isAuthenticated = computed(() => authStore.isAuthenticated)
const dashboardLink = computed(() => (authStore.user?.role === 'admin' ? '/dashboard/admin' : '/dashboard/user'))
const activeRoute = (name) =>
  route.name === name ? 'text-primary font-semibold' : ''

const handleOutsideClick = (e) => {
  if (sectorRef.value && !sectorRef.value.contains(e.target)) {
    showSectors.value = false
  }
}

onMounted(() => document.addEventListener('click', handleOutsideClick))
onUnmounted(() => document.removeEventListener('click', handleOutsideClick))
</script>

<style scoped>
.nav-link {
  color: #475569;
  padding: 0.45rem 0.85rem;
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 500;
  transition: color 0.15s, background-color 0.15s;
  cursor: pointer;
  border: none;
  background: none;
}
.nav-link:hover {
  color: #1A56DB;
  background-color: #EBF3FF;
}
.mobile-link {
  display: block;
  border-radius: 0.75rem;
  padding: 0.5rem 0.75rem;
  font-size: 0.875rem;
  font-weight: 500;
  color: #475569;
  transition: background-color 0.15s;
}
.mobile-link:hover {
  background-color: #f1f5f9;
}
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 9999px;
  padding: 0.55rem 1.2rem;
  font-size: 0.875rem;
  font-weight: 600;
  transition: all 0.15s;
}
.btn-primary {
  background-color: #1A56DB;
  color: white;
}
.btn-primary:hover {
  background-color: #1648c0;
}
.btn-outline {
  border: 1.5px solid #1A56DB;
  color: #1A56DB;
}
.btn-outline:hover {
  background-color: #EBF3FF;
}
</style>
