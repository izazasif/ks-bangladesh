<template>
  <div>
    <!-- Hero -->
    <section class="relative overflow-hidden">
      <img
        src="https://images.unsplash.com/photo-1625246333195-78d9c38ad449?auto=format&fit=crop&w=1600&q=80"
        alt="Agriculture"
        class="h-72 w-full object-cover md:h-96"
        loading="eager"
      />
      <div class="absolute inset-0 bg-gradient-to-r from-slate-950/90 via-slate-950/60 to-transparent"></div>
      <div class="absolute inset-0 flex flex-col justify-center px-6 sm:px-12 lg:px-20">
        <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Agriculture</p>
        <h1 class="mt-3 max-w-2xl text-4xl font-extrabold leading-tight text-white md:text-5xl">
          Transforming farming across Bangladesh
        </h1>
        <p class="mt-4 max-w-xl text-slate-300">
          We support farmers and agri-businesses with crop management, irrigation planning and modern agricultural technology.
        </p>
        <div class="mt-7 flex flex-wrap gap-3">
          <router-link to="/contact" class="inline-flex rounded-full bg-primary px-6 py-3 text-sm font-bold text-white shadow-lg transition hover:bg-blue-700">
            Get in Touch
          </router-link>
          <router-link to="/services" class="inline-flex rounded-full border border-white/40 px-6 py-3 text-sm font-bold text-white transition hover:bg-white/10">
            All Services
          </router-link>
        </div>
      </div>
    </section>

    <!-- Stats bar -->
    <section class="bg-primary">
      <div class="mx-auto max-w-7xl px-4 py-7 sm:px-6 lg:px-8">
        <div class="grid grid-cols-2 gap-4 md:grid-cols-4">
          <div v-for="s in stats" :key="s.label" class="text-center">
            <p class="text-2xl font-black text-white">{{ s.value }}</p>
            <p class="text-xs font-medium text-blue-200">{{ s.label }}</p>
          </div>
        </div>
      </div>
    </section>

    <div class="bg-slate-50">

      <!-- What We Do -->
      <section class="mx-auto max-w-6xl px-4 py-16 sm:px-6 lg:px-8">
        <div class="rounded-[35px] bg-white p-10 shadow-soft">
          <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Our Services</p>
          <h2 class="mt-3 text-3xl font-extrabold text-slate-900">What We Do</h2>
          <p class="mt-3 text-slate-500 max-w-2xl">Comprehensive agricultural services designed for Bangladesh's climate, land and rural communities.</p>
          <div class="mt-10 grid gap-6 md:grid-cols-2">
            <div
              v-for="item in services"
              :key="item.title"
              class="group flex gap-5 rounded-3xl border border-slate-100 bg-slate-50 p-6 transition hover:border-primary/30 hover:bg-blue-50/40 hover:shadow-sm"
            >
              <div class="flex h-14 w-14 flex-shrink-0 items-center justify-center rounded-2xl bg-primary/10 text-2xl transition group-hover:bg-primary/20">{{ item.icon }}</div>
              <div>
                <h3 class="text-lg font-bold text-slate-900">{{ item.title }}</h3>
                <p class="mt-2 text-sm leading-relaxed text-slate-500">{{ item.description }}</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Process -->
      <section class="mx-auto max-w-6xl px-4 pb-16 sm:px-6 lg:px-8">
        <div class="rounded-[35px] bg-white p-10 shadow-soft">
          <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">How It Works</p>
          <h2 class="mt-3 text-3xl font-extrabold text-slate-900">Our Agriculture Process</h2>
          <div class="mt-10 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
            <div
              v-for="(step, i) in process"
              :key="step.title"
              class="relative rounded-3xl border border-slate-100 bg-slate-50 p-6 text-center transition hover:border-primary/30 hover:shadow-sm"
            >
              <div class="mx-auto flex h-14 w-14 items-center justify-center rounded-full bg-primary text-lg font-black text-white shadow-md">{{ i + 1 }}</div>
              <h3 class="mt-4 text-base font-bold text-slate-900">{{ step.title }}</h3>
              <p class="mt-2 text-sm leading-relaxed text-slate-500">{{ step.description }}</p>
            </div>
          </div>
        </div>
      </section>

      <!-- Gallery -->
      <section class="mx-auto max-w-6xl px-4 pb-16 sm:px-6 lg:px-8">
        <div class="rounded-[35px] bg-white p-10 shadow-soft">
          <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Our Work</p>
          <h2 class="mt-3 text-3xl font-extrabold text-slate-900">Agriculture Gallery</h2>
          <div class="mt-8 grid gap-4 lg:grid-cols-2">
            <img
              :src="gallery[0]"
              alt="Agriculture"
              class="h-72 w-full rounded-3xl object-cover lg:h-full"
              loading="lazy"
            />
            <div class="grid gap-4">
              <img
                v-for="img in gallery.slice(1)"
                :key="img"
                :src="img"
                alt="Agriculture"
                class="h-44 w-full rounded-3xl object-cover"
                loading="lazy"
              />
            </div>
          </div>
        </div>
      </section>
    </div>

    <!-- CTA -->
    <section class="bg-primary py-16">
      <div class="mx-auto max-w-4xl px-4 text-center sm:px-6">
        <h2 class="text-3xl font-extrabold text-white">Ready to improve your agricultural output?</h2>
        <p class="mx-auto mt-4 max-w-xl text-blue-100">Our agri specialists are ready to help you achieve better yields, smarter irrigation and modern farm management.</p>
        <div class="mt-8 flex flex-wrap justify-center gap-3">
          <router-link to="/contact" class="inline-flex rounded-full bg-white px-8 py-4 text-sm font-bold text-primary shadow-lg transition hover:bg-slate-100">Contact Us Today</router-link>
          <router-link to="/services" class="inline-flex rounded-full border border-white/40 px-8 py-4 text-sm font-bold text-white transition hover:bg-white/10">View All Services</router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useSEO } from '../../composables/useSEO'

