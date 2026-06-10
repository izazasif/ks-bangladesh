<template>
  <div>
    <!-- Hero -->
    <section class="relative overflow-hidden">
      <img
        src="https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1600&q=80"
        alt="KSI Services"
        class="h-72 w-full object-cover md:h-96"
        loading="eager"
      />
      <div class="absolute inset-0 bg-gradient-to-r from-slate-950/90 via-slate-950/60 to-transparent"></div>
      <div class="absolute inset-0 flex flex-col justify-center px-6 sm:px-12 lg:px-20">
        <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">What We Offer</p>
        <h1 class="mt-3 max-w-2xl text-4xl font-extrabold leading-tight text-white md:text-5xl">
          Comprehensive support for every sector
        </h1>
        <p class="mt-4 max-w-xl text-slate-300">
          KSI Bangladesh helps businesses, government agencies and enterprises succeed through targeted, sector-specific service groups.
        </p>
      </div>
    </section>

    <!-- Stats bar -->
    <section class="bg-primary">
      <div class="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
        <div class="grid grid-cols-2 gap-4 md:grid-cols-4">
          <div v-for="s in stats" :key="s.label" class="text-center">
            <p class="text-2xl font-black text-white">{{ s.value }}</p>
            <p class="text-xs font-medium text-blue-200">{{ s.label }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Service Groups -->
    <section class="bg-slate-50 py-16">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="grid gap-8 lg:grid-cols-2">
          <div v-for="group in serviceGroups" :key="group.title" class="overflow-hidden rounded-[32px] bg-white shadow-soft">
            <!-- Image banner -->
            <div class="relative h-52 overflow-hidden">
              <img :src="group.image" :alt="group.title" class="h-full w-full object-cover transition duration-500 hover:scale-105" loading="lazy" />
              <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 to-transparent"></div>
              <div class="absolute bottom-0 left-0 p-6">
                <span class="inline-flex items-center gap-2 rounded-full bg-white/20 px-3 py-1.5 text-xs font-bold uppercase tracking-wider text-white backdrop-blur-sm">
                  {{ group.sector }}
                </span>
                <h2 class="mt-2 text-2xl font-extrabold text-white">{{ group.title }}</h2>
              </div>
            </div>

            <!-- Content -->
            <div class="p-8">
              <p class="text-slate-500">{{ group.description }}</p>
              <ul class="mt-6 space-y-3">
                <li v-for="service in group.items" :key="service.title" class="flex items-start gap-4 rounded-2xl border border-slate-100 bg-slate-50 p-4 transition hover:border-primary/30 hover:bg-blue-50/40">
                  <div class="flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-xl bg-primary/10 text-xl">{{ service.icon }}</div>
                  <div>
                    <p class="font-semibold text-slate-900">{{ service.title }}</p>
                    <p class="mt-0.5 text-sm text-slate-500">{{ service.details }}</p>
                  </div>
                </li>
              </ul>
              <router-link
                :to="group.link"
                class="mt-7 inline-flex items-center gap-2 rounded-full bg-primary px-6 py-3 text-sm font-semibold text-white shadow-md transition hover:bg-blue-700"
              >
                Explore {{ group.sector }}
                <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="bg-primary py-16">
      <div class="mx-auto max-w-4xl px-4 text-center sm:px-6 lg:px-8">
        <h2 class="text-3xl font-extrabold text-white">Not sure which service fits your needs?</h2>
        <p class="mx-auto mt-4 max-w-xl text-blue-100">Our team is ready to consult and recommend the right solution for your organization.</p>
        <router-link to="/contact" class="mt-8 inline-flex items-center rounded-full bg-white px-8 py-4 text-sm font-bold text-primary shadow-lg transition hover:bg-slate-100">
          Talk to Our Team →
        </router-link>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useSEO } from '../../composables/useSEO'

