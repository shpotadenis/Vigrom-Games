import user from '../../api/modules/user'

const state = () => ({
    userLogin: null, // string - логин пользователя
    isDev: false, // boolean - является ли разработчиком
    isRoleSelected: false, // boolean - выбрана ли роль
    token: null, // string - JWT токен для авторизации
    loggedIn: false, // boolean - выполнен ли вход (авторизация)
    library: {}
});

const getters = {
    isLoggedIn(state) {
        return state.loggedIn
    },

    getToken(state) {
        return state.token
    },

    isDeveloper(state) {
        return state.isDev
    },

    getLibrary(state) {
        return state.library
    }
};

const mutations = {
    userLogin(state, user) {
        state.userLogin = user.login

        if (user.token != null) {
            state.token = user.token
            state.loggedIn = true
        }
    },

    userLogout(state) {
        state.userLogin = null
        state.token = null
        state.loggedIn = false
    },

    setUserRole(state, isDev) {
        if (state.isRoleSelected == false) {
            state.isRoleSelected = true;
        }
        state.isDev = isDev
    },

    addLibrary(state, library) {
        state.library = library
    }
};

const actions = {
    login(context, credentials) {
        return new Promise((resolve, reject) => {
            user.login(credentials).then(response => {
                // Ответ получен, токен существует
                if (response.data.auth_token) {
                    context.commit('userLogin', {
                        login: credentials.login,
                        token: response.data.auth_token
                    });
                    resolve(response.data)
                }
                else { // В ответе нет токена, но код ответа не содержит ошибки
                    reject(response.data)
                }
            }).catch(error => {
                reject(error.response.data)
            })
        });
    },

    register({commit}, credentials) {
        return new Promise( (resolve, reject) => {
            user.register(credentials).then(response => {
                // Ответ получен, пользователь создан
                if (response.data.id) {
                    commit('userLogin', {
                        login: credentials.login
                    })
                    resolve(response.data);
                }
                else { // Ответ получен, но пользователь не зарегистрирован
                    reject(response.data)
                }
            }).catch(error => {
                reject(error.response.data)
            })
        });
    },

    changeRole({commit, state}, data) {
        return new Promise((resolve, reject) => {
            user.setRole(state.userLogin, data.isDev).then(rsp => {
                commit('setUserRole', data.isDev)
                resolve(rsp.data)
            }).catch(e => {
                reject(e.response.data)
            })
        });
    },

    getLibrary({commit}) {
        return new Promise((resolve, reject) => {
            user.getGamesLibrary().then(response => {
                if (response) {
                    commit('addLibrary', response.data)
                    resolve(response)
                }
            }).catch(error => {
                reject(error)
            })
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