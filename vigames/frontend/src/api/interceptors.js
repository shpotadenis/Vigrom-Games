import { vue } from "../main";
import  { instance } from './api'

instance.interceptors.request.use(req => {
    let token = vue.$store.getters['user/getToken'];
    if (token != null) {
        req.headers['Authorization'] = 'Token ' + token;
    }
    return req;
})