import Vue from 'vue'
import vuex from 'vuex'
import user from './modules/user'
import news from './modules/news'
import games from './modules/games'
import VuexPersistence from "vuex-persist";

Vue.use(vuex)


const vuexLocal = new VuexPersistence({
    storage: window.localStorage,
    reducer: (state) => ({
        user: state.user
    })
})

export default new vuex.Store({
    modules: {
        user,
        news,
        games
    },
    plugins: [vuexLocal.plugin]
})

