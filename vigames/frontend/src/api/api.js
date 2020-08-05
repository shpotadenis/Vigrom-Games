const axios = require('axios')
import vue from '../main'


export const instance = axios.create()
instance.defaults.baseURL = 'http://localhost:8000'
instance.defaults.timeout = 1000000

instance.interceptors.request.use(r => {
    // DEBUG logs
    console.log("DEBUG (request):")
    console.log(r)

    // auth
    let token = vue.$store.getters['user/getToken']
    if (token != null) {
        r.headers['Authorization'] = 'Token ' + token
    }

    return r
})

