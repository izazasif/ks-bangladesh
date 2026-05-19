<template>
  <div class="fixed inset-x-0 top-4 z-50 flex flex-col items-center gap-2 px-4 pointer-events-none">
    <transition-group name="toast" tag="div">
      <div
        v-for="toast in toasts"
        :key="toast.id"
        :class="['max-w-lg w-full pointer-events-auto rounded-2xl border p-4 shadow-soft', toast.type === 'error' ? 'border-red-200 bg-red-50 text-red-700' : 'border-slate-200 bg-white text-slate-900']"
      >
        <p class="text-sm leading-6">{{ toast.message }}</p>
      </div>
    </transition-group>
  </div>
</template>

<script setup>
import { useToast } from '../composables/useToast'
const { toasts } = useToast()
</script>

<style scoped>
.toast-enter-active,
.toast-leave-active {
  transition: all 0.3s ease;
}
.toast-enter-from,
.toast-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>
