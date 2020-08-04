import { instance } from '../api'


const login_endpoint = '/auth/token/login/'
const register_endpoint = '/auth/users/'
const role_endpoint = '/api/role'

export default {
    login(credentials)
    {
        return instance.post(login_endpoint, {
            'username': credentials.login,
            'password': credentials.password
        })
    },

    register(credentials)
    {
        return instance.post(register_endpoint, {
            'username': credentials.login,
            'password': credentials.password,
            'email': credentials.email
        })
    },

    setRole(name, isDev) {
        return instance.post(role_endpoint, {
            username: name,
            "is_developer": isDev
        })
    }

}