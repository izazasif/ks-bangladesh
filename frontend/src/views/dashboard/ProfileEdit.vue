<template>
  <div class="bg-slate-50 px-4 py-16 sm:px-6 lg:px-8">
    <div class="mx-auto max-w-2xl">
      <div class="rounded-[35px] bg-white p-10 shadow-soft">
        <div class="flex items-center gap-4">
          <button
            @click="router.push('/dashboard/user')"
            class="flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-full border border-slate-200 text-slate-600 transition hover:bg-slate-50"
            aria-label="Go back"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
            </svg>
          </button>
          <div>
            <h1 class="text-2xl font-semibold text-slate-900">Edit Profile</h1>
            <p class="mt-1 text-sm text-slate-500">Update your account information below</p>
          </div>
        </div>

        <form @submit.prevent="handleSubmit" class="mt-8 space-y-5" novalidate>
          <div>
            <label class="field-label">Full Name</label>
            <input
              v-model="form.name"
              type="text"
              class="input-field"
              placeholder="Your full name"
              required
              maxlength="100"
            />
          </div>

          <div>
            <label class="field-label">Mobile Number</label>
            <input
              v-model="form.mobile"
              type="text"
              class="input-field"
              placeholder="01XXXXXXXXX or +880XXXXXXXXXX"
              required
            />
            <p class="mt-1 text-xs text-slate-400">Format: 01XXXXXXXXX (11 digits) or +880XXXXXXXXXX</p>
          </div>

          <div>
            <label class="field-label">Purpose / Description</label>
            <textarea
              v-model="form.purpose"
              class="input-field resize-none"
              rows="3"
              placeholder="Briefly describe your purpose for using KSI Bangladesh services"
              required
              maxlength="250"
            ></textarea>
            <p class="mt-1 text-right text-xs text-slate-400">{{ form.purpose.length }}/250</p>
          </div>

          <div>
            <label class="field-label">Service Interest</label>
            <select v-model="form.service_interest" class="input-field" required>
              <option value="First Class Contractor">First Class Contractor</option>
              <option value="Supplier">Supplier</option>
              <option value="Digital Content">Digital Content</option>
              <option value="IT">IT</option>
              <option value="Agriculture">Agriculture</option>
              <option value="Multiple">Multiple</option>
            </select>
          </div>

          <div>
            <label class="field-label">User Type</label>
            <select v-model="form.user_type" class="input-field" required>
              <option value="Individual">Individual</option>
              <option value="Business">Business</option>
              <option value="Government">Government</option>
              <option value="NGO">NGO</option>
            </select>
          </div>

          <div v-if="errorMsg" class="rounded-2xl border border-red-200 bg-red-50 px-5 py-4 text-sm text-red-700">
            {{ errorMsg }}
          </div>

          <div class="flex gap-3 pt-2">
            <button
              type="button"
              @click="router.push('/dashboard/user')"
              class="flex-1 rounded-full border border-slate-300 px-6 py-3 text-sm font-semibold text-slate-700 transition hover:bg-slate-50"
            >
              Cancel
            </button>
            <button
              type="submit"
              :disabled="saving"
              class="flex-1 rounded-full bg-primary px-6 py-3 text-sm font-semibold text-white transition hover:opacity-90 disabled:opacity-50"
            >
              {{ saving ? 'Saving…' : 'Save Changes' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../../stores/auth'
import { useToast } from '../../composables/useToast'
import apiClient from '../../api/client'

const router = useRouter()
const authStore = useAuthStore()
const { addToast } = useToast()

const user = authStore.user
const saving = ref(false)
const errorMsg = ref('')

const form = ref({
  name: user?.name ?? '',
  mobile: user?.mobile ?? '',
  purpose: user?.purpose ?? '',
  service_interest: user?.service_interest ?? 'Agriculture',
  user_type: user?.user_type ?? 'Individual',
})

const handleSubmit = async () => {
  errorMsg.value = ''
  saving.value = true
  try {
    await apiClient.put(`/users/${user.id}`, form.value)
    await authStore.loadProfile()
    addToast('Profile updated successfully.', 'success')
    router.push('/dashboard/user')
  } catch (err) {
    const detail = err.response?.data?.detail
    if (Array.isArray(detail)) {
      errorMsg.value = detail.map((e) => e.msg).join(' ')
    } else if (typeof detail === 'string') {
      errorMsg.value = detail
    } else {
      errorMsg.value = 'Failed to update profile. Please check your inputs.'
    }
  } finally {
    saving.value = false
  }
}
</script>

<style scoped>
.field-label {
  display: block;
  font-size: 0.875rem;
  font-weight: 500;
  color: #475569;
  margin-bottom: 0.4rem;
}
.input-field {
  width: 100%;
  border: 1px solid #cbd5e1;
  border-radius: 1rem;
  padding: 0.85rem 1rem;
  background: #f8fafc;
  font-size: 0.875rem;
  color: #0f172a;
  transition: border-color 0.15s, box-shadow 0.15s;
}
.input-field:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}
</style>
