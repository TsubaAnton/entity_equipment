<template>
  <div class="max-w-md mx-auto mt-20 p-6 bg-white rounded-lg shadow-lg">
    <h1 class="text-3xl font-semibold mb-6 text-center">Вход в систему</h1>
    <form @submit.prevent="onLogin" class="space-y-4">
      <input
        v-model="username"
        type="text"
        placeholder="Имя пользователя"
        required
        class="w-full p-3 border rounded"
      />
      <input
        v-model="password"
        type="password"
        placeholder="Пароль"
        required
        class="w-full p-3 border rounded"
      />
      <button
        type="submit"
        class="w-full py-3 bg-blue-600 text-white rounded-lg font-medium hover:bg-blue-700"
      >
        Войти
      </button>
      <p v-if="error" class="text-red-500 text-center">{{ error }}</p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useApi } from '~/composables/useApi'

const username = ref('')
const password = ref('')
const error = ref('')
const router = useRouter()
const { post } = useApi()

async function onLogin() {
  error.value = ''
  try {
    const { data, error: fetchError } = await post('/api/user/login', {
      username: username.value,
      password: password.value
    })

    if (fetchError.value || !data.value?.access) {
      error.value = 'Неверный логин или пароль'
      return
    }

    const access = data.value.access
    const refresh = data.value.refresh
    localStorage.setItem('access_token', access)
    localStorage.setItem('refresh_token', refresh)

    router.push('/equipment')
  } catch (err) {
    error.value = 'Ошибка соединения с сервером'
  }
}
</script>
