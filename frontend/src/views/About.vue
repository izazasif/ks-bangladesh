<template>
  <div>
    <!-- Hero -->
    <section class="relative overflow-hidden">
      <img
        src="https://images.unsplash.com/photo-1600880292203-757bb62b4baf?auto=format&fit=crop&w=1600&q=80"
        alt="About KSI Bangladesh"
        class="h-72 w-full object-cover md:h-96"
        loading="eager"
      />
      <div class="absolute inset-0 bg-gradient-to-r from-slate-950/90 via-slate-950/60 to-transparent"></div>
      <div class="absolute inset-0 flex flex-col justify-center px-6 sm:px-12 lg:px-20">
        <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Who We Are</p>
        <h1 class="mt-3 max-w-2xl text-4xl font-extrabold leading-tight text-white md:text-5xl">
          Driving growth across Bangladesh since 2010
        </h1>
        <p class="mt-4 max-w-xl text-slate-300">A multi-sector company committed to agriculture, technology, infrastructure and logistics.</p>
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

    <div class="space-y-0 bg-slate-50">

      <!-- Mission & Vision -->
      <section class="mx-auto max-w-6xl px-4 py-16 sm:px-6 lg:px-8">
        <div class="rounded-[35px] bg-white p-10 shadow-soft">
          <div class="grid gap-10 lg:grid-cols-2 lg:items-center">
            <div>
              <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Our Purpose</p>
              <h2 class="mt-4 text-4xl font-extrabold leading-tight text-slate-900">
                KSI Bangladesh is a multi-sector company committed to driving growth across Bangladesh.
              </h2>
              <p class="mt-6 text-lg leading-relaxed text-slate-500">We support agriculture, IT, construction and transportation with integrated solutions designed for long-term impact, local economies and national priorities.</p>
            </div>
            <div class="grid gap-5 sm:grid-cols-2">
              <div class="rounded-3xl border border-slate-200 bg-lightblue p-7">
                <div class="mb-3 text-2xl">🎯</div>
                <h3 class="text-xl font-bold text-slate-900">Mission</h3>
                <p class="mt-3 text-slate-600">Empower organizations across Bangladesh through sustainable services, innovation and collaborative delivery.</p>
              </div>
              <div class="rounded-3xl bg-slate-950 p-7">
                <div class="mb-3 text-2xl">🌟</div>
                <h3 class="text-xl font-bold text-white">Vision</h3>
                <p class="mt-3 text-slate-300">To be the trusted partner for growth in agriculture, technology, infrastructure and transportation nationwide.</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- How We Work -->
      <section class="mx-auto max-w-6xl px-4 pb-16 sm:px-6 lg:px-8">
        <div class="rounded-[35px] bg-white p-10 shadow-soft">
          <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Our Approach</p>
          <h2 class="mt-3 text-3xl font-extrabold text-slate-900">How We Work</h2>
          <div class="mt-10 grid gap-6 lg:grid-cols-2">
            <div
              v-for="sector in sectors"
              :key="sector.title"
              class="rounded-3xl border border-slate-200 bg-slate-50 p-7 transition hover:border-primary/30 hover:shadow-sm"
            >
              <div class="flex items-center gap-3">
                <span class="text-2xl">{{ sector.icon }}</span>
                <h3 class="text-xl font-bold text-slate-900">{{ sector.title }}</h3>
              </div>
              <ol class="mt-5 space-y-2">
                <li v-for="(step, i) in sector.steps" :key="step" class="flex items-start gap-3 text-sm text-slate-600">
                  <span class="flex h-6 w-6 flex-shrink-0 items-center justify-center rounded-full bg-primary text-xs font-bold text-white">{{ i + 1 }}</span>
                  {{ step }}
                </li>
              </ol>
            </div>
          </div>
        </div>
      </section>

      <!-- Team & Values -->
      <section class="mx-auto max-w-6xl px-4 pb-16 sm:px-6 lg:px-8">
        <div class="grid gap-8 lg:grid-cols-2">

          <!-- Team -->
          <div class="rounded-[35px] bg-white p-10 shadow-soft">
            <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Our People</p>
            <h2 class="mt-3 text-3xl font-extrabold text-slate-900">Leadership Team</h2>
            <p class="mt-3 text-slate-500">Meet the people driving KSI Bangladesh's mission across all four sectors.</p>
            <div class="mt-8 grid gap-4 sm:grid-cols-2">
              <div
                v-for="member in team"
                :key="member.name"
                class="rounded-3xl border border-slate-100 bg-slate-50 p-6 transition hover:border-primary/20 hover:shadow-sm"
              >
                <div :class="member.color" class="h-14 w-14 rounded-2xl text-2xl font-bold flex items-center justify-center">{{ member.initials }}</div>
                <h3 class="mt-4 text-lg font-bold text-slate-900">{{ member.name }}</h3>
                <p class="mt-0.5 text-sm font-semibold text-primary">{{ member.role }}</p>
                <p class="mt-2 text-xs leading-relaxed text-slate-500">{{ member.bio }}</p>
              </div>
            </div>
          </div>

          <!-- Values -->
          <div class="rounded-[35px] bg-white p-10 shadow-soft">
            <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">What We Stand For</p>
            <h2 class="mt-3 text-3xl font-extrabold text-slate-900">Our Values</h2>
            <p class="mt-3 text-slate-500">The principles that guide everything we do at KSI Bangladesh.</p>
            <div class="mt-8 space-y-4">
              <div
                v-for="value in values"
                :key="value.title"
                class="flex items-start gap-4 rounded-3xl border border-slate-100 bg-slate-50 p-6 transition hover:border-primary/20"
              >
                <div class="flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-2xl bg-primary/10 text-2xl">{{ value.icon }}</div>
                <div>
                  <h3 class="text-lg font-bold text-slate-900">{{ value.title }}</h3>
                  <p class="mt-1 text-sm leading-relaxed text-slate-500">{{ value.description }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>

    <!-- CTA -->
    <section class="bg-primary py-16">
      <div class="mx-auto max-w-4xl px-4 text-center sm:px-6">
        <h2 class="text-3xl font-extrabold text-white">Ready to work with KSI Bangladesh?</h2>
        <p class="mx-auto mt-4 max-w-xl text-blue-100">Whether you're in agriculture, IT, construction or transportation — we have a solution for you.</p>
        <div class="mt-8 flex flex-wrap justify-center gap-3">
          <router-link to="/contact" class="inline-flex rounded-full bg-white px-8 py-4 text-sm font-bold text-primary shadow-lg transition hover:bg-slate-100">Contact Us</router-link>
          <router-link to="/services" class="inline-flex rounded-full border border-white/40 px-8 py-4 text-sm font-bold text-white transition hover:bg-white/10">View Services</router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
const stats = [
  { value: '15+', label: 'Years of Experience' },
  { value: '500+', label: 'Projects Completed' },
  { value: '4', label: 'Core Sectors' },
  { value: '50+', label: 'Partner Organizations' },
]

const sectors = [
  { icon: '🌾', title: 'Agriculture', steps: ['Field Assessment', 'Crop Planning', 'Resource Allocation', 'Harvest Support', 'Post-harvest Logistics'] },
  { icon: '💻', title: 'IT', steps: ['Requirement Analysis', 'System Design', 'Development', 'Testing & QA', 'Deployment & Support'] },
  { icon: '🏗️', title: 'Construction', steps: ['Site Survey', 'Blueprint & Design', 'Regulatory Approval', 'Construction', 'Inspection & Handover'] },
  { icon: '🚛', title: 'Transportation', steps: ['Route Analysis', 'Fleet Assignment', 'Real-time Tracking', 'Delivery Confirmation', 'Reporting'] },
]

const team = [
  { initials: 'AN', name: 'Ayesha Noor', role: 'Chief Operations Officer', bio: 'Over 15 years leading cross-sector operations across Bangladesh with a focus on sustainable delivery.', color: 'bg-primary/10 text-primary' },
  { initials: 'MR', name: 'Mohammad Rafiq', role: 'Technical Director', bio: 'Software architect specialising in cloud infrastructure and digital transformation.', color: 'bg-emerald-100 text-emerald-700' },
  { initials: 'SZ', name: 'Sadia Zaman', role: 'Head of Project Management', bio: 'PMP-certified manager with a strong record delivering construction and agri-tech initiatives.', color: 'bg-purple-100 text-purple-700' },
  { initials: 'KM', name: 'Kamal Mahmud', role: 'Logistics & Transportation Lead', bio: 'Expert in fleet management and supply chain optimisation across every region.', color: 'bg-amber-100 text-amber-700' },
]

const values = [
  { icon: '🤝', title: 'Integrity', description: 'We operate transparently and deliver on our commitments without compromise.' },
  { icon: '💡', title: 'Innovation', description: 'We adopt modern tools and ideas for lasting improvement in every sector.' },
  { icon: '📊', title: 'Impact', description: 'Our work is focused on measurable outcomes for communities and clients.' },
  { icon: '🌍', title: 'Inclusion', description: 'We support diverse clients, partners and local talent across Bangladesh.' },
]
</script>
