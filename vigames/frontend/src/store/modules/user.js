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
    login(context, credentials) {
        return new Promise((resolve, reject) => {
            user.login(credentials).then(response => {
                console.log(response)
                resolve(response)
            }).catch(error => {
                console.log(error)
                context.commit('userLogin', {
                    login: credentials.username,
                    token: error.response.data.auth_token
                });
                reject(error)
            })
        });
    },

    register({commit}, credentials) {
        return new Promise( (resolve, reject) => {
            user.register(credentials).then(response => {
                commit('userLogin', {
                    login: credentials.login
                })
                resolve(response);
            }).catch(error => {

                    reject(error)
                })
        });
    },

    changeRole({state}, data) {
        return new Promise((resolve, reject) => {
            user.setRole(state.userLogin, data.isDev).then(rsp => {
                resolve(rsp)
            }).catch(e => {
                reject(e)
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