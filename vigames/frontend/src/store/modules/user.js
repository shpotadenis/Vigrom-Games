import user from '../../api/modules/user'

const state = () => ({
    userLogin: null,
    token: null,
    loggedIn: false
});

const getters = {
    isLoggedIn(state) {
        return state.loggedIn
    },

    getToken(state) {
        return state.token
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
            commit('userLogin', {
                login: credentials.username,
                token: response.data.auth_token
            });
        })
        .catch(error => {
            console.log('error in store/modules/user.js:')
            console.log(error)
        })
    },

    register(context, credentials) {
        user.register(credentials).then(response => {
            if (response.data.id) {
                context.dispatch('login', credentials)
            }
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