<template>
  <div class="flex items-center gap-3">
    <svg :width="size" :height="size" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
      <!-- Dark arc — left, curves outward -->
      <path d="M22 68 C13 54 13 46 22 32" :stroke="darkArc" stroke-width="10" stroke-linecap="round"/>
      <!-- Blue arc 1 — curves left -->
      <path d="M36 75 C27 58 27 42 36 25" :stroke="blueArc" stroke-width="10" stroke-linecap="round"/>
      <!-- Blue arc 2 — center, tallest, straight -->
      <path d="M50 78 C50 59 50 41 50 22" :stroke="blueArc" stroke-width="10" stroke-linecap="round"/>
      <!-- Blue arc 3 — curves right, mirrors arc 1 -->
      <path d="M64 75 C73 58 73 42 64 25" :stroke="blueArc" stroke-width="10" stroke-linecap="round"/>
    </svg>
    <div class="leading-none">
      <p class="text-[22px] font-black tracking-[-0.03em]" :class="dark ? 'text-white' : 'text-slate-900'">KSI</p>
      <p class="text-[9px] font-bold uppercase tracking-[0.28em] -mt-0.5" :class="dark ? 'text-blue-300' : 'text-primary'">Bangladesh</p>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  dark: { type: Boolean, default: false },
  size: { type: Number, default: 44 },
})

const darkArc = computed(() => props.dark ? 'rgba(255,255,255,0.85)' : '#1e293b')
const blueArc = computed(() => props.dark ? '#93c5fd' : '#1A56DB')
</script>
