//import { ref } from 'vue'
//import { useNuxtApp } from '#app'
//
//export function useEquipment() {
//  const { $axios } = useNuxtApp()
//  const list = ref([])
//  const pagination = ref({ page: 1, pageCount: 1, total: 0 })
//  const error = ref(null)
//
//  const fetchList = async (page = 1, search = '') => {
//    try {
//      const res = await $axios.get('/equipment', { params: { page, search } })
//      list.value = res.data.results
//      pagination.value.page = page
//      pagination.value.pageCount = Math.ceil(res.data.count / 10)
//      pagination.value.total = res.data.count
//    } catch (e) { error.value = e.response?.data || e }
//  }
//
//  const fetchOne = async id => {
//    try {
//      const res = await $axios.get(`/equipment/${id}`)
//      return res.data
//    } catch (e) { throw e }
//  }
//
//  const create = async payload => {
//    try {
//      return await $axios.post('/equipment', payload)
//    } catch (e) { throw e }
//  }
//
//  const update = async (id, payload) => {
//    try {
//      return await $axios.put(`/equipment/${id}`, payload)
//    } catch (e) { throw e }
//  }
//
//  const remove = async id => {
//    try {
//      return await $axios.delete(`/equipment/${id}`)
//    } catch (e) { throw e }
//  }
//
//  return { list, pagination, error, fetchList, fetchOne, create, update, remove }
//}