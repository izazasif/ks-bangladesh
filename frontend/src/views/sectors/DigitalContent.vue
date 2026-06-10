<template>
  <div>
    <!-- Hero -->
    <section class="relative overflow-hidden">
      <img
        src="https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?auto=format&fit=crop&w=1600&q=80"
        alt="Digital Content Services KSI Bangladesh"
        class="h-[420px] w-full object-cover md:h-[520px]"
        loading="eager"
      />
      <div class="absolute inset-0 bg-gradient-to-r from-slate-950/90 via-slate-950/60 to-transparent"></div>
      <div class="absolute inset-0 flex flex-col justify-center px-6 sm:px-12 lg:px-24">
        <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Our Sector</p>
        <h1 class="mt-3 max-w-2xl text-4xl font-extrabold leading-tight text-white md:text-5xl lg:text-6xl">Digital Content</h1>
        <p class="mt-4 max-w-xl text-lg text-slate-300">We create and provide digital content and documentary for government and private sector.</p>
        <div class="mt-8 flex flex-wrap gap-4">
          <router-link to="/contact" class="inline-flex rounded-full bg-primary px-8 py-4 text-sm font-bold text-white shadow-lg transition hover:bg-blue-700">Start a Project</router-link>
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
        <h2 class="mt-3 text-3xl font-extrabold text-slate-900 md:text-4xl">Our Digital Content Services</h2>
        <p class="mx-auto mt-4 max-w-2xl text-slate-500">We create compelling content and manage digital channels that build trust, grow followers and convert audiences into clients.</p>
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
          <h2 class="mt-3 text-3xl font-extrabold text-slate-900 md:text-4xl">Our Content Process</h2>
        </div>
        <div class="mt-14 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
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
        <img v-for="img in gallery" :key="img" :src="img" alt="Digital content work" class="h-56 w-full rounded-[24px] object-cover transition hover:scale-[1.02]" loading="lazy" />
      </div>
    </section>

    <!-- CTA -->
    <section class="bg-primary py-20">
      <div class="mx-auto max-w-4xl px-4 text-center sm:px-6 lg:px-8">
        <h2 class="text-3xl font-extrabold text-white md:text-4xl">Ready to grow your digital presence?</h2>
        <p class="mx-auto mt-4 max-w-xl text-lg text-blue-100">Let's build content that speaks to your audience and drives real results for your brand.</p>
        <router-link to="/contact" class="mt-8 inline-flex items-center rounded-full bg-white px-10 py-4 text-sm font-bold text-primary shadow-lg transition hover:bg-slate-100">
          Let's Talk →
        </router-link>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useSEO } from '../../composables/useSEO'

useSEO({
  title: 'Digital Content Services',
  description: 'KSI Bangladesh creates compelling content, manages social media channels and builds brand identities that grow your digital presence across Bangladesh.',
  keywords: 'digital content Bangladesh, content creation, social media management, video production, graphic design, KSI digital',
  path: '/sectors/digital-content',
})

const stats = [
  { value: '200+', label: 'Campaigns Delivered' },
  { value: '50+', label: 'Brands Served' },
  { value: '1M+', label: 'Audience Reached' },
  { value: '5+', label: 'Years in Digital' },
]

const services = [
  { icon: '✍️', title: 'Content Creation', description: 'Blog posts, website copy, scripts and articles that inform, engage and convert your target audience.' },
  { icon: '📱', title: 'Social Media Management', description: 'Full management of Facebook, LinkedIn and YouTube — from strategy and posting to community engagement.' },
  { icon: '🎬', title: 'Video Production', description: 'Corporate videos, product demos and reels that bring your brand story to life with professional quality.' },
  { icon: '🎨', title: 'Design & Branding', description: 'Logos, brand guidelines, infographics and visual assets that build a consistent and memorable identity.' },
]

const process = [
  { title: 'Brand Discovery', description: 'Understand your brand voice, audience, goals and competitive landscape.' },
  { title: 'Content Strategy', description: 'Build a content calendar, platform plan and messaging framework.' },
  { title: 'Production', description: 'Create written, visual and video content to the highest quality standards.' },
  { title: 'Publishing & Distribution', description: 'Schedule and publish content across all relevant platforms.' },
  { title: 'Analytics & Reporting', description: 'Track performance metrics and refine the strategy for continuous growth.' },
  { title: 'Optimization', description: 'A/B test content, improve engagement and scale what works.' },
]

const gallery = [
  'https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?auto=format&fit=crop&w=900&q=80',
  'https://images.unsplash.com/photo-1557838923-2985c318be48?auto=format&fit=crop&w=900&q=80',
  'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?auto=format&fit=crop&w=900&q=80',
]
</script>
