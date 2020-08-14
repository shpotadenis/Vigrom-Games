import { instance } from '../api'

const list_endpoint = '/api/news/'

export default {
    getListOfNews() {
        return instance.get(list_endpoint)
    },

    getNewsInfo(newsId) {
        return instance.get('/api/news/' + newsId + '/')
    },

    search(text) {
        let fd = new FormData()
        fd.append('dir', 'news')
        fd.append('search', text)
        return instance.post('/api/search', fd)
    }
}