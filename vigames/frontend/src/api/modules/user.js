import { instance } from '../api'


const login_endpoint = '/auth/token/login/'
const register_endpoint = '/auth/users/'
const role_endpoint = '/api/role'

export default {
    login(credentials)
    {
        let fd = new FormData()
        fd.append('username', credentials.login)
        fd.append('password', credentials.password)
        return instance.post(login_endpoint, fd).then(response => {
            console.log("Response")
            console.log(response)
        }).catch(error => {
            console.log("Error")
            console.log(error)
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
        let fd = new FormData()
        fd.append('username', name)
        fd.append('is_developer', isDev)
        return instance.post(role_endpoint, fd)
    }

}