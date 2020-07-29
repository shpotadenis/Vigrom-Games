const axios = require('axios')

export const instance = axios.create()
instance.defaults.baseURL = 'http://localhost:80'
instance.defaults.timeout = 1000

