import { instance } from '../api'


const login_endpoint = '/auth/token/login/'
const register_endpoint = '/auth/users/'
const role_endpoint = '/api/role'
const library_endpoint = '/api/accounts/profile/library'
const changepass_endpoint = '/auth/users/set_password/'
const changename_endpoint = '/auth/users/set_username/'

export default {
    login(credentials)
    {
        let fd = new FormData()
        fd.append('username', credentials.login)
        fd.append('password', credentials.password)

        return instance.post(login_endpoint, fd)
    },

    register(credentials)
    {
        let fd = new FormData()
        fd.append('username', credentials.login)
        fd.append('password', credentials.password)
        fd.append('email', credentials.email)

        return instance.post(register_endpoint, fd)
    },

    setRole(name, isDev) {
        let fd = new FormData()
        fd.append('username', name)
        fd.append('is_developer', isDev)

        return instance.post(role_endpoint, fd)
    },

    getGamesLibrary() {
        return instance.get(library_endpoint)
    },

    changePassword(credentials) {
        let fd = new FormData()
        fd.append('new_password', credentials.new_password)
        fd.append('re_new_password', credentials.new_password)
        fd.append('current_password', credentials.current_password)

        return instance.post(changepass_endpoint, fd)
    },

    changeName(credentials) {
        let fd = new FormData()
        fd.append('new_username', credentials.username)
        fd.append('current_password', credentials.password)

        return instance.post(changename_endpoint, fd)
    }

}