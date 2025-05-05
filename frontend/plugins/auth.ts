export default defineNuxtPlugin((nuxtApp) => {
  if (process.client) {
    const token = localStorage.getItem('access_token')
    if (token) {
      nuxtApp.$api = (url, options = {}) => {
        options.headers = {
          ...(options.headers || {}),
          Authorization: `Bearer ${token}`,
        }
        return $fetch(url, options)
      }
    }
  }
})
