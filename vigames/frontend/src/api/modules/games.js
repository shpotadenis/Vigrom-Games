import { instance } from '../api'

const game_info_endpoint = '/api/games/'
const game_list_endpoint = '/api/main/new'
const recomendation_list_endpoint = '/api/main/recommended'

export default {
    getGameInfo(id) {
        return instance.get(game_info_endpoint + id)
    },

    getListOfGames() {
        return instance.get(game_list_endpoint)
    },

    // DEPRECATED
    getReviews(gameId) {
        return instance.get('/api/games/' + gameId + '/rating')
    },

    getByGenre(genre) {
        return instance.get('/api/genre/' + genre)
    },

    getRecommendation() {
        return instance.get(recomendation_list_endpoint)
    },

    search(text) {
        let fd = new FormData()
        fd.append('search', text)
        fd.append('dir', 'games')
        return instance.post('/api/search', fd)
    },

    getTopInGenre(genre) {
        return instance.get('/api/genre/' + genre + '/top')
    }
}
