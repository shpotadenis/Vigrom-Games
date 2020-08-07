import { instance } from '../api'

const game_info_endpoint = '/api/games/'
const game_list_endpoint = '/api/'

export default {
    getGameInfo(id) {
        return instance.get(game_info_endpoint + id)
    },

    getListOfGames() {
        return instance.get(game_list_endpoint)
    },

    getReviews(gameId) {
        return instance.get('/api/games/' + gameId + '/rating')
    }
}