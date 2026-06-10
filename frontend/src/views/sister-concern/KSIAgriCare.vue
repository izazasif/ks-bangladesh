<template>
  <div>
    <section class="relative overflow-hidden">
      <img src="https://images.unsplash.com/photo-1625246333195-78d9c38ad449?auto=format&fit=crop&w=1600&q=80" alt="KSI AgriCare" class="h-[420px] w-full object-cover md:h-[520px]" loading="eager" />
      <div class="absolute inset-0 bg-gradient-to-r from-slate-950/90 via-slate-950/60 to-transparent"></div>
      <div class="absolute inset-0 flex flex-col justify-center px-6 sm:px-12 lg:px-24">
        <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Sister Concern</p>
        <h1 class="mt-3 max-w-2xl text-4xl font-extrabold leading-tight text-white md:text-5xl lg:text-6xl">KSI AgriCare</h1>
        <p class="mt-4 max-w-xl text-lg text-slate-300">Dedicated agriculture and rural development services — empowering farmers and agri-businesses across Bangladesh.</p>
        <div class="mt-8 flex flex-wrap gap-4">
          <router-link to="/contact" class="inline-flex rounded-full bg-primary px-8 py-4 text-sm font-bold text-white shadow-lg transition hover:bg-blue-700">Get in Touch</router-link>
        </div>
      </div>
    </section>

    <section class="bg-primary">
      <div class="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        <div class="grid grid-cols-2 gap-6 md:grid-cols-4">
          <div v-for="stat in stats" :key="stat.label" class="flex flex-col items-center text-center">
            <span class="text-3xl font-black text-white">{{ stat.value }}</span>
            <span class="mt-1 text-sm font-medium text-blue-200">{{ stat.label }}</span>
          </div>
        </div>
      </div>
    </section>

    <section class="mx-auto max-w-7xl px-4 py-20 sm:px-6 lg:px-8">
      <div class="grid items-center gap-12 lg:grid-cols-2">
        <div>
          <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">About KSI AgriCare</p>
          <h2 class="mt-3 text-3xl font-extrabold text-slate-900 md:text-4xl">Growing Bangladesh's Agricultural Future</h2>
          <p class="mt-5 text-lg leading-relaxed text-slate-600">KSI AgriCare is the agriculture-focused sister concern of KSI Bangladesh, dedicated to modern farming techniques, crop advisory, irrigation systems and rural development programs that improve livelihoods across Bangladesh.</p>
          <div class="mt-8 grid gap-4 sm:grid-cols-2">
            <div v-for="s in services" :key="s.title" class="rounded-2xl border border-slate-100 bg-slate-50 p-5">
              <span class="text-2xl">{{ s.icon }}</span>
              <h3 class="mt-3 font-bold text-slate-900">{{ s.title }}</h3>
              <p class="mt-1 text-sm text-slate-500">{{ s.desc }}</p>
            </div>
          </div>
        </div>
        <div class="grid grid-cols-2 gap-4">
          <img src="/images/agri-canal-1.jpg" alt="AgriCare field" class="h-56 w-full rounded-3xl object-cover shadow-soft" loading="lazy" />
          <img src="/images/agri-canal-2.jpg" alt="AgriCare irrigation" class="mt-8 h-56 w-full rounded-3xl object-cover shadow-soft" loading="lazy" />
        </div>
      </div>
    </section>

    <section class="bg-primary py-20">
      <div class="mx-auto max-w-4xl px-4 text-center">
        <h2 class="text-3xl font-extrabold text-white">Partner with KSI AgriCare</h2>
        <p class="mx-auto mt-4 max-w-xl text-blue-100">Contact us for crop advisory, irrigation projects or agri-tech solutions.</p>
        <router-link to="/contact" class="mt-8 inline-flex items-center rounded-full bg-white px-10 py-4 text-sm font-bold text-primary shadow-lg transition hover:bg-slate-100">Contact Us →</router-link>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useSEO } from '../../composables/useSEO'

useSEO({
  title: 'KSI AgriCare — Agriculture Sister Concern',
  description: 'KSI AgriCare is the agriculture-focused sister concern of KSI Bangladesh, providing crop advisory, irrigation and rural development services.',
  keywords: 'KSI AgriCare, agriculture Bangladesh, crop advisory, irrigation, rural development',
  path: '/sister-concern/ksi-agricare',
})

const stats = [
  { value: '10,000+', label: 'Acres Managed' },
  { value: '2,000+', label: 'Farmers Supported' },
  { value: '150+', label: 'Agri Projects' },
  { value: '15+', label: 'Years Active' },
]

const services = [
  { icon: '🌾', title: 'Crop Management', desc: 'Seasonal crop planning and yield optimization advisory.' },
  { icon: '💧', title: 'Irrigation Systems', desc: 'Smart water management and irrigation infrastructure.' },
  { icon: '📊', title: 'Agri-Tech', desc: 'Digital tools and data analytics for modern farming.' },
  { icon: '🤝', title: 'Farmer Support', desc: 'Training, resources and community development programs.' },
]
</script>
