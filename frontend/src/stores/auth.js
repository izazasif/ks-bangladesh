import { defineStore } from 'pinia'
import { login as apiLogin, refresh as apiRefresh, logout as apiLogout, fetchMe } from '../api/auth'
import { setAuthToken } from '../api/client'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    accessToken: null,
    user: null,
    isAuthenticated: false,
    loading: false,
  }),
  actions: {
    async login(payload) {
      this.loading = true
      try {
        const response = await apiLogin(payload)
        this.accessToken = response.data.access_token
        this.isAuthenticated = true
        setAuthToken(this.accessToken)
        await this.loadProfile()
        return response
      } finally {
        this.loading = false
      }
    },
    async restoreSession() {
      if (this.isAuthenticated) {
        return true
      }
      this.loading = true
      try {
        const response = await apiRefresh()
        this.accessToken = response.data.access_token
        this.isAuthenticated = true
        setAuthToken(this.accessToken)
        await this.loadProfile()
        return true
      } catch (error) {
        this.clearSession()
        return false
      } finally {
        this.loading = false
      }
    },
    async loadProfile() {
      try {
        const response = await fetchMe()
        this.user = response.data
      } catch (error) {
        this.clearSession()
      }
    },
    async logout() {
      await apiLogout().catch(() => {})
      this.clearSession()
    },
    clearSession() {
      this.accessToken = null
      this.user = null
      this.isAuthenticated = false
      setAuthToken(null)
    },
  },
})
