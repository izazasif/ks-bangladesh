import apiClient from './client'

export function getStats() {
  return apiClient.get('/admin/stats')
}

export function getUsers(params = {}) {
  return apiClient.get('/users', { params })
}

export function getContacts(params = {}) {
  return apiClient.get('/contact', { params })
}
