import user from '../../api/modules/user'


const state = () => ({
    userLogin: null, // string - логин пользователя
    isDev: false, // boolean - является ли разработчиком
    isRoleSelected: false, // boolean - выбрана ли роль
    token: null, // string - JWT токен для авторизации
    loggedIn: false, // boolean - выполнен ли вход (авторизация)
    library: {}, // object - Библиотека пользователя
    wishlist: {}  // object - избранное пользователя
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
    },

    getUserName(state) {
        return state.userLogin
    },

    getWishlist(state) {
        return state.wishlist
    },

    isInWishlist: (state) => (gameId) => {
        return state.wishlist.some(g => g.id == gameId)
    },

    isGamePurchased: (state) => (gameId) => {
        return state.library.some(g => g.id == gameId)
    },
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
        state.isDev = false
        state.isRoleSelected = false
        state.token = null
        state.loggedIn = false
        state.library = {}
        state.wishlist = {}
        window.localStorage.clear()
    },

    setUserRole(state, isDev) {
        if (state.isRoleSelected == false) {
            state.isRoleSelected = true;
        }
        state.isDev = isDev
    },

    addLibrary(state, library) {
        state.library = library
    },

    addWishlist(state, wishlist) {
        state.wishlist = wishlist
    },

    changeName(state, newName) {
        state.userLogin = newName
    },

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
                    context.dispatch('afterLoginEvents')
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

    // Выполняет загрузку необходимых данных после того, как пользователь авторизовался
    afterLoginEvents(context) {
        // Загрузка библиотеки
        context.dispatch('getLibrary')

        // Загрузка wishlist
        context.dispatch('getWishlist')
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
    },

    getWishlist({commit}) {
      return new Promise((resolve, reject) => {
         user.getWishlist().then(response => {
             if (response) {
                 commit('addWishlist', response.data)
                 resolve(response)
             }
         }).catch(error => {
             reject(error)
         })
      });
    },

    addToWishlist(context, data) {
        return new Promise((resolve, reject) => {
            user.addToWishlist(data.gameId).then(response => {
                context.dispatch('getWishlist')
                resolve(response)
            }).catch(error => {
                reject(error)
            })
        })
    },

    removeFromWishlist(context, data) {
        return new Promise((resolve, reject) => {
            user.removeFromWishlist(data.gameId).then(response => {
                context.dispatch('getWishlist')
                resolve(response)
            }).catch(error => {
                reject(error)
            })
        })
    },

    changePassword(context, data) {
        return new Promise((resolve, reject) => {
            user.changePassword(data).then(response => {
                if (response) {
                    resolve(response)
                }
            }).catch(error => {
                reject(error.response)
            })
        })
    },

    changeName(context, data) {
        return new Promise((resolve, reject) => {
            user.changeName(data).then(response => {
                if (response) {
                    resolve(response.data)
                    context.commit('changeName', data.username)
                }
            }).catch(error => {
                reject(error.response)
            })
        })
    },

    buyGame(context, data) {
        return new Promise((resolve, reject) => {
            user.buyGame(data.gameId).then(response => {
                if (response) {
                    resolve(response.data)
                    context.dispatch('getWishlist')
                    context.dispatch('getLibrary')
                }
            }).catch(error => {
                console.log(error)
                reject(error)
            })
        })
    },

    addReview(context, data) {
        return new Promise((resolve, reject) => {
            user.createReview(data.gameId, data).then(response => {
                resolve(response)
            }).catch(error => {
                console.log(error.response)
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