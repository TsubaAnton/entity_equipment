<template>
  <div class="flex justify-center mt-4">
    <button
      @click="change(page - 1)"
      :disabled="page <= 1"
      class="px-3 py-1 border rounded mr-2"
    >&lt;</button>
    <span class="px-3 py-1">{{ page }} / {{ pageCount }}</span>
    <button
      @click="change(page + 1)"
      :disabled="page >= pageCount"
      class="px-3 py-1 border rounded ml-2"
    >&gt;</button>
  </div>
</template>

<script setup>
const props = defineProps({ page: Number, pageCount: Number })
const emit = defineEmits(['change'])
const change = p => { if (p >=1 && p <= props.pageCount) emit('change', p) }
</script>