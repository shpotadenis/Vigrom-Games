import user from '../../api/modules/user'

const state = () => ({
    userLogin: null,
    token: null,
    loggedIn: false
});

const getters = {
    isLoggedIn(state) {
        return state.loggedIn
    }
};

const mutations = {
    userLogin(state, user) {
        state.userLogin = user.login
        state.token = user.token
        state.loggedIn = true
    },

    userLogout(state) {
        state.userLogin = null
        state.token = null
        state.loggedIn = false
    }
};

const actions = {
    login({ commit }, credentials) {
        user.login(credentials).then(response => {
            commit('userLogin', response.data);
        })
        .catch(error => {
            console.log('error in store/modules/user.js:')
            console.log(error)
        })
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}