<template>
  <div>
    <!-- Hero -->
    <section class="relative overflow-hidden">
      <img
        src="https://images.unsplash.com/photo-1553413077-190dd305871c?auto=format&fit=crop&w=1600&q=80"
        alt="Supplier Services KSI Bangladesh"
        class="h-[420px] w-full object-cover md:h-[520px]"
        loading="eager"
      />
      <div class="absolute inset-0 bg-gradient-to-r from-slate-950/90 via-slate-950/60 to-transparent"></div>
      <div class="absolute inset-0 flex flex-col justify-center px-6 sm:px-12 lg:px-24">
        <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Our Sector</p>
        <h1 class="mt-3 max-w-2xl text-4xl font-extrabold leading-tight text-white md:text-5xl lg:text-6xl">Supplier &amp; Procurement</h1>
        <p class="mt-4 max-w-xl text-lg text-slate-300">Strategic sourcing, vendor management and materials supply — connecting the right resources to every project.</p>
        <div class="mt-8 flex flex-wrap gap-4">
          <router-link to="/contact" class="inline-flex rounded-full bg-primary px-8 py-4 text-sm font-bold text-white shadow-lg transition hover:bg-blue-700">Start a Request</router-link>
          <router-link to="/services" class="inline-flex rounded-full border border-white/40 px-8 py-4 text-sm font-bold text-white transition hover:bg-white/10">View All Services</router-link>
        </div>
      </div>
    </section>

    <!-- Stats bar -->
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

    <!-- What We Do -->
    <section class="mx-auto max-w-7xl px-4 py-20 sm:px-6 lg:px-8">
      <div class="text-center">
        <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">What We Do</p>
        <h2 class="mt-3 text-3xl font-extrabold text-slate-900 md:text-4xl">Our Supplier Services</h2>
        <p class="mx-auto mt-4 max-w-2xl text-slate-500">From procurement strategy to last-mile delivery, we manage the full supply chain so your projects stay on track.</p>
      </div>
      <div class="mt-14 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
        <div v-for="s in services" :key="s.title" class="rounded-[28px] border border-slate-100 bg-white p-7 shadow-soft transition hover:border-primary/30 hover:shadow-md">
          <div class="mb-4 flex h-14 w-14 items-center justify-center rounded-2xl bg-primary/10 text-3xl">{{ s.icon }}</div>
          <h3 class="text-lg font-bold text-slate-900">{{ s.title }}</h3>
          <p class="mt-2 text-sm leading-relaxed text-slate-500">{{ s.description }}</p>
        </div>
      </div>
    </section>

    <!-- Process -->
    <section class="bg-slate-50 py-20">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="text-center">
          <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">How It Works</p>
          <h2 class="mt-3 text-3xl font-extrabold text-slate-900 md:text-4xl">Our Supply Process</h2>
        </div>
        <div class="mt-14 grid gap-6 sm:grid-cols-2 lg:grid-cols-5">
          <div v-for="(step, i) in process" :key="step.title" class="relative rounded-[24px] bg-white p-6 shadow-soft">
            <div class="mb-4 flex h-10 w-10 items-center justify-center rounded-full bg-primary text-sm font-black text-white">{{ i + 1 }}</div>
            <h3 class="text-base font-bold text-slate-900">{{ step.title }}</h3>
            <p class="mt-2 text-sm leading-relaxed text-slate-500">{{ step.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Gallery -->
    <section class="mx-auto max-w-7xl px-4 py-20 sm:px-6 lg:px-8">
      <div class="grid gap-4 sm:grid-cols-3">
        <img v-for="img in gallery" :key="img" :src="img" alt="Supplier work" class="h-56 w-full rounded-[24px] object-cover transition hover:scale-[1.02]" loading="lazy" />
      </div>
    </section>

    <!-- CTA -->
    <section class="bg-primary py-20">
      <div class="mx-auto max-w-4xl px-4 text-center sm:px-6 lg:px-8">
        <h2 class="text-3xl font-extrabold text-white md:text-4xl">Need reliable supply chain support?</h2>
        <p class="mx-auto mt-4 max-w-xl text-lg text-blue-100">Tell us your project requirements and we'll connect you with the right vendors and materials.</p>
        <router-link to="/contact" class="mt-8 inline-flex items-center rounded-full bg-white px-10 py-4 text-sm font-bold text-primary shadow-lg transition hover:bg-slate-100">
          Get a Quote →
        </router-link>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useSEO } from '../../composables/useSEO'

useSEO({
  title: 'Supplier & Procurement Services',
  description: 'KSI Bangladesh provides strategic procurement, vendor management and materials supply for construction, agriculture and IT projects across Bangladesh.',
  keywords: 'supplier Bangladesh, procurement services, vendor management, materials supply, KSI supplier',
  path: '/sectors/supplier',
})

const stats = [
  { value: '500+', label: 'Vendors Networked' },
  { value: '100+', label: 'Supply Categories' },
  { value: '50+', label: 'Active Partners' },
  { value: '15+', label: 'Years Experience' },
]

const services = [
  { icon: '🛒', title: 'Procurement & Sourcing', description: 'Strategic purchasing from qualified suppliers for construction materials, agri inputs and IT equipment.' },
  { icon: '🤝', title: 'Vendor Management', description: 'Onboarding, evaluation and performance tracking of suppliers to maintain quality and reliability.' },
  { icon: '🏭', title: 'Materials Supply', description: 'Timely delivery of raw materials, equipment and consumables directly to project sites.' },
  { icon: '📋', title: 'Contract Management', description: 'End-to-end supplier contracts, pricing negotiations and compliance documentation.' },
]

const process = [
  { title: 'Needs Assessment', description: 'Understand project requirements, quantities, timelines and quality standards.' },
  { title: 'Vendor Sourcing', description: 'Identify and shortlist qualified suppliers from our verified network.' },
  { title: 'Quality Verification', description: 'Inspect materials and evaluate vendors before commitment.' },
  { title: 'Order & Delivery', description: 'Coordinate procurement, logistics and on-site delivery.' },
  { title: 'Review & Optimize', description: 'Track supplier performance and refine the supply chain continuously.' },
]

const gallery = [
  'https://images.unsplash.com/photo-1553413077-190dd305871c?auto=format&fit=crop&w=900&q=80',
  'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=900&q=80',
  'https://images.unsplash.com/photo-1494412574643-ff11b0a5c1c3?auto=format&fit=crop&w=900&q=80',
]
</script>
