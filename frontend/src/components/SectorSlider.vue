<template>
  <section class="py-14 bg-white">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="mb-10 flex flex-col items-start gap-2 sm:flex-row sm:items-end sm:justify-between">
        <div>
          <p class="text-sm font-bold uppercase tracking-[0.3em] text-primary">Sector Highlights</p>
          <h2 class="mt-2 text-3xl font-extrabold text-slate-900">Explore what we deliver</h2>
        </div>
        <router-link to="/services" class="text-sm font-semibold text-primary hover:underline">
          View all services →
        </router-link>
      </div>

      <Swiper
        :modules="[Autoplay, Navigation]"
        :loop="true"
        :autoplay="{ delay: 4500, disableOnInteraction: false }"
        :navigation="true"
        :breakpoints="{
          0: { slidesPerView: 1, spaceBetween: 16 },
          640: { slidesPerView: 2, spaceBetween: 20 },
          1024: { slidesPerView: 3, spaceBetween: 24 }
        }"
        class="pb-4"
      >
        <SwiperSlide v-for="item in cards" :key="item.title">
          <div class="group overflow-hidden rounded-[28px] border border-slate-100 bg-white shadow-soft transition hover:-translate-y-1 hover:shadow-lg">
            <div class="relative h-52 overflow-hidden">
              <img
                :src="item.image"
                :alt="item.title"
                class="h-full w-full object-cover transition duration-500 group-hover:scale-105"
                loading="lazy"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-slate-900/50 to-transparent"></div>
              <span class="absolute bottom-3 left-4 rounded-full bg-white/20 px-3 py-1 text-xs font-semibold uppercase tracking-wider text-white backdrop-blur-sm">
                {{ item.sector }}
              </span>
            </div>
            <div class="p-6">
              <h3 class="text-lg font-bold text-slate-900">{{ item.title }}</h3>
              <p class="mt-2 text-sm leading-relaxed text-slate-500">{{ item.description }}</p>
              <router-link
                :to="item.link"
                class="mt-4 inline-flex items-center gap-1 text-sm font-semibold text-primary transition hover:gap-2"
              >
                Learn more
                <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
              </router-link>
            </div>
          </div>
        </SwiperSlide>
      </Swiper>
    </div>
  </section>
</template>

<script setup>
import { Swiper, SwiperSlide } from 'swiper/vue'
import { Autoplay, Navigation } from 'swiper/modules'

const cards = [
  {
    sector: 'Agriculture',
    title: 'Agriculture Innovation',
    description: 'Precision farming, crop yield optimization and rural enterprise development across Bangladesh.',
    image: 'https://images.unsplash.com/photo-1625246333195-78d9c38ad449?auto=format&fit=crop&w=900&q=80',
    link: '/sectors/agriculture',
  },
  {
    sector: 'IT',
    title: 'IT Solutions',
    description: 'Scalable software, cloud migration and cybersecurity for growing organizations.',
    image: 'https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=900&q=80',
    link: '/sectors/it',
  },
  {
    sector: 'Construction',
    title: 'Construction Projects',
    description: 'Civil engineering, infrastructure planning and safe execution across Bangladesh.',
    image: 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=900&q=80',
    link: '/sectors/construction',
  },
  {
    sector: 'Transportation',
    title: 'Transportation Network',
    description: 'Logistics, fleet management and cargo movement with intelligent route planning.',
    image: 'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=900&q=80',
    link: '/sectors/transportation',
  },
]
</script>
