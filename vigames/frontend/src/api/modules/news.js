import { instance } from '../api'

const list_endpoint = '/api/news'
export default {
    getListOfNews() {
        return instance.get(list_endpoint)
    }
}