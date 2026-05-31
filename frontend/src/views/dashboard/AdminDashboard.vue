<template>
  <div class="bg-slate-50 px-4 py-16 sm:px-6 lg:px-8">
    <div class="mx-auto max-w-7xl space-y-8">

      <!-- Stats cards -->
      <div class="grid gap-6 md:grid-cols-3">
        <div class="rounded-[30px] bg-white p-6 shadow-soft">
          <p class="text-sm uppercase tracking-[0.3em] text-slate-500">Total Users</p>
          <p class="mt-4 text-4xl font-bold text-slate-900">{{ stats.total_users || 0 }}</p>
        </div>
        <div class="rounded-[30px] bg-white p-6 shadow-soft">
          <p class="text-sm uppercase tracking-[0.3em] text-slate-500">Total Contacts</p>
          <p class="mt-4 text-4xl font-bold text-slate-900">{{ stats.total_contacts || 0 }}</p>
        </div>
        <div class="rounded-[30px] bg-white p-6 shadow-soft">
          <p class="text-sm uppercase tracking-[0.3em] text-slate-500">Most Common Type</p>
          <p class="mt-4 text-2xl font-bold text-slate-900">{{ dominantType }}</p>
          <p class="mt-1 text-sm text-slate-500">{{ dominantCount }} users</p>
        </div>
      </div>

      <!-- User distribution chart -->
      <div v-if="hasChartData" class="rounded-[35px] bg-white p-8 shadow-soft">
        <h2 class="text-2xl font-semibold text-slate-900">User Distribution</h2>
        <p class="mt-2 text-sm text-slate-500">Breakdown of registered users by account type</p>
        <div class="mt-8 space-y-5">
          <div
            v-for="(count, type) in stats.users_by_type"
            :key="type"
            class="flex items-center gap-4"
          >
            <span class="w-28 flex-shrink-0 text-sm font-medium text-slate-700">{{ type }}</span>
            <div class="flex-1 rounded-full bg-slate-100 h-3 overflow-hidden">
              <div
                class="h-3 rounded-full bg-primary transition-all duration-700"
                :style="{ width: getPercent(count) + '%' }"
              ></div>
            </div>
            <span class="w-8 text-right text-sm font-bold text-slate-900">{{ count }}</span>
            <span class="w-12 text-right text-xs text-slate-400">{{ getPercent(count) }}%</span>
          </div>
        </div>
      </div>

      <!-- Users table -->
      <div class="rounded-[35px] bg-white p-8 shadow-soft">
        <div class="flex flex-col gap-4 md:flex-row md:items-start md:justify-between">
          <div>
            <h2 class="text-2xl font-semibold text-slate-900">Registered Users</h2>
            <p class="mt-2 text-sm text-slate-500">Review and manage users registered on the platform.</p>
          </div>
          <div class="flex flex-wrap gap-3">
            <input
              v-model="search"
              type="text"
              placeholder="Search by name or email"
              class="input-field w-56"
            />
            <select v-model="selectedType" class="input-field w-40">
              <option value="">All types</option>
              <option value="Individual">Individual</option>
              <option value="Business">Business</option>
              <option value="Government">Government</option>
              <option value="NGO">NGO</option>
            </select>
            <button
              @click="exportUsersCSV"
              class="rounded-full border border-primary px-4 py-2 text-sm font-semibold text-primary transition hover:bg-primary hover:text-white"
            >
              Export CSV
            </button>
          </div>
        </div>

        <div class="mt-6 overflow-x-auto">
          <table class="min-w-full text-left text-sm text-slate-700">
            <thead class="border-b border-slate-200 text-xs font-semibold uppercase tracking-wider text-slate-500">
              <tr>
                <th class="py-4 pr-6">Name</th>
                <th class="py-4 pr-6">Email</th>
                <th class="py-4 pr-6">Mobile</th>
                <th class="py-4 pr-6">User Type</th>
                <th class="py-4 pr-6">Service Interest</th>
                <th class="py-4 pr-6">Registered</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100">
              <tr
                v-for="user in filteredUsers"
                :key="user.id"
                class="transition hover:bg-slate-50"
              >
                <td class="py-4 pr-6 font-medium text-slate-900">{{ user.name }}</td>
                <td class="py-4 pr-6 text-slate-600">{{ user.email }}</td>
                <td class="py-4 pr-6 text-slate-600">{{ user.mobile }}</td>
                <td class="py-4 pr-6">
                  <span :class="typeColor(user.user_type)" class="rounded-full px-3 py-0.5 text-xs font-semibold">
                    {{ user.user_type }}
                  </span>
                </td>
                <td class="py-4 pr-6 text-slate-600">{{ user.service_interest }}</td>
                <td class="py-4 pr-6 text-slate-500">{{ fmtDate(user.created_at) }}</td>
              </tr>
            </tbody>
          </table>
          <div
            v-if="filteredUsers.length === 0"
            class="mt-6 rounded-3xl border border-dashed border-slate-300 p-6 text-center text-slate-500"
          >
            No matching users found.
          </div>
        </div>

        <!-- Users pagination -->
        <div class="mt-6 flex items-center justify-between border-t border-slate-100 pt-5">
          <p class="text-sm text-slate-500">
            Page {{ userPage }} &middot; showing {{ users.length }} users
          </p>
          <div class="flex gap-2">
            <button
              :disabled="userPage === 1"
              @click="prevUserPage"
              class="rounded-full border border-slate-200 px-4 py-2 text-sm font-medium text-slate-600 transition hover:border-primary hover:text-primary disabled:opacity-30"
            >
              &larr; Prev
            </button>
            <button
              :disabled="!hasMoreUsers"
              @click="nextUserPage"
              class="rounded-full border border-slate-200 px-4 py-2 text-sm font-medium text-slate-600 transition hover:border-primary hover:text-primary disabled:opacity-30"
            >
              Next &rarr;
            </button>
          </div>
        </div>
      </div>

      <!-- SEO Panel -->
      <div class="rounded-[35px] bg-white p-8 shadow-soft">
        <div class="flex items-start justify-between">
          <div>
            <h2 class="text-2xl font-semibold text-slate-900">SEO Health</h2>
            <p class="mt-2 text-sm text-slate-500">Search engine optimization status for ks-bangladesh.vercel.app</p>
          </div>
          <span class="rounded-full bg-emerald-100 px-4 py-1.5 text-xs font-bold text-emerald-700">All Systems OK</span>
        </div>

        <!-- Checklist -->
        <div class="mt-6 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
          <div v-for="item in seoChecklist" :key="item.label" class="flex items-start gap-3 rounded-2xl border border-slate-100 bg-slate-50 px-4 py-3.5">
            <span :class="item.ok ? 'bg-emerald-100 text-emerald-600' : 'bg-red-100 text-red-500'" class="flex h-6 w-6 flex-shrink-0 items-center justify-center rounded-full text-xs font-bold">
              {{ item.ok ? '✓' : '✗' }}
            </span>
            <div>
              <p class="text-sm font-semibold text-slate-800">{{ item.label }}</p>
              <p class="mt-0.5 text-xs text-slate-500">{{ item.desc }}</p>
            </div>
          </div>
        </div>

        <!-- Google Search Preview -->
        <div class="mt-8">
          <p class="mb-3 text-xs font-bold uppercase tracking-[0.2em] text-slate-400">Google Search Preview — Home Page</p>
          <div class="rounded-2xl border border-slate-200 bg-white p-5 font-sans shadow-sm">
            <p class="text-xs text-slate-500">https://ks-bangladesh.vercel.app</p>
            <p class="mt-1 text-lg font-medium leading-snug text-[#1a0dab] hover:underline cursor-pointer">
              KSI Bangladesh | Agriculture · IT · Construction · Transportation
            </p>
            <p class="mt-1 text-sm leading-relaxed text-slate-600">
              KSI Bangladesh is a multi-sector company driving Agriculture, IT, Construction, and Transportation growth across Bangladesh since 2010.
            </p>
          </div>
        </div>

        <!-- Page Meta Table -->
        <div class="mt-8">
          <p class="mb-4 text-xs font-bold uppercase tracking-[0.2em] text-slate-400">Page Meta Titles & Descriptions</p>
          <div class="overflow-x-auto">
            <table class="min-w-full text-left text-sm">
              <thead class="border-b border-slate-200 text-xs font-semibold uppercase tracking-wider text-slate-500">
                <tr>
                  <th class="py-3 pr-6">Page</th>
                  <th class="py-3 pr-6">Meta Title</th>
                  <th class="py-3">Meta Description</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100">
                <tr v-for="page in seoPages" :key="page.path" class="hover:bg-slate-50">
                  <td class="py-3 pr-6 font-medium text-primary">{{ page.path }}</td>
                  <td class="py-3 pr-6 text-slate-700">{{ page.title }}</td>
                  <td class="py-3 max-w-xs text-slate-500 text-xs">{{ page.desc }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Contacts table -->
      <div class="rounded-[35px] bg-white p-8 shadow-soft">
        <div class="flex flex-col gap-4 md:flex-row md:items-start md:justify-between">
          <div>
            <h2 class="text-2xl font-semibold text-slate-900">Contact Submissions</h2>
            <p class="mt-2 text-sm text-slate-500">Messages submitted through the contact form.</p>
          </div>
          <button
            @click="exportContactsCSV"
            class="self-start rounded-full border border-primary px-4 py-2 text-sm font-semibold text-primary transition hover:bg-primary hover:text-white"
          >
            Export CSV
          </button>
        </div>

        <div class="mt-6 overflow-x-auto">
          <table class="min-w-full text-left text-sm text-slate-700">
            <thead class="border-b border-slate-200 text-xs font-semibold uppercase tracking-wider text-slate-500">
              <tr>
                <th class="py-4 pr-6">Name</th>
                <th class="py-4 pr-6">Email</th>
                <th class="py-4 pr-6">Subject</th>
                <th class="py-4 pr-6">Message</th>
                <th class="py-4 pr-6">Date</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100">
              <tr
                v-for="item in contactSubmissions"
                :key="item.id"
                class="transition hover:bg-slate-50"
              >
                <td class="py-4 pr-6 font-medium text-slate-900">{{ item.name }}</td>
                <td class="py-4 pr-6 text-slate-600">{{ item.email }}</td>
                <td class="py-4 pr-6 text-slate-700">{{ item.subject }}</td>
                <td class="py-4 pr-6 max-w-xs text-slate-500">
                  {{ item.message.length > 80 ? item.message.slice(0, 80) + '…' : item.message }}
                </td>
                <td class="py-4 pr-6 text-slate-500 whitespace-nowrap">{{ fmtDate(item.created_at) }}</td>
              </tr>
            </tbody>
          </table>
          <div
            v-if="contactSubmissions.length === 0"
            class="mt-6 rounded-3xl border border-dashed border-slate-300 p-6 text-center text-slate-500"
          >
            No submissions yet.
          </div>
        </div>

        <!-- Contacts pagination -->
        <div class="mt-6 flex items-center justify-between border-t border-slate-100 pt-5">
          <p class="text-sm text-slate-500">
            Page {{ contactPage }} &middot; showing {{ contactSubmissions.length }} submissions
          </p>
          <div class="flex gap-2">
            <button
              :disabled="contactPage === 1"
              @click="prevContactPage"
              class="rounded-full border border-slate-200 px-4 py-2 text-sm font-medium text-slate-600 transition hover:border-primary hover:text-primary disabled:opacity-30"
            >
              &larr; Prev
            </button>
            <button
              :disabled="!hasMoreContacts"
              @click="nextContactPage"
              class="rounded-full border border-slate-200 px-4 py-2 text-sm font-medium text-slate-600 transition hover:border-primary hover:text-primary disabled:opacity-30"
            >
              Next &rarr;
            </button>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { getStats, getUsers, getContacts } from '../../api/admin'
import { useToast } from '../../composables/useToast'
import { useSEO } from '../../composables/useSEO'

useSEO({ title: 'Admin Dashboard', path: '/dashboard/admin' })

const LIMIT = 20

const stats = ref({ total_users: 0, total_contacts: 0, users_by_type: {} })
const users = ref([])
const contactSubmissions = ref([])
const search = ref('')
const selectedType = ref('')
const userPage = ref(1)
const contactPage = ref(1)
const hasMoreUsers = ref(false)
const hasMoreContacts = ref(false)
const { addToast } = useToast()

const hasChartData = computed(() => Object.keys(stats.value.users_by_type || {}).length > 0)

const totalUsersForChart = computed(() =>
  Object.values(stats.value.users_by_type || {}).reduce((a, b) => a + b, 0),
)

const dominantType = computed(() => {
  const types = stats.value.users_by_type || {}
  return Object.keys(types).sort((a, b) => types[b] - types[a])[0] ?? '—'
})

const dominantCount = computed(() => stats.value.users_by_type?.[dominantType.value] ?? 0)

const getPercent = (count) => {
  const total = totalUsersForChart.value
  return total > 0 ? Math.round((count / total) * 100) : 0
}

const typeColor = (type) => {
  const map = {
    Individual: 'bg-blue-100 text-blue-700',
    Business: 'bg-emerald-100 text-emerald-700',
    Government: 'bg-purple-100 text-purple-700',
    NGO: 'bg-amber-100 text-amber-700',
  }
  return map[type] || 'bg-slate-100 text-slate-700'
}

const fmtDate = (val) =>
  new Date(val).toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' })

const loadStats = async () => {
  try {
    const res = await getStats()
    stats.value = res.data
  } catch {
    addToast('Unable to load statistics.', 'error')
  }
}

const loadUsers = async () => {
  try {
    const res = await getUsers({ limit: LIMIT, skip: (userPage.value - 1) * LIMIT })
    users.value = res.data
    hasMoreUsers.value = res.data.length === LIMIT
  } catch {
    addToast('Unable to load users.', 'error')
  }
}

const loadContacts = async () => {
  try {
    const res = await getContacts({ limit: LIMIT, skip: (contactPage.value - 1) * LIMIT })
    contactSubmissions.value = res.data
    hasMoreContacts.value = res.data.length === LIMIT
  } catch {
    addToast('Unable to load contact submissions.', 'error')
  }
}

const nextUserPage = async () => { userPage.value++; await loadUsers() }
const prevUserPage = async () => { userPage.value--; await loadUsers() }
const nextContactPage = async () => { contactPage.value++; await loadContacts() }
const prevContactPage = async () => { contactPage.value--; await loadContacts() }

const filteredUsers = computed(() =>
  users.value.filter((u) => {
    const q = search.value.trim().toLowerCase()
    const matchesSearch = !q || u.name.toLowerCase().includes(q) || u.email.toLowerCase().includes(q)
    const matchesType = !selectedType.value || u.user_type === selectedType.value
    return matchesSearch && matchesType
  }),
)

const downloadCSV = (headers, rows, filename) => {
  const lines = [
    headers.join(','),
    ...rows.map((row) =>
      headers.map((h) => `"${String(row[h] ?? '').replace(/"/g, '""')}"`).join(','),
    ),
  ]
  const blob = new Blob([lines.join('\n')], { type: 'text/csv;charset=utf-8;' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = filename
  a.click()
  URL.revokeObjectURL(url)
}

const exportUsersCSV = () => {
  const rows = users.value.map((u) => ({
    name: u.name,
    email: u.email,
    mobile: u.mobile,
    user_type: u.user_type,
    service_interest: u.service_interest,
    created_at: fmtDate(u.created_at),
  }))
  downloadCSV(['name', 'email', 'mobile', 'user_type', 'service_interest', 'created_at'], rows, 'ksi-users.csv')
}

const exportContactsCSV = () => {
  const rows = contactSubmissions.value.map((c) => ({
    name: c.name,
    email: c.email,
    subject: c.subject,
    message: c.message,
    created_at: fmtDate(c.created_at),
  }))
  downloadCSV(['name', 'email', 'subject', 'message', 'created_at'], rows, 'ksi-contacts.csv')
}

const seoChecklist = [
  { label: 'robots.txt', desc: 'Tells crawlers which pages to index', ok: true },
  { label: 'sitemap.xml', desc: 'Lists all public URLs for search engines', ok: true },
  { label: 'Meta Description', desc: 'Unique descriptions on every page', ok: true },
  { label: 'Open Graph Tags', desc: 'og:title, og:description, og:image set', ok: true },
  { label: 'Twitter Card', desc: 'summary_large_image card configured', ok: true },
  { label: 'Canonical URL', desc: 'Prevents duplicate content issues', ok: true },
  { label: 'JSON-LD Schema', desc: 'Organization schema in index.html', ok: true },
  { label: 'Keywords Meta', desc: 'Per-page keyword meta tags', ok: true },
  { label: 'Responsive Design', desc: 'Mobile-friendly layout (Google ranks mobile)', ok: true },
]

const seoPages = [
  { path: '/', title: 'Multi-Sector Company in Bangladesh | KSI Bangladesh', desc: 'KSI Bangladesh delivers expert services in 5 sectors since 2010...' },
  { path: '/about', title: 'About Us | KSI Bangladesh', desc: 'Learn about KSI Bangladesh — our history, mission, team and values...' },
  { path: '/services', title: 'Our Services | KSI Bangladesh', desc: 'Explore KSI Bangladesh\'s full range of services across five sectors...' },
  { path: '/contact', title: 'Contact Us | KSI Bangladesh', desc: 'Get in touch for project inquiries, consultations or partnership...' },
  { path: '/sectors/construction', title: 'Construction Services | KSI Bangladesh', desc: 'Civil engineering, infrastructure, project management and safety compliance...' },
  { path: '/sectors/supplier', title: 'Supplier & Procurement | KSI Bangladesh', desc: 'Strategic procurement, vendor management and materials supply...' },
  { path: '/sectors/digital-content', title: 'Digital Content Services | KSI Bangladesh', desc: 'Content creation, social media management, video production and branding...' },
  { path: '/sectors/it', title: 'IT & Technology Services | KSI Bangladesh', desc: 'Software development, cloud solutions, cybersecurity, digital transformation...' },
  { path: '/sectors/agriculture', title: 'Agriculture Services | KSI Bangladesh', desc: 'Crop management, irrigation, agri-tech and farmer support programs...' },
]

onMounted(async () => {
  await Promise.all([loadStats(), loadUsers(), loadContacts()])
})
</script>

<style scoped>
.input-field {
  border: 1px solid #cbd5e1;
  border-radius: 1rem;
  padding: 0.6rem 1rem;
  background: #f8fafc;
  font-size: 0.875rem;
}
.input-field:focus {
  outline: none;
  border-color: #3b82f6;
}
</style>
