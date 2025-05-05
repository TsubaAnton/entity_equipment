<template>
  <div v-if="form" class="max-w-xl mx-auto p-4">
    <h2 class="text-xl mb-4">Редактировать оборудование #{{ form.id }}</h2>
    <form @submit.prevent="save">
      <label>Тип оборудования</label>
      <input v-model="form.equipment_type" disabled class="w-full mb-2 p-2 border bg-gray-100" />
      <label>Серийный номер</label>
      <input v-model="form.serial_number" disabled class="w-full mb-2 p-2 border bg-gray-100" />
      <label>Примечание</label>
      <textarea v-model="form.note" rows="2" class="w-full mb-4 p-2 border"></textarea>
      <button type="submit" class="p-2 bg-blue-600 text-white mr-2">Сохранить</button>
      <button type="button" @click="remove" class="p-2 bg-red-600 text-white">Удалить</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useApi } from '~/composables/useApi'

const route = useRoute()
const id = route.params.id
const form = ref(null)
const router = useRouter()
const { get, put, del } = useApi()

onMounted(async () => {
  const { data } = await get(`/api/equipment/${id}`)
  form.value = data.value
})

async function save() {
  await put(`/api/equipment/${id}`, form.value)
  alert('Сохранено')
}

async function remove() {
  if (confirm('Удалить?')) {
    await del(`/api/equipment/${id}`)
    router.push('/equipment')
  }
}
</script>