<template>
  <section class="relative overflow-hidden">
    <Swiper
      :modules="[Autoplay, EffectFade, Pagination]"
      effect="fade"
      :loop="true"
      :autoplay="{ delay: 6000, disableOnInteraction: false }"
      :pagination="{ clickable: true }"
      class="h-[580px] md:h-[640px]"
    >
      <SwiperSlide v-for="slide in slides" :key="slide.title">
        <div class="relative h-full w-full">
          <img
            :src="slide.image"
            :alt="slide.title"
            class="h-full w-full object-cover"
            loading="eager"
          />
          <!-- Gradient overlay -->
          <div class="absolute inset-0 bg-gradient-to-r from-slate-950/80 via-slate-950/50 to-transparent"></div>

          <!-- Content -->
          <div class="absolute inset-0 flex flex-col justify-center px-6 sm:px-12 lg:px-20">
            <div class="max-w-2xl">
              <span class="inline-flex items-center gap-2 rounded-full border border-white/20 bg-white/10 px-4 py-1.5 text-xs font-bold uppercase tracking-[0.2em] text-white backdrop-blur-sm">
                {{ slide.sector }}
              </span>
              <h2 class="mt-5 text-4xl font-extrabold leading-tight text-white sm:text-5xl lg:text-6xl">
                {{ slide.title }}
              </h2>
              <p class="mt-4 max-w-xl text-base leading-relaxed text-slate-200 sm:text-lg">
                {{ slide.subtitle }}
              </p>
              <div class="mt-8 flex flex-wrap gap-3">
                <router-link
                  :to="slide.link"
                  class="inline-flex items-center gap-2 rounded-full bg-primary px-6 py-3 text-sm font-semibold text-white shadow-lg transition hover:bg-blue-700"
                >
                  Explore {{ slide.sector }}
                  <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                </router-link>
                <router-link
                  to="/contact"
                  class="inline-flex items-center rounded-full border border-white/40 bg-white/10 px-6 py-3 text-sm font-semibold text-white backdrop-blur-sm transition hover:bg-white/20"
                >
                  Contact Us
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </SwiperSlide>
    </Swiper>
  </section>
</template>

<script setup>
import { Swiper, SwiperSlide } from 'swiper/vue'
import { Autoplay, EffectFade, Pagination } from 'swiper/modules'

const slides = [
  {
    sector: 'Agriculture',
    title: 'Empowering Farmers Across Bangladesh',
    subtitle: 'Sustainable crop management, irrigation planning and agri-tech for every rural community.',
    image: 'https://images.unsplash.com/photo-1625246333195-78d9c38ad449?auto=format&fit=crop&w=1600&q=80',
    link: '/sectors/agriculture',
  },
  {
    sector: 'IT & Technology',
    title: 'Driving Digital Transformation',
    subtitle: 'Custom software, cloud infrastructure and cybersecurity for growing Bangladeshi businesses.',
    image: 'https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1600&q=80',
    link: '/sectors/it',
  },
  {
    sector: 'Construction',
    title: "Building Bangladesh's Future",
    subtitle: 'Civil engineering, infrastructure and project delivery — built safely and on schedule.',
    image: 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=1600&q=80',
    link: '/sectors/construction',
  },
  {
    sector: 'Transportation',
    title: 'Connecting Every Corner of Bangladesh',
    subtitle: 'Reliable logistics, fleet management and cargo movement across every region.',
    image: 'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=1600&q=80',
    link: '/sectors/transportation',
  },
]
</script>
