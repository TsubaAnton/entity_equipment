export function useApi() {
  const config = useRuntimeConfig()
  const apiBase = config.public.apiBase

  function get(path, params) {
    return useFetch(path, {
      baseURL: apiBase,
      method: 'get',
      params,
      headers: { Authorization: `Bearer ${localStorage.getItem('access_token') || ''}` }
    })
  }

  function post(path, body) {
    return useFetch(path, {
      baseURL: apiBase,
      method: 'post',
      body,
      headers: { Authorization: `Bearer ${localStorage.getItem('access_token') || ''}` }
    })
  }

  function put(path, body) {
    return useFetch(path, {
      baseURL: apiBase,
      method: 'put',
      body,
      headers: { Authorization: `Bearer ${localStorage.getItem('access_token') || ''}` }
    })
  }

  function del(path) {
    return useFetch(path, {
      baseURL: apiBase,
      method: 'delete',
      headers: { Authorization: `Bearer ${localStorage.getItem('access_token') || ''}` }
    })
  }

  return { get, post, put, del }
}

