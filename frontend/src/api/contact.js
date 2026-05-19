import apiClient from './client'

export function submitContact(payload) {
  return apiClient.post('/contact', payload)
}
