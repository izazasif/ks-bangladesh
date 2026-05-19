<template>
  <div class="flex min-h-[calc(100vh-56px)]">

    <!-- Left brand panel -->
    <div class="relative hidden w-[45%] overflow-hidden lg:flex">
      <img
        src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1200&q=80"
        alt=""
        class="h-full w-full object-cover"
      />
      <div class="absolute inset-0 bg-primary/88"></div>
      <div class="relative flex flex-col justify-between p-12 text-white">
        <router-link to="/" class="flex items-center gap-3">
          <svg width="40" height="40" viewBox="0 0 46 46" fill="none">
            <rect width="46" height="46" rx="12" fill="white" fill-opacity="0.2"/>
            <rect x="11" y="9" width="5.5" height="28" rx="2.5" fill="white"/>
            <polygon points="16.5,23 23,23 37,9 30.5,9" fill="white"/>
            <polygon points="16.5,23 23,23 37,37 30.5,37" fill="white"/>
          </svg>
          <div>
            <p class="text-xl font-black tracking-tight">KSI</p>
            <p class="text-[9px] font-bold uppercase tracking-[0.3em] text-blue-200">Bangladesh</p>
          </div>
        </router-link>

        <div>
          <h2 class="text-4xl font-extrabold leading-tight">Welcome back to KSI Bangladesh</h2>
          <p class="mt-4 text-lg text-blue-100">Access your dashboard and manage your projects across four key sectors.</p>
          <div class="mt-10 space-y-4">
            <div v-for="b in benefits" :key="b" class="flex items-center gap-3">
              <div class="flex h-7 w-7 flex-shrink-0 items-center justify-center rounded-full bg-white/20 text-sm">✓</div>
              <span class="text-sm text-blue-100">{{ b }}</span>
            </div>
          </div>
        </div>

        <p class="text-sm text-blue-300">© 2025 KSI Bangladesh. All rights reserved.</p>
      </div>
    </div>

    <!-- Right form panel -->
    <div class="flex flex-1 items-center justify-center bg-slate-50 px-6 py-16 lg:px-16">
      <div class="w-full max-w-md">
        <div class="mb-8">
          <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Welcome Back</p>
          <h1 class="mt-3 text-3xl font-extrabold text-slate-900">Log in to your account</h1>
          <p class="mt-2 text-slate-500">Enter your credentials to access your dashboard.</p>
        </div>

        <div class="rounded-[28px] bg-white p-8 shadow-soft">
          <form @submit.prevent="handleSubmit" class="space-y-5" novalidate>
            <div>
              <label class="field-label">Email Address</label>
              <input v-model="form.email" type="email" class="input-field" placeholder="you@example.com" required />
            </div>
            <div>
              <label class="field-label">Password</label>
              <input v-model="form.password" type="password" class="input-field" placeholder="••••••••" required minlength="8" />
            </div>
            <div class="flex items-center justify-between">
              <label class="flex items-center gap-2 text-sm text-slate-600 cursor-pointer">
                <input v-model="rememberMe" type="checkbox" class="h-4 w-4 rounded border-slate-300 accent-primary" />
                Remember me
              </label>
            </div>

            <div v-if="errorMsg" class="rounded-xl border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
              {{ errorMsg }}
            </div>

            <button
              type="submit"
              :disabled="loading"
              class="w-full rounded-full bg-primary py-3.5 text-sm font-bold text-white shadow-md transition hover:bg-blue-700 disabled:opacity-50"
            >
              {{ loading ? 'Logging in…' : 'Log In' }}
            </button>
          </form>
        </div>

        <p class="mt-6 text-center text-sm text-slate-500">
          Don't have an account?
          <router-link to="/signup" class="font-semibold text-primary hover:underline">Create one →</router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { useToast } from '../composables/useToast'

const authStore = useAuthStore()
const router = useRouter()
const route = useRoute()
const { addToast } = useToast()
const loading = ref(false)
const rememberMe = ref(false)
const errorMsg = ref('')
const form = ref({ email: '', password: '' })

const benefits = [
  'View and manage your contact submissions',
  'Track project inquiries across all sectors',
  'Update your profile and preferences',
  'Access exclusive partner resources',
]

const handleSubmit = async () => {
  errorMsg.value = ''
  loading.value = true
  try {
    await authStore.login(form.value)
    addToast('Logged in successfully.')
    const redirect = route.query.redirect || (authStore.user?.role === 'admin' ? '/dashboard/admin' : '/dashboard/user')
    await router.push(redirect)
  } catch {
    errorMsg.value = 'Login failed. Please check your email and password.'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.field-label { display: block; font-size: 0.875rem; font-weight: 500; color: #475569; margin-bottom: 0.4rem; }
.input-field { width: 100%; border: 1px solid #cbd5e1; border-radius: 1rem; padding: 0.85rem 1.1rem; background: #f8fafc; font-size: 0.875rem; transition: border-color 0.15s, box-shadow 0.15s; }
.input-field:focus { outline: none; border-color: #1a56db; box-shadow: 0 0 0 3px rgba(26,86,219,0.1); }
</style>
