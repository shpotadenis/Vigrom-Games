import { instance } from '../api'

const game_info_endpoint = '/api/games/'

export default {
    getGameInfo(id) {
        return instance.get(game_info_endpoint + id)
    }
}