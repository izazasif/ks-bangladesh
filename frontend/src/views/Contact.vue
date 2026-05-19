<template>
  <div>
    <!-- Hero -->
    <section class="relative overflow-hidden">
      <img
        src="https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=1600&q=80"
        alt="Contact KSI Bangladesh"
        class="h-64 w-full object-cover md:h-80"
        loading="eager"
      />
      <div class="absolute inset-0 bg-gradient-to-r from-slate-950/90 via-slate-950/60 to-transparent"></div>
      <div class="absolute inset-0 flex flex-col justify-center px-6 sm:px-12 lg:px-20">
        <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Reach Us</p>
        <h1 class="mt-3 text-4xl font-extrabold text-white md:text-5xl">Get in touch with us</h1>
        <p class="mt-3 max-w-xl text-slate-300">Project inquiries, consultations or partnership opportunities — we're here to help.</p>
      </div>
    </section>

    <!-- Contact info cards -->
    <section class="bg-primary">
      <div class="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        <div class="grid gap-4 sm:grid-cols-3">
          <div v-for="info in contactInfo" :key="info.label" class="flex items-center gap-4 rounded-2xl bg-white/10 px-6 py-5 backdrop-blur-sm">
            <div class="flex h-11 w-11 flex-shrink-0 items-center justify-center rounded-xl bg-white/20 text-2xl">{{ info.icon }}</div>
            <div>
              <p class="text-xs font-bold uppercase tracking-wider text-blue-200">{{ info.label }}</p>
              <p class="mt-0.5 text-sm font-medium text-white">{{ info.value }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Map + Form -->
    <section class="bg-slate-50 py-16">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="grid gap-10 lg:grid-cols-2 lg:items-start">

          <!-- Map -->
          <div class="overflow-hidden rounded-[28px] shadow-soft">
            <div id="map" class="h-80 w-full"></div>
            <div class="bg-white p-6">
              <h3 class="text-lg font-bold text-slate-900">KSI Bangladesh Headquarters</h3>
              <p class="mt-1 text-sm text-slate-500">Dhaka, Bangladesh</p>
              <div class="mt-4 grid grid-cols-2 gap-3">
                <div v-for="hour in hours" :key="hour.day" class="rounded-xl bg-slate-50 px-4 py-3">
                  <p class="text-xs font-semibold text-slate-500">{{ hour.day }}</p>
                  <p class="mt-0.5 text-sm font-medium text-slate-800">{{ hour.time }}</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Form -->
          <div class="rounded-[28px] bg-white p-8 shadow-soft">
            <h2 class="text-2xl font-extrabold text-slate-900">Send us a message</h2>
            <p class="mt-2 text-sm text-slate-500">Fill in the form and our team will get back to you within 24 hours.</p>

            <form @submit.prevent="handleSubmit" class="mt-7 space-y-5" novalidate>
              <div class="grid gap-4 sm:grid-cols-2">
                <div>
                  <label class="field-label">Full Name</label>
                  <input v-model="form.name" type="text" class="input-field" placeholder="Your name" required maxlength="100" />
                </div>
                <div>
                  <label class="field-label">Email Address</label>
                  <input v-model="form.email" type="email" class="input-field" placeholder="you@example.com" required />
                </div>
              </div>
              <div class="grid gap-4 sm:grid-cols-2">
                <div>
                  <label class="field-label">Phone Number</label>
                  <input v-model="form.phone" type="tel" class="input-field" placeholder="01XXXXXXXXX" required maxlength="20" />
                </div>
                <div>
                  <label class="field-label">Subject</label>
                  <input v-model="form.subject" type="text" class="input-field" placeholder="How can we help?" required maxlength="200" />
                </div>
              </div>
              <div>
                <label class="field-label">Message</label>
                <textarea v-model="form.message" rows="5" class="input-field resize-none" placeholder="Tell us about your project or inquiry…" required maxlength="2000"></textarea>
              </div>

              <!-- Honeypot -->
              <input v-model="form.honeypot" type="text" class="hidden" />

              <button
                type="submit"
                :disabled="sending"
                class="w-full rounded-full bg-primary py-3.5 text-sm font-bold text-white shadow-md transition hover:bg-blue-700 disabled:opacity-50"
              >
                {{ sending ? 'Sending…' : 'Send Message' }}
              </button>
            </form>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'
import { submitContact } from '../api/contact'
import { useToast } from '../composables/useToast'

const { addToast } = useToast()
const sending = ref(false)
const form = ref({ name: '', email: '', phone: '', subject: '', message: '', honeypot: '' })

const contactInfo = [
  { icon: '📍', label: 'Address', value: 'KSI Bangladesh HQ, Dhaka, Bangladesh' },
  { icon: '📧', label: 'Email', value: 'info@ksibangladesh.com' },
  { icon: '📞', label: 'Phone', value: '+880-1234-567890' },
]

const hours = [
  { day: 'Mon – Thu', time: '9:00 AM – 6:00 PM' },
  { day: 'Friday', time: '9:00 AM – 5:00 PM' },
  { day: 'Saturday', time: '10:00 AM – 2:00 PM' },
  { day: 'Sunday', time: 'Closed' },
]

const handleSubmit = async () => {
  if (form.value.honeypot) return
  sending.value = true
  try {
    await submitContact({ ...form.value })
    addToast('Message sent successfully. We\'ll get back to you soon!')
    form.value = { name: '', email: '', phone: '', subject: '', message: '', honeypot: '' }
  } catch {
    addToast('Unable to send message. Please try again.', 'error')
  } finally {
    sending.value = false
  }
}

onMounted(() => {
  const map = L.map('map', { scrollWheelZoom: false }).setView([23.8103, 90.4125], 13)
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors',
  }).addTo(map)
  L.marker([23.8103, 90.4125]).addTo(map).bindPopup('<strong>KSI Bangladesh HQ</strong><br>Dhaka, Bangladesh').openPopup()
})
</script>

<style scoped>
.field-label { display: block; font-size: 0.875rem; font-weight: 500; color: #475569; margin-bottom: 0.4rem; }
.input-field { width: 100%; border: 1px solid #cbd5e1; border-radius: 1rem; padding: 0.85rem 1.1rem; background: #f8fafc; font-size: 0.875rem; transition: border-color 0.15s, box-shadow 0.15s; }
.input-field:focus { outline: none; border-color: #1a56db; box-shadow: 0 0 0 3px rgba(26,86,219,0.1); }
</style>
