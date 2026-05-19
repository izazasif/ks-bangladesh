<template>
  <div class="bg-slate-50 px-4 py-16 sm:px-6 lg:px-8">
    <div class="mx-auto grid max-w-7xl gap-8 lg:grid-cols-[300px_1fr]">
      <!-- Sidebar -->
      <aside class="space-y-4">
        <div class="rounded-[35px] bg-white p-8 shadow-soft">
          <div class="flex items-center gap-4">
            <div class="flex h-14 w-14 items-center justify-center rounded-2xl bg-primary/10 text-xl font-bold text-primary">
              {{ initials }}
            </div>
            <div>
              <h2 class="text-lg font-semibold text-slate-900">{{ user?.name }}</h2>
              <span class="mt-1 inline-block rounded-full bg-slate-100 px-3 py-0.5 text-xs font-medium text-slate-600">{{ user?.user_type }}</span>
            </div>
          </div>

          <div class="mt-6 space-y-3">
            <div class="rounded-2xl bg-slate-50 p-4">
              <p class="text-xs font-medium uppercase tracking-wider text-slate-400">Email</p>
              <p class="mt-1 text-sm font-medium text-slate-800 break-all">{{ user?.email }}</p>
            </div>
            <div class="rounded-2xl bg-slate-50 p-4">
              <p class="text-xs font-medium uppercase tracking-wider text-slate-400">Mobile</p>
              <p class="mt-1 text-sm font-medium text-slate-800">{{ user?.mobile }}</p>
            </div>
            <div class="rounded-2xl bg-slate-50 p-4">
              <p class="text-xs font-medium uppercase tracking-wider text-slate-400">Service Interest</p>
              <p class="mt-1 text-sm font-medium text-slate-800">{{ user?.service_interest }}</p>
            </div>
            <div class="rounded-2xl bg-slate-50 p-4">
              <p class="text-xs font-medium uppercase tracking-wider text-slate-400">Purpose</p>
              <p class="mt-1 text-sm text-slate-700 leading-relaxed">{{ user?.purpose }}</p>
            </div>
          </div>

          <div class="mt-6 space-y-3">
            <router-link
              to="/profile/edit"
              class="block w-full rounded-full border border-primary px-6 py-3 text-center text-sm font-semibold text-primary transition hover:bg-primary hover:text-white"
            >
              Edit Profile
            </router-link>
            <button
              @click="handleLogout"
              class="w-full rounded-full bg-slate-100 px-6 py-3 text-sm font-semibold text-slate-700 transition hover:bg-slate-200"
            >
              Logout
            </button>
          </div>
        </div>
      </aside>

      <!-- Main content -->
      <section class="space-y-8">
        <div class="rounded-[35px] bg-white p-8 shadow-soft">
          <div class="flex items-center justify-between">
            <div>
              <h2 class="text-2xl font-semibold text-slate-900">Your Submissions</h2>
              <p class="mt-2 text-sm text-slate-500">Messages you have sent through the contact form.</p>
            </div>
            <span class="rounded-full bg-primary/10 px-4 py-1.5 text-sm font-semibold text-primary">{{ submissions.length }}</span>
          </div>

          <div class="mt-6 space-y-4">
            <div v-if="loading" class="space-y-3">
              <div v-for="i in 3" :key="i" class="animate-pulse rounded-3xl bg-slate-100 p-6 h-24"></div>
            </div>
            <div
              v-else-if="submissions.length === 0"
              class="rounded-3xl border border-dashed border-slate-300 p-10 text-center"
            >
              <p class="text-slate-400">No submissions yet.</p>
              <router-link
                to="/contact"
                class="mt-4 inline-block rounded-full bg-primary px-5 py-2 text-sm font-semibold text-white"
              >
                Send a message
              </router-link>
            </div>
            <div v-else class="space-y-4">
              <div
                v-for="item in submissions"
                :key="item.id"
                class="rounded-3xl border border-slate-200 p-6 transition hover:border-primary/30 hover:shadow-sm"
              >
                <div class="flex flex-wrap items-center justify-between gap-3">
                  <p class="font-semibold text-slate-900">{{ item.subject }}</p>
                  <span class="rounded-full bg-primary/10 px-3 py-1 text-xs text-primary">
                    {{ new Date(item.created_at).toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' }) }}
                  </span>
                </div>
                <p class="mt-3 text-sm leading-relaxed text-slate-600">{{ item.message }}</p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { useAuthStore } from '../../stores/auth'
import apiClient from '../../api/client'
import { useToast } from '../../composables/useToast'

const authStore = useAuthStore()
const user = authStore.user
const submissions = ref([])
const loading = ref(false)
const { addToast } = useToast()

const initials = computed(() => {
  if (!user?.name) return '?'
  return user.name
    .split(' ')
    .slice(0, 2)
    .map((w) => w[0].toUpperCase())
    .join('')
})

const loadSubmissions = async () => {
  loading.value = true
  try {
    const response = await apiClient.get('/contact/me')
    submissions.value = response.data
  } catch {
    addToast('Unable to load your submissions.', 'error')
  } finally {
    loading.value = false
  }
}

const handleLogout = async () => {
  await authStore.logout()
}

onMounted(loadSubmissions)
</script>