useSEO({
  title: 'Our Services',
  description: 'Explore KSI Bangladesh\'s full range of services — First Class Contractor, Supplier, Digital Content, IT and AgriCare — tailored solutions for businesses, NGOs and government.',
  keywords: 'KSI Bangladesh services, first class contractor, supplier, digital content, IT services, agriculture Bangladesh',
  path: '/services',
})

const stats = [
  { value: '5', label: 'Core Sectors' },
  { value: '12+', label: 'Service Lines' },
  { value: '500+', label: 'Projects Done' },
  { value: '50+', label: 'Partners' },
]

const serviceGroups = [
  {
    sector: 'Agriculture',
    title: 'Agriculture Services',
    description: 'Smart agriculture solutions that improve yields, irrigation and harvest logistics across rural Bangladesh.',
    image: 'https://images.unsplash.com/photo-1625246333195-78d9c38ad449?auto=format&fit=crop&w=900&q=80',
    link: '/sectors/agriculture',
    items: [
      { icon: '🌾', title: 'Crop Management', details: 'Advisory and execution for modern crop cycles and yield optimization.' },
      { icon: '💧', title: 'Irrigation Planning', details: 'Water efficiency and smart irrigation design for local farms.' },
      { icon: '📈', title: 'Agri-Tech', details: 'Data-driven tools for farmer success and supply chain visibility.' },
    ],
  },
  {
    sector: 'IT',
    title: 'IT Services',
    description: 'Digital transformation with secure, scalable and user-friendly systems tailored for Bangladesh.',
    image: 'https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=900&q=80',
    link: '/sectors/it',
    items: [
      { icon: '⚙️', title: 'Software Development', details: 'Custom web and mobile apps built for rapid, reliable delivery.' },
      { icon: '☁️', title: 'Cloud & Data', details: 'Cloud migration and analytics for smarter, leaner operations.' },
      { icon: '🛡️', title: 'Cybersecurity', details: 'Protect critical systems with modern, layered security controls.' },
    ],
  },
  {
    sector: 'First Class Contractor',
    title: 'First Class Contractor',
    description: 'Civil infrastructure, roads & bridges, industrial establishment and canal excavation across Bangladesh.',
    image: 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=900&q=80',
    link: '/business-unit/first-class-contractor',
    items: [
      { icon: '🛣️', title: 'Roads & Bridges', details: 'Design and construction of roads, highways and bridge structures.' },
      { icon: '🏭', title: 'Industrial Establishment', details: 'Factory floors, industrial parks and commercial buildings.' },
      { icon: '💧', title: 'Canal Excavation', details: 'Precision canal digging and waterway development.' },
    ],
  },
  {
    sector: 'Supplier',
    title: 'Supplier Services',
    description: 'End-to-end procurement and supply chain solutions connecting vendors, materials and project sites across Bangladesh.',
    image: 'https://images.unsplash.com/photo-1553413077-190dd305871c?auto=format&fit=crop&w=900&q=80',
    link: '/sectors/supplier',
    items: [
      { icon: '🛒', title: 'Procurement', details: 'Strategic sourcing and purchasing for construction, agri and IT needs.' },
      { icon: '🤝', title: 'Vendor Management', details: 'Qualified vendor networks with quality checks and performance tracking.' },
      { icon: '🏭', title: 'Materials Supply', details: 'Reliable delivery of equipment, raw materials and consumables on time.' },
    ],
  },
  {
    sector: 'Digital Content',
    title: 'Digital Content Services',
    description: 'Creative content strategies, production and distribution to grow your brand\'s digital presence across Bangladesh.',
    image: 'https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?auto=format&fit=crop&w=900&q=80',
    link: '/sectors/digital-content',
    items: [
      { icon: '✍️', title: 'Content Creation', details: 'Written, visual and video content tailored to your audience and goals.' },
      { icon: '📱', title: 'Social Media', details: 'Full management of Facebook, LinkedIn and YouTube channels.' },
      { icon: '🎨', title: 'Design & Branding', details: 'Graphic design, logo creation and visual brand identity systems.' },
    ],
  },
]
</script>