useSEO({
  title: 'Agriculture Services',
  description: 'KSI Bangladesh provides crop management, smart irrigation, agri-tech data tools and farmer support programs across Bangladesh\'s rural communities.',
  keywords: 'agriculture services Bangladesh, crop management, irrigation, agri-tech, farmer support KSI',
  path: '/sectors/agriculture',
})

const stats = [
  { value: '10,000+', label: 'Acres Managed' },
  { value: '2,000+', label: 'Farmers Supported' },
  { value: '150+', label: 'Agri Projects' },
  { value: '15+', label: 'Years Active' },
]

const services = [
  { icon: '🌿', title: 'Crop Management', description: 'Precision support for crop planning, field monitoring and yield optimization for sustainable farming.' },
  { icon: '💧', title: 'Irrigation Systems', description: 'Efficiency-driven water solutions, smart irrigation design and water conservation strategies.' },
  { icon: '📊', title: 'Agri-Tech & Data', description: 'Digital tools, analytics dashboards and data-driven marketplaces connecting producers to buyers.' },
  { icon: '🤝', title: 'Farmer Support', description: 'Training programs, resource distribution and community partnerships for rural development.' },
]

const process = [
  { title: 'Field Assessment', description: 'Understand soil conditions, climate patterns and crop potential in each region.' },
  { title: 'Crop Planning', description: 'Design optimal planting schedules, fertilizer plans and rotation strategies.' },
  { title: 'Resource Allocation', description: 'Coordinate farm teams, irrigation supply and agri-input delivery logistics.' },
  { title: 'Harvest & Logistics', description: 'Support full harvest handling and supply chain movement to market.' },
]

const gallery = [
  '/images/agri-canal-1.jpg',
  '/images/agri-canal-2.jpg',
  'https://images.unsplash.com/photo-1574943320219-553eb213f72d?auto=format&fit=crop&w=900&q=80',
]
</script>
