import { instance } from '../api'


const login_endpoint = '/auth/token/login'
const register_endpoint = '/auth/users'

export default {
    login(credentials)
    {
        return instance.post(login_endpoint, credentials)
    },

    register(credentials)
    {
        return instance.post(register_endpoint, credentials)
    }

}