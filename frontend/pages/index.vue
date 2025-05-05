<template>
  <div class="flex items-center justify-center h-screen text-gray-600">
    Redirecting to <NuxtLink to="/login" class="text-blue-500">Login</NuxtLink>...
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

onMounted(() => {
  router.replace('/login')
})
</script>