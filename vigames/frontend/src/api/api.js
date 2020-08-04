const axios = require('axios')

export const instance = axios.create()
instance.defaults.baseURL = 'http://localhost:8000'
instance.defaults.timeout = 1000000

instance.interceptors.request.use(r => {
    console.log("DEBUG (request):")
    console.log(r)
    return r
})

