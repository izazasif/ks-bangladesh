import apiClient from './client'

export function register(payload) {
  return apiClient.post('/auth/register', payload)
}

export function login(payload) {
  return apiClient.post('/auth/login', payload)
}

export function refresh() {
  return apiClient.post('/auth/refresh')
}

export function logout() {
  return apiClient.post('/auth/logout')
}

export function fetchMe() {
  return apiClient.get('/auth/me')
}

export function updateUser(userId, payload) {
  return apiClient.put(`/users/${userId}`, payload)
}
