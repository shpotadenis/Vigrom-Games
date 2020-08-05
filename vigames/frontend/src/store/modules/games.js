import games from '../../api/modules/games'

const state = () => ({
    all: []
});

const getters = {
    getGame: (state) => (id) => {
        if (state.all) {
            let game = state.all.filter(g => g.id == id)
            if (game != null) {
                return game[0]
            }
        }
    }
};

const mutations = {
    addGame(state, game) {
        state.all.push(game)
    }
};

const actions = {
    loadGame(context, data) {
        return new Promise((resolve, reject) => {
            games.getGameInfo(data.id).then(response => {
                if (response.data) {
                    response.data.id = data.id
                    context.commit('addGame', response.data)
                    resolve(response.data)
                }
            }).catch(error => {
                if (error) {
                    reject(error)
                }
            })
        });
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}