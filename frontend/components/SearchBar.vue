<template>
  <div class="mb-4">
    <input
      v-model="query"
      @keyup.enter="onSearch"
      type="text"
      placeholder="Поиск по SN или примечанию"
      class="border p-2 w-full rounded"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
const emit = defineEmits(['search'])
const query = ref('')
const onSearch = () => emit('search', query.value)
</script>