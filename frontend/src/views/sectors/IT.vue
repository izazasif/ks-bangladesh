<template>
  <div>
    <!-- Hero -->
    <section class="relative overflow-hidden">
      <img
        src="https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1600&q=80"
        alt="IT & Technology"
        class="h-72 w-full object-cover md:h-96"
        loading="eager"
      />
      <div class="absolute inset-0 bg-gradient-to-r from-slate-950/90 via-slate-950/60 to-transparent"></div>
      <div class="absolute inset-0 flex flex-col justify-center px-6 sm:px-12 lg:px-20">
        <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">IT & Technology</p>
        <h1 class="mt-3 max-w-2xl text-4xl font-extrabold leading-tight text-white md:text-5xl">
          Driving digital transformation in Bangladesh
        </h1>
        <p class="mt-4 max-w-xl text-slate-300">
          Custom software, secure infrastructure and cloud services to modernize businesses and public services nationwide.
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
          <p class="mt-3 text-slate-500 max-w-2xl">End-to-end digital solutions tailored for Bangladeshi organizations ready to scale.</p>
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
          <h2 class="mt-3 text-3xl font-extrabold text-slate-900">Our Development Process</h2>
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
          <h2 class="mt-3 text-3xl font-extrabold text-slate-900">IT Projects Gallery</h2>
          <div class="mt-8 grid gap-4 lg:grid-cols-2">
            <img
              :src="gallery[0]"
              alt="IT"
              class="h-72 w-full rounded-3xl object-cover lg:h-full"
              loading="lazy"
            />
            <div class="grid gap-4">
              <img
                v-for="img in gallery.slice(1)"
                :key="img"
                :src="img"
                alt="IT"
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
        <h2 class="text-3xl font-extrabold text-white">Ready to digitally transform your organization?</h2>
        <p class="mx-auto mt-4 max-w-xl text-blue-100">Our technology team delivers robust, scalable solutions built for Bangladesh's rapidly evolving digital landscape.</p>
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
  { value: '200+', label: 'Software Projects' },
  { value: '50+', label: 'Cloud Deployments' },
  { value: '100+', label: 'Clients Served' },
  { value: '99.9%', label: 'Uptime SLA' },
]

const services = [
  { icon: '🖥️', title: 'Software Development', description: 'Custom web and mobile applications built to scale with your organization, from MVP to enterprise grade.' },
  { icon: '☁️', title: 'Cloud Solutions', description: 'Modern cloud migration, architecture and optimization on AWS, Azure and GCP for resilient operations.' },
  { icon: '🛡️', title: 'Cybersecurity', description: 'Comprehensive security audits, penetration testing and layered defenses to protect your systems and data.' },
  { icon: '📱', title: 'Digital Transformation', description: 'User-centric web portals, mobile apps and process automation to modernize how you work.' },
]

const process = [
  { title: 'Requirement Analysis', description: 'Discover business goals, workflows and technical priorities through structured workshops.' },
  { title: 'System Design', description: 'Architect scalable, maintainable and secure technology solutions with clear blueprints.' },
  { title: 'Development', description: 'Build iteratively with agile sprints, code reviews and automated testing pipelines.' },
  { title: 'Testing & QA', description: 'Validate security, performance, usability and integration across every module.' },
  { title: 'Deployment', description: 'Launch securely to production with CI/CD pipelines and zero-downtime strategies.' },
  { title: 'Ongoing Support', description: 'Maintain, monitor and optimize systems with dedicated support after launch.' },
]

const gallery = [
  'https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=900&q=80',
  'https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=900&q=80',
  'https://images.unsplash.com/photo-1535223289827-42f1e9919769?auto=format&fit=crop&w=900&q=80',
]
</script>
