<template>
  <div>
    <!-- Hero -->
    <section class="relative overflow-hidden">
      <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1600&q=80" alt="KSI Bangladesh Management Team" class="h-72 w-full object-cover md:h-96" loading="eager" />
      <div class="absolute inset-0 bg-gradient-to-r from-slate-950/90 via-slate-950/60 to-transparent"></div>
      <div class="absolute inset-0 flex flex-col justify-center px-6 sm:px-12 lg:px-20">
        <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Our People</p>
        <h1 class="mt-3 text-4xl font-extrabold text-white md:text-5xl">Management &amp; Specialists</h1>
        <p class="mt-3 max-w-xl text-slate-300">Meet the experienced leaders and specialists driving KSI Bangladesh forward across every sector.</p>
      </div>
    </section>

    <!-- Leadership Team -->
    <section class="mx-auto max-w-7xl px-4 py-20 sm:px-6 lg:px-8">
      <div class="text-center">
        <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Leadership</p>
        <h2 class="mt-3 text-3xl font-extrabold text-slate-900 md:text-4xl">Senior Management</h2>
        <p class="mx-auto mt-4 max-w-2xl text-slate-500">Our leadership team brings decades of combined experience across construction, supply chain, technology and agriculture.</p>
      </div>

      <div class="mt-14 grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
        <div v-for="member in leadership" :key="member.name" class="overflow-hidden rounded-[32px] bg-white shadow-soft border border-slate-100 transition hover:shadow-md">
          <!-- Photo -->
          <div class="relative h-64 overflow-hidden bg-slate-100">
            <img v-if="member.photo" :src="member.photo" :alt="member.name" class="h-full w-full object-cover object-top" loading="lazy" />
            <div v-else class="flex h-full w-full items-center justify-center" :class="member.bg">
              <span class="text-5xl font-black" :class="member.color">{{ member.initials }}</span>
            </div>
          </div>
          <!-- Info -->
          <div class="p-7">
            <h3 class="text-xl font-extrabold text-slate-900">{{ member.name }}</h3>
            <p class="mt-1 text-sm font-bold text-primary">{{ member.title }}</p>
            <div class="mt-4 space-y-2">
              <div class="flex items-start gap-2 text-sm text-slate-600">
                <span class="mt-0.5 text-primary font-bold">▸</span>
                <span>{{ member.experience }}</span>
              </div>
              <div v-if="member.education" class="flex items-start gap-2 text-sm text-slate-500">
                <span class="mt-0.5">🎓</span>
                <span>{{ member.education }}</span>
              </div>
              <div v-if="member.expertise" class="flex items-start gap-2 text-sm text-slate-500">
                <span class="mt-0.5">⭐</span>
                <span>{{ member.expertise }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Specialists -->
    <section class="bg-slate-50 py-20">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="text-center">
          <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Experts</p>
          <h2 class="mt-3 text-3xl font-extrabold text-slate-900 md:text-4xl">Our Specialists</h2>
          <p class="mx-auto mt-4 max-w-2xl text-slate-500">Domain experts who deliver technical excellence in every project we undertake.</p>
        </div>
        <div class="mt-14 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
          <div v-for="spec in specialists" :key="spec.name" class="rounded-[28px] bg-white p-6 shadow-soft text-center border border-slate-100">
            <div class="mx-auto mb-4 flex h-16 w-16 items-center justify-center rounded-2xl text-3xl" :class="spec.bg">{{ spec.icon }}</div>
            <h3 class="font-bold text-slate-900">{{ spec.name }}</h3>
            <p class="mt-1 text-sm font-semibold text-primary">{{ spec.role }}</p>
            <p class="mt-2 text-xs leading-relaxed text-slate-500">{{ spec.bio }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Join CTA -->
    <section class="bg-primary py-20">
      <div class="mx-auto max-w-4xl px-4 text-center sm:px-6 lg:px-8">
        <h2 class="text-3xl font-extrabold text-white md:text-4xl">Join Our Team</h2>
        <p class="mx-auto mt-4 max-w-xl text-lg text-blue-100">We're always looking for talented professionals to grow with KSI Bangladesh.</p>
        <router-link to="/contact" class="mt-8 inline-flex items-center rounded-full bg-white px-10 py-4 text-sm font-bold text-primary shadow-lg transition hover:bg-slate-100">Contact Us →</router-link>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useSEO } from '../composables/useSEO'

useSEO({
  title: 'Management & Specialists',
  description: 'Meet the experienced management team and specialists at KSI Bangladesh driving excellence across Construction, Supplier, IT, Digital Content and AgriCare.',
  keywords: 'KSI Bangladesh management team, specialists, leadership, directors, Bangladesh',
  path: '/management',
})

const leadership = [
  {
    name: 'Md. Kamal Hossain',
    title: 'Chairman & Managing Director',
    initials: 'KH',
    bg: 'bg-primary/10',
    color: 'text-primary',
    photo: '',
    experience: '20+ years leading multi-sector operations across Bangladesh.',
    education: 'MBA, University of Dhaka',
    expertise: 'Strategy, Business Development, Government Relations',
  },
  {
    name: 'Ayesha Noor',
    title: 'Chief Operations Officer',
    initials: 'AN',
    bg: 'bg-emerald-100',
    color: 'text-emerald-700',
    photo: '',
    experience: 'Over 15 years leading cross-sector operations with a focus on sustainable delivery.',
    education: 'BBA, BRAC University',
    expertise: 'Operations Management, Supply Chain, Compliance',
  },
  {
    name: 'Mohammad Rafiq',
    title: 'Technical Director',
    initials: 'MR',
    bg: 'bg-purple-100',
    color: 'text-purple-700',
    photo: '',
    experience: 'Software architect specialising in cloud infrastructure and digital transformation.',
    education: 'BSc Computer Science, BUET',
    expertise: 'IT Architecture, Cloud Solutions, Cybersecurity',
  },
  {
    name: 'Sadia Zaman',
    title: 'Head of Project Management',
    initials: 'SZ',
    bg: 'bg-amber-100',
    color: 'text-amber-700',
    photo: '',
    experience: 'PMP-certified manager with a strong record delivering construction and agri-tech initiatives.',
    education: 'MSc Civil Engineering, BUET',
    expertise: 'Project Management, Construction, Quality Control',
  },
  {
    name: 'Kamal Mahmud',
    title: 'Supply Chain & Procurement Lead',
    initials: 'KM',
    bg: 'bg-rose-100',
    color: 'text-rose-700',
    photo: '',
    experience: 'Expert in procurement, vendor management and supply chain across all sectors.',
    education: 'BBA Supply Chain Management',
    expertise: 'Procurement, Logistics, Vendor Relations',
  },
  {
    name: 'Nasreen Akter',
    title: 'Head of Digital Content',
    initials: 'NA',
    bg: 'bg-cyan-100',
    color: 'text-cyan-700',
    photo: '',
    experience: '10+ years in digital marketing, content creation and brand development.',
    education: 'BA Mass Communication, Dhaka University',
    expertise: 'Content Strategy, Social Media, Video Production',
  },
]

const specialists = [
  { icon: '🏗️', bg: 'bg-primary/10', name: 'Eng. Rahim Uddin', role: 'Civil Engineer', bio: '15+ years in roads, bridges and infrastructure projects across Bangladesh.' },
  { icon: '💧', bg: 'bg-blue-100', name: 'Eng. Farida Islam', role: 'Irrigation Specialist', bio: 'Expert in canal excavation, water management and agri-irrigation systems.' },
  { icon: '💻', bg: 'bg-purple-100', name: 'Tanvir Ahmed', role: 'Senior Software Engineer', bio: 'Full-stack developer specialising in enterprise applications and cloud deployment.' },
  { icon: '🏥', bg: 'bg-emerald-100', name: 'Shahana Begum', role: 'Health Supply Specialist', bio: 'Procurement expert for medical equipment, surgical items and pharmaceuticals.' },
]
</script>
