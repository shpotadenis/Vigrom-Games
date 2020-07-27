import { instance } from '../api'


const login_endpoint = '/login'
export default {
    login(credentials)
    {
        return instance.post(login_endpoint, credentials)
    }
}