<template>
  <div>
    <section class="relative overflow-hidden">
      <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1600&q=80" alt="Kazi Corporation" class="h-[420px] w-full object-cover md:h-[520px]" loading="eager" />
      <div class="absolute inset-0 bg-gradient-to-r from-slate-950/90 via-slate-950/60 to-transparent"></div>
      <div class="absolute inset-0 flex flex-col justify-center px-6 sm:px-12 lg:px-24">
        <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Sister Concern</p>
        <h1 class="mt-3 max-w-2xl text-4xl font-extrabold leading-tight text-white md:text-5xl lg:text-6xl">Kazi Corporation</h1>
        <p class="mt-4 max-w-xl text-lg text-slate-300">A trusted corporate partner delivering business solutions, trade and professional services across Bangladesh.</p>
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
          <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">About Kazi Corporation</p>
          <h2 class="mt-3 text-3xl font-extrabold text-slate-900 md:text-4xl">Business Excellence Across Sectors</h2>
          <p class="mt-5 text-lg leading-relaxed text-slate-600">Kazi Corporation is a sister concern of KSI Bangladesh, focused on trade, business consultancy and professional services. We support enterprises, government bodies and NGOs with reliable corporate solutions.</p>
          <div class="mt-8 grid gap-4 sm:grid-cols-2">
            <div v-for="s in services" :key="s.title" class="rounded-2xl border border-slate-100 bg-slate-50 p-5">
              <span class="text-2xl">{{ s.icon }}</span>
              <h3 class="mt-3 font-bold text-slate-900">{{ s.title }}</h3>
              <p class="mt-1 text-sm text-slate-500">{{ s.desc }}</p>
            </div>
          </div>
        </div>
        <img src="https://images.unsplash.com/photo-1600880292203-757bb62b4baf?auto=format&fit=crop&w=900&q=80" alt="Kazi Corporation" class="h-96 w-full rounded-3xl object-cover shadow-soft" loading="lazy" />
      </div>
    </section>

    <section class="bg-primary py-20">
      <div class="mx-auto max-w-4xl px-4 text-center">
        <h2 class="text-3xl font-extrabold text-white">Work with Kazi Corporation</h2>
        <p class="mx-auto mt-4 max-w-xl text-blue-100">Reach out to explore trade partnerships, consultancy or business collaboration opportunities.</p>
        <router-link to="/contact" class="mt-8 inline-flex items-center rounded-full bg-white px-10 py-4 text-sm font-bold text-primary shadow-lg transition hover:bg-slate-100">Contact Us →</router-link>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useSEO } from '../../composables/useSEO'

useSEO({
  title: 'Kazi Corporation — Sister Concern',
  description: 'Kazi Corporation is a sister concern of KSI Bangladesh, delivering trade, business consultancy and professional services across Bangladesh.',
  keywords: 'Kazi Corporation Bangladesh, business consultancy, trade services, KSI sister concern',
  path: '/sister-concern/kazi-corporation',
})

const stats = [
  { value: '50+', label: 'Business Partners' },
  { value: '100+', label: 'Projects Handled' },
  { value: '10+', label: 'Years Active' },
  { value: '5+', label: 'Industry Sectors' },
]

const services = [
  { icon: '🤝', title: 'Trade & Commerce', desc: 'Import/export facilitation and domestic trade partnerships.' },
  { icon: '📋', title: 'Business Consultancy', desc: 'Strategy, compliance and operational advisory for businesses.' },
  { icon: '🏢', title: 'Corporate Services', desc: 'Company setup, documentation and professional support services.' },
  { icon: '🔗', title: 'Partnerships', desc: 'Joint ventures and collaboration with local and international firms.' },
]
</script>
