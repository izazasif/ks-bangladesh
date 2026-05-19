import { ref } from 'vue'

const toasts = ref([])

export function useToast() {
  const addToast = (message, type = 'success') => {
    const id = Date.now().toString()
    toasts.value.push({ id, message, type })
    setTimeout(() => {
      toasts.value = toasts.value.filter((item) => item.id !== id)
    }, 4000)
  }
  return { toasts, addToast }
}
