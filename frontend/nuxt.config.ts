export default {
  css: ['~/assets/css/tailwind.css'],
  modules: ['@nuxtjs/tailwindcss'],
  runtimeConfig: {
    public: { apiBase: 'http://localhost:8000' }
  }
}