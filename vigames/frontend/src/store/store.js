import Vue from 'vue'
import vuex from 'vuex'
import user from './modules/user'
import news from './modules/news'
import games from './modules/games'

Vue.use(vuex)

export default new vuex.Store({
    modules: {
        user,
        news,
        games
    }
})

