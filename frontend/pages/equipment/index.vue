<template>
  <div class="max-w-5xl mx-auto mt-10 p-6 bg-white rounded-lg shadow">
    <h1 class="text-4xl font-bold mb-6 text-center">Оборудование</h1>

    <div v-if="route.query.created" class="mb-4 text-green-600 text-center">
    </div>

    <div class="flex flex-col md:flex-row justify-between items-center mb-6 space-y-4 md:space-y-0 md:space-x-4">
      <input
        v-model="query.search"
        @input="fetchList"
        placeholder="Поиск по SN или примечанию"
        class="flex-1 p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400"
      />
      <button
        @click="goCreate"
        class="px-6 py-3 bg-green-500 text-white rounded-lg font-medium hover:bg-green-600"
      >
        Добавить
      </button>
    </div>

    <table class="w-full table-auto text-lg">
      <thead class="bg-gray-100">
        <tr>
          <th class="px-4 py-2">ID</th>
          <th class="px-4 py-2">Тип</th>
          <th class="px-4 py-2">SN</th>
          <th class="px-4 py-2">Примечание</th>
          <th class="px-4 py-2">Действия</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="item in list"
          :key="item.id"
          class="border-b hover:bg-gray-50"
        >
          <td class="px-4 py-3 text-center">{{ item.id }}</td>
          <td class="px-4 py-3">{{ item.equipment_type.type_name }}</td>
          <td class="px-4 py-3">{{ item.serial_number }}</td>
          <td class="px-4 py-3">{{ item.note }}</td>
          <td class="px-4 py-3 space-x-2 text-center">
            <button @click="edit(item.id)" class="px-2 py-1 bg-blue-400 text-white rounded hover:bg-blue-500">✏️</button>
            <button @click="remove(item.id)" class="px-2 py-1 bg-red-500 text-white rounded hover:bg-red-600">🗑️</button>
          </td>
        </tr>
      </tbody>
    </table>

    <div class="flex justify-center items-center mt-6 space-x-4">
      <button
        v-if="meta.previous"
        @click="onPage(meta.page - 1)"
        class="px-4 py-2 bg-gray-200 rounded hover:bg-gray-300"
      >Prev</button>
      <span class="text-lg">Стр. {{ meta.page }} из {{ meta.total_pages }}</span>
      <button
        v-if="meta.next"
        @click="onPage(meta.page + 1)"
        class="px-4 py-2 bg-gray-200 rounded hover:bg-gray-300"
      >Next</button>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useApi } from '~/composables/useApi'

const list = ref([])
const meta = reactive({ page: 1, total_pages: 1, next: null, previous: null })
const query = reactive({ page: 1, search: '' })

const router = useRouter()
const route = useRoute()
const { get, del } = useApi()

watch(
  () => route.path,
  (newPath) => {
    if (newPath === '/equipment') fetchList()
  }
)

watch(
  () => route.query.forceRefresh,
  () => {
    fetchList()
  }
)

async function fetchList() {
  try {
    const { data, error } = await get('/api/equipment', query)
    if (error.value) throw error.value
    const json = data.value
    list.value = json?.results || []
    meta.page = json?.page || 1
    meta.total_pages = json?.total_pages || 1
    meta.next = json?.next || null
    meta.previous = json?.previous || null
  } catch (e) {
    console.error('Fetch equipment error', e)
    list.value = []
    meta.page = 1
    meta.total_pages = 1
    meta.next = null
    meta.previous = null
  }
}

onMounted(fetchList)
watch(() => route.fullPath, fetchList)

onMounted(fetchList)
function onPage(p) { query.page = p; fetchList() }
function goCreate() { router.push('/equipment/create') }
function edit(id) { router.push(`/equipment/${id}`) }
async function remove(id) {
  if (confirm('Удалить?')) {
    await del(`/api/equipment/${id}`)
    fetchList()
  }
}
</script>
