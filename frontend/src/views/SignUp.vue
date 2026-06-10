<template>
  <div class="flex min-h-[calc(100vh-56px)]">

    <!-- Left brand panel -->
    <div class="relative hidden w-[40%] overflow-hidden lg:flex">
      <img
        src="https://images.unsplash.com/photo-1600880292203-757bb62b4baf?auto=format&fit=crop&w=1200&q=80"
        alt=""
        class="h-full w-full object-cover"
      />
      <div class="absolute inset-0 bg-slate-950/80"></div>
      <div class="relative flex flex-col justify-between p-12 text-white">
        <router-link to="/"><KSILogo :dark="true" :size="40" /></router-link>

        <div>
          <h2 class="text-4xl font-extrabold leading-tight">Join KSI Bangladesh today</h2>
          <p class="mt-4 text-lg text-slate-300">Create your account to access multi-sector services and project support.</p>
          <div class="mt-10 grid grid-cols-2 gap-4">
            <div v-for="s in sectors" :key="s.name" class="rounded-2xl border border-white/10 bg-white/10 p-4 backdrop-blur-sm">
              <span class="text-2xl">{{ s.icon }}</span>
              <p class="mt-2 text-sm font-semibold text-white">{{ s.name }}</p>
              <p class="mt-1 text-xs text-slate-400">{{ s.desc }}</p>
            </div>
          </div>
        </div>

        <p class="text-sm text-slate-500">© 2025 KSI Bangladesh. All rights reserved.</p>
      </div>
    </div>

    <!-- Right form panel -->
    <div class="flex flex-1 items-start justify-center overflow-y-auto bg-slate-50 px-6 py-12 lg:px-12">
      <div class="w-full max-w-lg">
        <div class="mb-8">
          <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Get Started</p>
          <h1 class="mt-3 text-3xl font-extrabold text-slate-900">Create your account</h1>
          <p class="mt-2 text-slate-500">Register with KSI Bangladesh for services and project consultations.</p>
        </div>

        <div class="rounded-[28px] bg-white p-8 shadow-soft">
          <form @submit.prevent="handleSubmit" class="space-y-5" novalidate>
            <div class="grid gap-4 sm:grid-cols-2">
              <div>
                <label class="field-label">Full Name</label>
                <input v-model="form.name" type="text" class="input-field" placeholder="Your full name" required maxlength="100" />
              </div>
              <div>
                <label class="field-label">Mobile Number</label>
                <input v-model="form.mobile" type="tel" class="input-field" placeholder="01XXXXXXXXX" required maxlength="20" />
              </div>
            </div>

            <div>
              <label class="field-label">Email Address</label>
              <input v-model="form.email" type="email" class="input-field" placeholder="you@example.com" required />
            </div>

            <div>
              <label class="field-label">Password</label>
              <input v-model="form.password" type="password" class="input-field" placeholder="Min. 8 chars, 1 uppercase, 1 number" required minlength="8" />
            </div>

            <div>
              <label class="field-label">Purpose / Description</label>
              <textarea v-model="form.purpose" rows="3" class="input-field resize-none" placeholder="Briefly describe your purpose" required maxlength="250"></textarea>
            </div>

            <div class="grid gap-4 sm:grid-cols-2">
              <div>
                <label class="field-label">Service Interest</label>
                <select v-model="form.service_interest" class="input-field" required>
                  <option disabled value="">Select one</option>
                  <option>First Class Contractor</option>
                  <option>Supplier</option>
                  <option>Digital Content</option>
                  <option>IT</option>
                  <option>Agriculture</option>
                  <option>Multiple</option>
                </select>
              </div>
              <div>
                <label class="field-label">User Type</label>
                <select v-model="form.user_type" class="input-field" required>
                  <option disabled value="">Select one</option>
                  <option>Individual</option>
                  <option>Business</option>
                  <option>Government</option>
                  <option>NGO</option>
                </select>
              </div>
            </div>

            <div v-if="errorMsg" class="rounded-xl border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">{{ errorMsg }}</div>
            <div v-if="successMsg" class="rounded-xl border border-green-200 bg-green-50 px-4 py-3 text-sm text-green-700">{{ successMsg }}</div>

            <button
              type="submit"
              :disabled="sending"
              class="w-full rounded-full bg-primary py-3.5 text-sm font-bold text-white shadow-md transition hover:bg-blue-700 disabled:opacity-50"
            >
              {{ sending ? 'Creating account…' : 'Create Account' }}
            </button>
          </form>
        </div>

        <p class="mt-6 text-center text-sm text-slate-500">
          Already have an account?
          <router-link to="/login" class="font-semibold text-primary hover:underline">Log in →</router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { register } from '../api/auth'
import { useToast } from '../composables/useToast'
import KSILogo from '../components/KSILogo.vue'

const { addToast } = useToast()
const sending = ref(false)
const errorMsg = ref('')
const successMsg = ref('')

const sectors = [
  { icon: '🌾', name: 'Agriculture', desc: 'Crop, irrigation & agri-tech' },
  { icon: '💻', name: 'IT', desc: 'Software & cloud solutions' },
  { icon: '🏗️', name: 'First Class Contractor', desc: 'Civil & infrastructure' },
  { icon: '📦', name: 'Supplier', desc: 'Health equipment & more' },
]

const form = ref({ name: '', mobile: '', email: '', password: '', purpose: '', service_interest: '', user_type: '' })

const handleSubmit = async () => {
  errorMsg.value = ''
  successMsg.value = ''
  sending.value = true
  try {
    await register(form.value)
    successMsg.value = 'Account created! Please log in.'
    addToast('Registration successful. Please log in.')
    form.value = { name: '', mobile: '', email: '', password: '', purpose: '', service_interest: '', user_type: '' }
  } catch (err) {
    const detail = err.response?.data?.detail
    errorMsg.value = Array.isArray(detail) ? detail.map(e => e.msg).join(' ') : (detail || 'Registration failed. Please try again.')
  } finally {
    sending.value = false
  }
}
</script>

<style scoped>
.field-label { display: block; font-size: 0.875rem; font-weight: 500; color: #475569; margin-bottom: 0.4rem; }
.input-field { width: 100%; border: 1px solid #cbd5e1; border-radius: 1rem; padding: 0.85rem 1.1rem; background: #f8fafc; font-size: 0.875rem; transition: border-color 0.15s, box-shadow 0.15s; }
.input-field:focus { outline: none; border-color: #1a56db; box-shadow: 0 0 0 3px rgba(26,86,219,0.1); }
</style>
