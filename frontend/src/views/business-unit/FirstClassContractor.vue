<template>
  <div>
    <!-- Hero -->
    <section class="relative overflow-hidden">
      <img src="https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=1600&q=80" alt="First Class Contractor KSI Bangladesh" class="h-[420px] w-full object-cover md:h-[520px]" loading="eager" />
      <div class="absolute inset-0 bg-gradient-to-r from-slate-950/90 via-slate-950/60 to-transparent"></div>
      <div class="absolute inset-0 flex flex-col justify-center px-6 sm:px-12 lg:px-24">
        <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Business Unit</p>
        <h1 class="mt-3 max-w-2xl text-4xl font-extrabold leading-tight text-white md:text-5xl lg:text-6xl">First Class Contractor</h1>
        <p class="mt-4 max-w-xl text-lg text-slate-300">Civil infrastructure, Roads &amp; Bridges, Industrial Establishment and Canal Excavation — delivered to the highest standards.</p>
        <div class="mt-8 flex flex-wrap gap-4">
          <router-link to="/contact" class="inline-flex rounded-full bg-primary px-8 py-4 text-sm font-bold text-white shadow-lg transition hover:bg-blue-700">Start a Project</router-link>
          <router-link to="/about" class="inline-flex rounded-full border border-white/40 px-8 py-4 text-sm font-bold text-white transition hover:bg-white/10">Learn More</router-link>
        </div>
      </div>
    </section>

    <!-- Stats -->
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

    <!-- About section -->
    <section class="mx-auto max-w-7xl px-4 py-20 sm:px-6 lg:px-8">
      <div class="grid items-center gap-12 lg:grid-cols-2">
        <div>
          <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Who We Are</p>
          <h2 class="mt-3 text-3xl font-extrabold text-slate-900 md:text-4xl">Trusted Infrastructure Experts</h2>
          <p class="mt-5 text-lg leading-relaxed text-slate-600">
            We are a first class contractor delivering civil infrastructure, Roads &amp; Bridges, Industrial Establishment and Canal Excavation across Bangladesh. With a highly skilled workforce and modern equipment, we execute every project with precision, safety and on-time delivery.
          </p>
          <div class="mt-8 grid grid-cols-2 gap-4">
            <div v-for="point in points" :key="point" class="flex items-center gap-3 rounded-2xl bg-slate-50 px-4 py-3">
              <span class="flex h-7 w-7 flex-shrink-0 items-center justify-center rounded-full bg-primary/10 text-primary text-sm font-bold">✓</span>
              <span class="text-sm font-medium text-slate-700">{{ point }}</span>
            </div>
          </div>
        </div>
        <div class="grid grid-cols-2 gap-4">
          <img :src="'/images/agri-canal-1.jpg'" alt="Canal Excavation" class="h-56 w-full rounded-3xl object-cover shadow-soft" loading="lazy" />
          <img :src="'/images/agri-canal-2.jpg'" alt="Canal Excavation" class="mt-8 h-56 w-full rounded-3xl object-cover shadow-soft" loading="lazy" />
        </div>
      </div>
    </section>

    <!-- Services -->
    <section class="bg-slate-50 py-20">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="text-center">
          <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">What We Do</p>
          <h2 class="mt-3 text-3xl font-extrabold text-slate-900 md:text-4xl">Our Core Services</h2>
        </div>
        <div class="mt-14 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
          <div v-for="s in services" :key="s.title" class="rounded-[28px] bg-white p-7 shadow-soft transition hover:border-primary/30 hover:shadow-md border border-slate-100">
            <div class="mb-4 flex h-14 w-14 items-center justify-center rounded-2xl bg-primary/10 text-3xl">{{ s.icon }}</div>
            <h3 class="text-lg font-bold text-slate-900">{{ s.title }}</h3>
            <p class="mt-2 text-sm leading-relaxed text-slate-500">{{ s.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="bg-primary py-20">
      <div class="mx-auto max-w-4xl px-4 text-center sm:px-6 lg:px-8">
        <h2 class="text-3xl font-extrabold text-white md:text-4xl">Ready to build something great?</h2>
        <p class="mx-auto mt-4 max-w-xl text-lg text-blue-100">Share your project requirements and our team will prepare a proposal for you.</p>
        <router-link to="/contact" class="mt-8 inline-flex items-center rounded-full bg-white px-10 py-4 text-sm font-bold text-primary shadow-lg transition hover:bg-slate-100">Get a Free Quote →</router-link>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useSEO } from '../../composables/useSEO'

useSEO({
  title: 'First Class Contractor',
  description: 'KSI Bangladesh is a first class contractor delivering civil infrastructure, Roads & Bridges, Industrial Establishment and Canal Excavation across Bangladesh.',
  keywords: 'first class contractor Bangladesh, civil infrastructure, roads bridges, canal excavation, industrial construction KSI',
  path: '/business-unit/first-class-contractor',
})

const stats = [
  { value: '120+', label: 'Projects Completed' },
  { value: '500K+', label: 'sqm Built' },
  { value: '100%', label: 'Safety Compliance' },
  { value: '15+', label: 'Years Experience' },
]

const points = ['Civil Infrastructure', 'Roads & Bridges', 'Industrial Establishment', 'Canal Excavation', 'Site Supervision', 'On-time Delivery']

const services = [
  { icon: '🛣️', title: 'Roads & Bridges', description: 'Design and construction of roads, highways and bridge structures for public and private sectors.' },
  { icon: '🏭', title: 'Industrial Establishment', description: 'Factory floors, industrial parks and commercial building construction to international standards.' },
  { icon: '💧', title: 'Canal Excavation', description: 'Precision canal digging and waterway development for irrigation, drainage and infrastructure.' },
  { icon: '🏗️', title: 'Civil Infrastructure', description: 'Complete civil works including foundations, retaining walls, drainage systems and site development.' },
]
</script>
