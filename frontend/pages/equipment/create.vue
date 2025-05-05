<template>
  <div class="max-w-xl mx-auto p-4">
    <h2 class="text-xl mb-4">Добавить оборудование</h2>
    <form @submit.prevent="submit">
      <label>Тип оборудования</label>
      <select v-model="form.equipment_type" required class="w-full mb-2 p-2 border">
        <option v-for="t in types" :key="t.id" :value="t.id">{{ t.type_name }}</option>
      </select>
      <label>Серийные номера (каждый с новой строки)</label>
      <textarea v-model="form.serial_numbers" rows="5" required class="w-full mb-2 p-2 border"></textarea>
      <label>Примечание</label>
      <textarea v-model="form.note" rows="2" class="w-full mb-4 p-2 border"></textarea>
      <button type="submit" class="p-2 bg-blue-600 text-white">Добавить</button>
    </form>
    <ul v-if="errors.length" class="mt-4 text-red-600">
      <li v-for="e in errors" :key="e">{{ e }}</li>
    </ul>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useApi } from '~/composables/useApi'
import { validateMask } from '~/utils/mask'

const types = ref([])
const errors = ref([])
const form = reactive({ equipment_type: null, serial_numbers: '', note: '' })

const router = useRouter()
const { get, post } = useApi()

onMounted(async () => {
  const { data } = await get('/api/equipment-type')
  types.value = data.value.results
})

async function submit() {
  errors.value = []
  const sns = form.serial_numbers.split(/\r?\n/).map(s => s.trim()).filter(Boolean)
  const mask = types.value.find(t => t.id === form.equipment_type)?.mask_sn || ''
  const invalid = sns.filter(sn => !validateMask(sn, mask))
  if (invalid.length) {
    errors.value = invalid.map(sn => `Неверный SN: ${sn}`)
    return
  }

  const payload = sns.map(sn => ({
    equipment_type: form.equipment_type,
    serial_number: sn,
    note: form.note
  }))

  try {
    const { error } = await post('/api/equipment', payload)

    if (error.value) {
      errors.value = error.value.data
      return
    }

    router.push({
      path: '/equipment',
      query: { forceRefresh: Date.now() }
    })

  } catch (e) {
    errors.value = e.data || ['Ошибка при создании']
  }
}
</script>
