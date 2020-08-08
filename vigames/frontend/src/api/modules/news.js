import { instance } from '../api'

const list_endpoint = '/api/news'

export default {
    getListOfNews() {
        return instance.get(list_endpoint)
    },

    getNewsInfo(newsId) {
        return instance.get('/api/news/' + newsId)
    }
}