<template>
  <div>
    <!-- Hero Banner Slider -->
    <BannerSlider />

    <!-- Stats Bar -->
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

    <!-- About Section — split image/text -->
    <section class="mx-auto max-w-7xl px-4 py-20 sm:px-6 lg:px-8">
      <div class="grid items-center gap-12 lg:grid-cols-2 lg:gap-20">
        <div>
          <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Who We Are</p>
          <h2 class="mt-4 text-4xl font-extrabold leading-tight text-slate-900">
            A trusted multi-sector company driving growth across Bangladesh
          </h2>
          <p class="mt-6 text-lg leading-relaxed text-slate-500">
            KSI Bangladesh delivers integrated solutions across agriculture, IT, construction and transportation — with a strong commitment to sustainable development and national progress.
          </p>
          <div class="mt-8 grid grid-cols-2 gap-5">
            <div v-for="point in aboutPoints" :key="point.title" class="flex items-start gap-3">
              <div class="flex h-9 w-9 flex-shrink-0 items-center justify-center rounded-full bg-primary/10 text-lg">{{ point.icon }}</div>
              <div>
                <p class="text-sm font-bold text-slate-900">{{ point.title }}</p>
                <p class="mt-0.5 text-xs leading-relaxed text-slate-500">{{ point.description }}</p>
              </div>
            </div>
          </div>
          <router-link to="/about" class="mt-10 inline-flex items-center gap-2 rounded-full bg-primary px-7 py-3.5 text-sm font-semibold text-white shadow-md transition hover:bg-blue-700">
            Learn About Us
            <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
          </router-link>
        </div>

        <div class="relative pt-6 pl-6">
          <img
            src="https://images.unsplash.com/photo-1600880292203-757bb62b4baf?auto=format&fit=crop&w=900&q=80"
            alt="KSI Bangladesh team"
            class="h-[500px] w-full rounded-[32px] object-cover shadow-xl"
            loading="lazy"
          />
          <div class="absolute -bottom-4 -left-2 rounded-2xl bg-white p-5 shadow-xl border border-slate-100">
            <p class="text-3xl font-black text-primary">15+</p>
            <p class="mt-1 text-sm font-medium text-slate-600">Years of Experience</p>
          </div>
          <div class="absolute -top-2 right-4 rounded-2xl bg-primary p-5 shadow-xl">
            <p class="text-3xl font-black text-white">500+</p>
            <p class="mt-1 text-sm font-medium text-blue-200">Projects Completed</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Services — image cards -->
    <section class="bg-slate-50 py-20">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="mb-12 text-center">
          <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Our Services</p>
          <h2 class="mt-3 text-4xl font-extrabold text-slate-900">Solutions in every sector</h2>
          <p class="mx-auto mt-4 max-w-xl text-lg text-slate-500">
            Tailored services across Bangladesh's key industries — delivered by local experts.
          </p>
        </div>
        <div class="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
          <div
            v-for="service in services"
            :key="service.title"
            class="group relative overflow-hidden rounded-[28px] shadow-soft"
          >
            <img
              :src="service.image"
              :alt="service.title"
              class="h-80 w-full object-cover transition duration-500 group-hover:scale-105"
              loading="lazy"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-900/60 to-transparent"></div>
            <div class="absolute inset-x-0 bottom-0 p-6">
              <div class="mb-3 inline-flex h-10 w-10 items-center justify-center rounded-xl bg-white/20 text-xl backdrop-blur-sm">{{ service.icon }}</div>
              <h3 class="text-lg font-bold text-white">{{ service.title }}</h3>
              <p class="mt-2 text-sm leading-relaxed text-slate-300">{{ service.description }}</p>
              <router-link
                :to="service.link"
                class="mt-4 inline-flex items-center gap-1 text-sm font-semibold text-primary transition-all hover:gap-2"
              >
                Explore →
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Sector Slider -->
    <SectorSlider />

    <!-- Why Choose Us — full image background -->
    <section class="relative overflow-hidden py-24">
      <img
        src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1600&q=80"
        alt=""
        class="absolute inset-0 h-full w-full object-cover"
        loading="lazy"
      />
      <div class="absolute inset-0 bg-primary/90"></div>
      <div class="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="text-center">
          <p class="text-sm font-bold uppercase tracking-[0.3em] text-blue-200">Why Choose Us</p>
          <h2 class="mt-3 text-4xl font-extrabold text-white">Built for Bangladesh's growth</h2>
          <p class="mx-auto mt-4 max-w-2xl text-blue-100">
            Deep local knowledge combined with modern expertise to deliver real, measurable impact for every client.
          </p>
        </div>
        <div class="mt-14 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
          <div
            v-for="feature in features"
            :key="feature.title"
            class="rounded-[24px] border border-white/20 bg-white/10 p-7 text-center backdrop-blur-sm transition hover:bg-white/15"
          >
            <div class="mx-auto mb-4 flex h-14 w-14 items-center justify-center rounded-2xl bg-white/20 text-3xl">{{ feature.icon }}</div>
            <h3 class="text-lg font-bold text-white">{{ feature.title }}</h3>
            <p class="mt-3 text-sm leading-relaxed text-blue-100">{{ feature.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Impact Image Strip -->
    <section class="grid h-64 grid-cols-4 overflow-hidden sm:h-80">
      <div v-for="strip in imageStrip" :key="strip.label" class="group relative overflow-hidden">
        <img :src="strip.image" :alt="strip.label" class="h-full w-full object-cover transition duration-500 group-hover:scale-110" loading="lazy" />
        <div class="absolute inset-0 bg-slate-950/50 transition group-hover:bg-slate-950/30"></div>
        <div class="absolute inset-0 flex items-end p-4">
          <span class="text-sm font-bold uppercase tracking-wider text-white">{{ strip.label }}</span>
        </div>
      </div>
    </section>

    <!-- Partner Logo Slider -->
    <PartnerLogoSlider />

    <!-- CTA Banner -->
    <section class="relative overflow-hidden bg-slate-950">
      <img
        src="https://images.unsplash.com/photo-1448932223592-d1fc686e76ea?auto=format&fit=crop&w=1600&q=80"
        alt=""
        class="absolute inset-0 h-full w-full object-cover opacity-10"
        loading="lazy"
      />
      <div class="relative mx-auto flex max-w-7xl flex-col items-center justify-between gap-10 px-4 py-24 sm:px-6 lg:flex-row lg:px-8">
        <div>
          <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Ready to work with us?</p>
          <h2 class="mt-4 text-4xl font-extrabold leading-tight text-white lg:text-5xl">
            Partner with KSI Bangladesh<br class="hidden lg:block" /> for sustainable growth.
          </h2>
          <p class="mt-5 max-w-lg text-slate-400">
            Join hundreds of clients across Bangladesh who trust KSI for reliable, impactful, and innovative multi-sector solutions.
          </p>
        </div>
        <div class="flex flex-shrink-0 flex-col gap-3 sm:flex-row">
          <router-link to="/contact" class="inline-flex items-center justify-center rounded-full bg-primary px-8 py-4 text-sm font-semibold text-white shadow-lg transition hover:bg-blue-600">
            Contact Us
          </router-link>
          <router-link to="/services" class="inline-flex items-center justify-center rounded-full border border-white/30 px-8 py-4 text-sm font-semibold text-white transition hover:bg-white/10">
            View Services
          </router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import BannerSlider from '../components/BannerSlider.vue'
import SectorSlider from '../components/SectorSlider.vue'
import PartnerLogoSlider from '../components/PartnerLogoSlider.vue'
import { useSEO } from '../composables/useSEO'

useSEO({
  title: 'Multi-Sector Company in Bangladesh',
  description: 'KSI Bangladesh delivers expert services in Agriculture, IT, Construction and Transportation. Serving businesses, NGOs and government bodies since 2010.',
  keywords: 'KSI Bangladesh, multi-sector company, agriculture, IT, construction, transportation, Bangladesh',
  path: '/',
})

const stats = [
  { value: '15+', label: 'Years of Experience' },
  { value: '500+', label: 'Projects Completed' },
  { value: '5', label: 'Key Sectors' },
  { value: '50+', label: 'Partner Organizations' },
]

const aboutPoints = [
  { icon: '🏆', title: 'Proven Track Record', description: 'Trusted by businesses, government bodies and NGOs.' },
  { icon: '🌍', title: 'Nationwide Coverage', description: 'Active across Dhaka, Chattogram, Rajshahi and beyond.' },
  { icon: '💡', title: 'Innovative Approach', description: 'Modern tools and strategies tailored for the local market.' },
  { icon: '🤝', title: 'Strong Partnerships', description: 'A network of industry leaders and community stakeholders.' },
]

const services = [
  {
    icon: '🌾',
    title: 'Agriculture Advisory',
    description: 'Crop planning, irrigation and agri-tech services tailored for Bangladesh.',
    image: 'https://images.unsplash.com/photo-1625246333195-78d9c38ad449?auto=format&fit=crop&w=900&q=80',
    link: '/sectors/agriculture',
  },
  {
    icon: '💻',
    title: 'IT Development',
    description: 'Custom software, cloud transformation and secure digital platforms.',
    image: 'https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=900&q=80',
    link: '/sectors/it',
  },
  {
    icon: '🏗️',
    title: 'Construction',
    description: 'Infrastructure planning, civil engineering and project supervision.',
    image: 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=900&q=80',
    link: '/sectors/construction',
  },
  {
    icon: '📦',
    title: 'Supplier',
    description: 'Procurement, vendor management and materials supply for every project scale.',
    image: 'https://images.unsplash.com/photo-1553413077-190dd305871c?auto=format&fit=crop&w=900&q=80',
    link: '/sectors/supplier',
  },
  {
    icon: '🎬',
    title: 'Digital Content',
    description: 'Content creation, social media management and brand storytelling that drives results.',
    image: 'https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?auto=format&fit=crop&w=900&q=80',
    link: '/sectors/digital-content',
  },
]

const features = [
  { icon: '⭐', title: 'Trusted Expertise', description: 'Decades of combined sector experience and deep local market knowledge.' },
  { icon: '📍', title: 'Nationwide Reach', description: 'Active projects across Dhaka, Chattogram, Rajshahi, Sylhet and rural Bangladesh.' },
  { icon: '🔗', title: 'Multi-Sector Solutions', description: 'Integrated services that create value across all four key industries.' },
  { icon: '💡', title: 'Client First', description: 'Full transparency, speed and measurable outcomes on every engagement.' },
]

const imageStrip = [
  { label: 'Agriculture', image: 'https://images.unsplash.com/photo-1625246333195-78d9c38ad449?auto=format&fit=crop&w=600&q=80' },
  { label: 'IT & Technology', image: 'https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=600&q=80' },
  { label: 'Construction', image: 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=600&q=80' },
  { label: 'Transportation', image: 'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=600&q=80' },
]
</script>
