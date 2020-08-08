const axios = require('axios')
import vue from '../main.js'


export const apiUrl = 'http://localhost:8000'
export const instance = axios.create()
instance.defaults.baseURL = apiUrl // 'http://13.94.157.21:8000' - for test in remote
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

instance.interceptors.response.use((response) => {
    return response
}, error => {

    if (error.response.status == 401 && vue.$store.getters['user/isLoggedIn']) {
        vue.$store.commit('user/userLogout')
    }

    return Promise.reject(error)
});
instance.interceptors.response.use((response) => {
    return response
}, error => {

    if (error.response.status == 401 && vue.$store.getters['user/isLoggedIn']) {
        vue.$store.commit('user/userLogout')
        vue.$router.push({
            name: 'signInPage'
        })
    }

    return Promise.reject(error)
});