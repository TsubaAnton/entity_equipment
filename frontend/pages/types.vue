<template>
  <div class="p-4">
    <h1 class="text-2xl mb-4">Типы оборудования</h1>
    <input v-model="query.search" @input="fetchTypes" placeholder="Поиск по наименованию или маске" class="p-2 mb-4 border" />
    <ul>
      <li v-for="type in list" :key="type.id">
        {{ type.id }} — {{ type.type_name }} (маска: {{ type.mask_sn }})
      </li>
    </ul>
    <div class="flex space-x-2 mt-4">
      <button v-if="meta.previous" @click="onPage(meta.page - 1)">Prev</button>
      <span>Стр. {{ meta.page }} из {{ meta.total_pages }}</span>
      <button v-if="meta.next" @click="onPage(meta.page + 1)">Next</button>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { useApi } from '~/composables/useApi'

const list = ref([])
const meta = reactive({ page: 1, total_pages: 1, next: null, previous: null })
const query = reactive({ page: 1, search: '' })
const { get } = useApi()

async function fetchTypes() {
  const { data } = await get('/api/equipment-type', query)
  list.value = data.value.results
  Object.assign(meta, data.value)
}

onMounted(fetchTypes)

function onPage(p) { query.page = p; fetchTypes() }
</script>