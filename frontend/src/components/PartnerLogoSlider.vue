<template>
  <section class="border-t border-slate-200 bg-white py-10">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="mb-8 text-center">
        <p class="text-sm uppercase tracking-[0.3em] text-primary">Partners</p>
        <h2 class="mt-3 text-3xl font-bold text-slate-900">Trusted by industry leaders</h2>
      </div>
      <Swiper
        :modules="[Autoplay]"
        :loop="true"
        :autoplay="{ delay: 2500, disableOnInteraction: false }"
        :slides-per-view="2"
        :breakpoints="{ 640: { slidesPerView: 3 }, 1024: { slidesPerView: 5 } }"
        space-between="24"
      >
        <SwiperSlide
          v-for="partner in partners"
          :key="partner.name"
          class="flex items-center justify-center py-2"
        >
          <div class="flex h-24 w-full cursor-default select-none items-center justify-center gap-3 rounded-3xl border border-slate-200 bg-slate-50 px-5 transition hover:border-primary/40 hover:bg-white hover:shadow-sm">
            <div
              :class="partner.color"
              class="flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-xl text-sm font-bold text-white"
            >
              {{ partner.initials }}
            </div>
            <span class="text-sm font-semibold leading-tight text-slate-700">{{ partner.name }}</span>
          </div>
        </SwiperSlide>
      </Swiper>
    </div>
  </section>
</template>

<script setup>
import { Swiper, SwiperSlide } from 'swiper/vue'
import { Autoplay } from 'swiper/modules'

const partners = [
  { name: 'AgriTech BD', initials: 'AT', color: 'bg-green-600' },
  { name: 'LogiCorp', initials: 'LC', color: 'bg-blue-600' },
  { name: 'InfraBuild', initials: 'IB', color: 'bg-orange-600' },
  { name: 'CloudOps', initials: 'CO', color: 'bg-purple-600' },
  { name: 'GreenFields', initials: 'GF', color: 'bg-emerald-600' },
  { name: 'TrackWay', initials: 'TW', color: 'bg-cyan-600' },
  { name: 'DataBridge', initials: 'DB', color: 'bg-indigo-600' },
  { name: 'BuildPlus', initials: 'BP', color: 'bg-amber-600' },
]
</script>
