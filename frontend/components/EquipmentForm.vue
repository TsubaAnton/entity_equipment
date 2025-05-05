<template>
  <form @submit.prevent="onSubmit" class="space-y-6">
    <div>
        <label class="block mb-2 font-semibold text-lg">Тип оборудования</label>
        <select v-model="form.type" class="border p-2 w-full rounded">
        <option v-for="t in types" :key="t.id" :value="t.id">{{ t.name }}</option>
      </select>
    </div>

    <div>
      <label>Серийные номера (каждый с новой строки)</label>
      <textarea v-model="snText" rows="3" class="border p-2 w-full rounded" />
    </div>

    <div>
      <label>Примечание</label>
      <textarea v-model="form.note" rows="2" class="border p-2 w-full rounded" />
    </div>

    <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded">{{ isEdit ? 'Сохранить' : 'Добавить' }}</button>
  </form>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import { useEquipment } from '../composables/useEquipment'
import { useNuxtApp } from '#app'
import { useRoute, useRouter } from 'vue-router'

const { fetchOne, create, update } = useEquipment()
const { $axios } = useNuxtApp()
const types = ref([])
const form = ref({ type: null, serials: [], note: '' })
const snText = ref('')
const route = useRoute()
const router = useRouter()
const isEdit = Boolean(route.params.id)

onMounted(async () => {
  const res = await $axios.get('/equipment-type')
  types.value = res.data.results
  if (isEdit) {
    const data = await fetchOne(route.params.id)
    form.value.type = data.type
    form.value.note = data.note
    snText.value = data.serials.join('\n')
  }
})

watch(snText, v => form.value.serials = v.split(/\r?\n/).filter(x => x))

const onSubmit = async () => {
  try {
    const payload = { type: form.value.type, serials: form.value.serials, note: form.value.note }
    if (isEdit) {
      await update(route.params.id, payload)
    } else {
      await create(payload)
    }
    router.push('/equipment')
  } catch (e) {
    alert(JSON.stringify(e.response?.data || e))
  }
}
</script>