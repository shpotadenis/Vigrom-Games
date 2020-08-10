import { instance } from '../api'

const game_info_endpoint = '/api/games/'
const game_list_endpoint = '/api/main/new'

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
    }
}