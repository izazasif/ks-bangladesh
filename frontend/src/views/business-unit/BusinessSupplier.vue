<template>
  <div>
    <!-- Hero -->
    <section class="relative overflow-hidden">
      <img src="https://images.unsplash.com/photo-1553413077-190dd305871c?auto=format&fit=crop&w=1600&q=80" alt="Supplier KSI Bangladesh" class="h-[420px] w-full object-cover md:h-[520px]" loading="eager" />
      <div class="absolute inset-0 bg-gradient-to-r from-slate-950/90 via-slate-950/60 to-transparent"></div>
      <div class="absolute inset-0 flex flex-col justify-center px-6 sm:px-12 lg:px-24">
        <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Business Unit</p>
        <h1 class="mt-3 max-w-2xl text-4xl font-extrabold leading-tight text-white md:text-5xl lg:text-6xl">Supplier</h1>
        <p class="mt-4 max-w-xl text-lg text-slate-300">Health equipment, surgical items, medicine, furniture, electronics and promotional items — supplied to hospitals, universities, schools and industry.</p>
        <div class="mt-8 flex flex-wrap gap-4">
          <router-link to="/contact" class="inline-flex rounded-full bg-primary px-8 py-4 text-sm font-bold text-white shadow-lg transition hover:bg-blue-700">Request a Quote</router-link>
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

    <!-- About -->
    <section class="mx-auto max-w-7xl px-4 py-20 sm:px-6 lg:px-8">
      <div class="grid items-center gap-12 lg:grid-cols-2">
        <div>
          <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Who We Are</p>
          <h2 class="mt-3 text-3xl font-extrabold text-slate-900 md:text-4xl">Leading Supplier in Bangladesh</h2>
          <p class="mt-5 text-lg leading-relaxed text-slate-600">
            KSI Bangladesh is a leading health equipment, surgical item &amp; medicine, furniture, electric &amp; electronics product, gift and promotion item supplier to the Hospital, University, School &amp; College and Industrial sector.
          </p>
          <p class="mt-4 text-slate-500 leading-relaxed">
            We source high-quality products from certified manufacturers and deliver to institutions across Bangladesh, ensuring reliability, competitive pricing and timely supply.
          </p>
          <router-link to="/contact" class="mt-8 inline-flex rounded-full bg-primary px-8 py-3.5 text-sm font-bold text-white shadow-md transition hover:bg-blue-700">Get in Touch</router-link>
        </div>
        <div class="grid grid-cols-2 gap-4">
          <img src="https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=900&q=80" alt="Health Equipment" class="h-56 w-full rounded-3xl object-cover shadow-soft" loading="lazy" />
          <img src="https://images.unsplash.com/photo-1631549916768-4119b2e5f926?auto=format&fit=crop&w=900&q=80" alt="Medical Supplies" class="mt-8 h-56 w-full rounded-3xl object-cover shadow-soft" loading="lazy" />
        </div>
      </div>
    </section>

    <!-- Product Categories -->
    <section class="bg-slate-50 py-20">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="text-center">
          <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">What We Supply</p>
          <h2 class="mt-3 text-3xl font-extrabold text-slate-900 md:text-4xl">Product Categories</h2>
          <p class="mx-auto mt-4 max-w-2xl text-slate-500">We supply a wide range of products to hospitals, educational institutions and industrial clients across Bangladesh.</p>
        </div>
        <div class="mt-14 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          <div v-for="cat in categories" :key="cat.title" class="rounded-[28px] bg-white p-7 shadow-soft border border-slate-100 transition hover:border-primary/30 hover:shadow-md">
            <div class="mb-4 flex h-14 w-14 items-center justify-center rounded-2xl bg-primary/10 text-3xl">{{ cat.icon }}</div>
            <h3 class="text-lg font-bold text-slate-900">{{ cat.title }}</h3>
            <p class="mt-2 text-sm leading-relaxed text-slate-500">{{ cat.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Clients we serve -->
    <section class="mx-auto max-w-7xl px-4 py-20 sm:px-6 lg:px-8">
      <div class="text-center">
        <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Who We Serve</p>
        <h2 class="mt-3 text-3xl font-extrabold text-slate-900 md:text-4xl">Our Client Sectors</h2>
      </div>
      <div class="mt-12 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <div v-for="client in clients" :key="client.name" class="flex flex-col items-center rounded-[24px] bg-slate-50 p-8 text-center shadow-soft">
          <span class="text-4xl">{{ client.icon }}</span>
          <h3 class="mt-4 text-base font-bold text-slate-900">{{ client.name }}</h3>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="bg-primary py-20">
      <div class="mx-auto max-w-4xl px-4 text-center sm:px-6 lg:px-8">
        <h2 class="text-3xl font-extrabold text-white md:text-4xl">Need a reliable supplier?</h2>
        <p class="mx-auto mt-4 max-w-xl text-lg text-blue-100">Send us your requirements and we'll provide a competitive quotation within 24 hours.</p>
        <router-link to="/contact" class="mt-8 inline-flex items-center rounded-full bg-white px-10 py-4 text-sm font-bold text-primary shadow-lg transition hover:bg-slate-100">Request a Quote →</router-link>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useSEO } from '../../composables/useSEO'

useSEO({
  title: 'Supplier — Health Equipment & More',
  description: 'KSI Bangladesh supplies health equipment, surgical items, medicine, furniture, electronics and promotional items to hospitals, universities, schools and industry.',
  keywords: 'health equipment supplier Bangladesh, surgical items, medicine supplier, furniture supplier, electronics supplier KSI',
  path: '/business-unit/supplier',
})

const stats = [
  { value: '500+', label: 'Products Supplied' },
  { value: '100+', label: 'Institutions Served' },
  { value: '50+', label: 'Trusted Brands' },
  { value: '15+', label: 'Years Experience' },
]

const categories = [
  { icon: '🏥', title: 'Health Equipment', description: 'Hospital-grade medical equipment, diagnostic tools and patient care devices from certified manufacturers.' },
  { icon: '💉', title: 'Surgical Items & Medicine', description: 'Surgical instruments, disposables, pharmaceuticals and medical consumables for healthcare institutions.' },
  { icon: '🪑', title: 'Furniture', description: 'Office, classroom, laboratory and hospital furniture designed for durability and comfort.' },
  { icon: '💡', title: 'Electric & Electronics', description: 'Electrical fittings, electronics, appliances and IT hardware for institutional and industrial use.' },
  { icon: '🎁', title: 'Gift & Promotional Items', description: 'Custom branded gifts, corporate merchandise and promotional materials for events and campaigns.' },
  { icon: '🔧', title: 'Industrial Supplies', description: 'Safety equipment, tools, maintenance supplies and industrial materials for factory and site operations.' },
]

const clients = [
  { icon: '🏥', name: 'Hospitals & Clinics' },
  { icon: '🎓', name: 'Universities & Colleges' },
  { icon: '🏫', name: 'Schools' },
  { icon: '🏭', name: 'Industrial Sector' },
]
</script>
