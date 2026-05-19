<template>
  <div>
    <!-- Hero -->
    <section class="relative overflow-hidden">
      <img
        src="https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=1600&q=80"
        alt="Construction"
        class="h-72 w-full object-cover md:h-96"
        loading="eager"
      />
      <div class="absolute inset-0 bg-gradient-to-r from-slate-950/90 via-slate-950/60 to-transparent"></div>
      <div class="absolute inset-0 flex flex-col justify-center px-6 sm:px-12 lg:px-20">
        <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Construction</p>
        <h1 class="mt-3 max-w-2xl text-4xl font-extrabold leading-tight text-white md:text-5xl">
          Building Bangladesh's future with precision
        </h1>
        <p class="mt-4 max-w-xl text-slate-300">
          Delivering quality infrastructure and civil engineering services for safe, scalable and lasting growth nationwide.
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
          <p class="mt-3 text-slate-500 max-w-2xl">End-to-end construction and infrastructure services, built on safety, compliance and quality workmanship.</p>
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
          <h2 class="mt-3 text-3xl font-extrabold text-slate-900">Our Construction Process</h2>
          <div class="mt-10 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            <div
              v-for="(step, i) in process"
              :key="step.title"
              class="relative rounded-3xl border border-slate-100 bg-slate-50 p-6 transition hover:border-primary/30 hover:shadow-sm"
            >
              <div class="flex h-12 w-12 items-center justify-center rounded-full bg-primary text-base font-black text-white shadow-md">{{ i + 1 }}</div>
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
          <h2 class="mt-3 text-3xl font-extrabold text-slate-900">Construction Gallery</h2>
          <div class="mt-8 grid gap-4 lg:grid-cols-2">
            <img
              :src="gallery[0]"
              alt="Construction"
              class="h-72 w-full rounded-3xl object-cover lg:h-full"
              loading="lazy"
            />
            <div class="grid gap-4">
              <img
                v-for="img in gallery.slice(1)"
                :key="img"
                :src="img"
                alt="Construction"
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
        <h2 class="text-3xl font-extrabold text-white">Ready to build your next project?</h2>
        <p class="mx-auto mt-4 max-w-xl text-blue-100">From site survey to handover, our construction teams deliver quality infrastructure on time and within budget.</p>
        <div class="mt-8 flex flex-wrap justify-center gap-3">
          <router-link to="/contact" class="inline-flex rounded-full bg-white px-8 py-4 text-sm font-bold text-primary shadow-lg transition hover:bg-slate-100">Start a Project</router-link>
          <router-link to="/services" class="inline-flex rounded-full border border-white/40 px-8 py-4 text-sm font-bold text-white transition hover:bg-white/10">View All Services</router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
const stats = [
  { value: '120+', label: 'Projects Built' },
  { value: '500K+', label: 'Sq Metres Delivered' },
  { value: '100%', label: 'Regulatory Compliance' },
  { value: '0', label: 'Major Safety Incidents' },
]

const services = [
  { icon: '📐', title: 'Civil Engineering', description: 'Comprehensive structural planning and technical supervision for residential, commercial and public works.' },
  { icon: '🏗️', title: 'Infrastructure Works', description: 'Building roads, bridges, commercial spaces and public amenities with safety-first execution.' },
  { icon: '🧱', title: 'Project Management', description: 'Schedule-driven coordination, quality oversight and stakeholder reporting from groundbreaking to handover.' },
  { icon: '🛡️', title: 'Safety & Compliance', description: 'Rigorous safety standards, regulatory liaison and compliance audits to protect people and assets.' },
]

const process = [
  { title: 'Site Survey', description: 'Collect topographic data, soil tests and site conditions before design begins.' },
  { title: 'Blueprint & Design', description: 'Create detailed architectural and structural drawings for every component.' },
  { title: 'Regulatory Approval', description: 'Secure permits, environmental clearances and authority approvals efficiently.' },
  { title: 'Construction', description: 'Execute with skilled trade teams, modern equipment and strict quality control.' },
  { title: 'Inspection & Testing', description: 'Complete structural reviews, load tests and finishing inspections at every stage.' },
  { title: 'Handover', description: 'Deliver the finished project with full documentation, warranties and ongoing support.' },
]

const gallery = [
  'https://images.unsplash.com/photo-1541888946425-d81bb19240f5?auto=format&fit=crop&w=900&q=80',
  'https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=900&q=80',
  'https://images.unsplash.com/photo-1590846406792-0adc7f938f1d?auto=format&fit=crop&w=900&q=80',
]
</script>
