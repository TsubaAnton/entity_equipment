import { defineNuxtPlugin, useRuntimeConfig, navigateTo } from '#app'
import axios from 'axios'

export default defineNuxtPlugin(() => {
  const config = useRuntimeConfig()
  const instance = axios.create({
    baseURL: config.public.apiBase
  })
  instance.interceptors.request.use(req => {
    const token = localStorage.getItem('token')
    if (token) {
      req.headers.Authorization = `Bearer ${token}`
    }
    return req
  })
  instance.interceptors.response.use(
    res => res,
    err => {
      if (err.response?.status === 401) {
        localStorage.removeItem('token')
        navigateTo('/login')
      }
      return Promise.reject(err)
    }
  )

  return { provide: { axios: instance } }
})