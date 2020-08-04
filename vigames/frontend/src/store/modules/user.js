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

    register({commit}, credentials) {
        return new Promise( (resolve, reject) => {
            user.register(credentials).then(response => {

                resolve(response);
            })
                .catch(error => {
                    commit('userLogin', {
                        login: credentials.login,
                        token: 'dfsf'
                    })
                    console.log('error in store/modules/user.js:')
                    console.log(error)
                    reject(error)
                })
        });
    },

    changeRole({state}, data) {
        console.log(state)
        console.log(state.userLogin)
        user.setRole(state.userLogin, data.isDev).then(rsp => {
            console.log(rsp)
        }).catch(e => {
            console.log(e)
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