import Vue from 'vue'
import App from './App.vue'
import Router from 'vue-router'
import store from './store/store.js'
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap-grid.min.css';
import GameSinglePage from "./pages/GameSinglePage/index.vue";
import LoginPage from "./pages/LoginPage/index.vue";
import NewsPage from "./pages/NewsGamePage/NewsPage";
import HomePage from "./pages/HomeGamePage/HomePage.vue";
import SignInPage from "./pages/SignInPage/index.vue"
import SignUpRolePage from "./pages/SignUpRolePage/index.vue"
import Checkout from "./components/Pop-ups/Checkout/checkout.vue"
import VueAwesomeSwiper from 'vue-awesome-swiper'
import 'swiper/swiper-bundle.css'
import LibraryPage from "./pages/LibraryPage/index.vue"
import VueScrollTo from 'vue-scrollto'
import FeaturedPage from './pages/FeaturedPage/index.vue'
import NewsSinglePage from "./pages/NewsSinglePage/index.vue"
import FreeGames from "./pages/FreeGames/FreeGames.vue"

Vue.use(VueScrollTo)

Vue.use(VueAwesomeSwiper);

Vue.use(Router);

Vue.config.productionTip = false

const router = new Router({
  routes: [
    { path: '/login', name: 'loginPage', component: LoginPage },
    { path: '/shop', name: 'singlePage', component: GameSinglePage },
    { path: '/home', name: 'homePage', component: HomePage },
    { path: '/news', name: 'newsPage', component: NewsPage },
    { path: '/sign_in', name: 'signInPage', component: SignInPage },
    { path: '/sign_up_next', name: 'signUpRolePage', component: SignUpRolePage },
    { path: '/checkout', name: 'checkout', component: Checkout },
    { path: '/library', name: 'libraryPage', component: LibraryPage },
    { path: '/featured', name: 'featuredPage', component: FeaturedPage },
    { path: '/separate_news', name: 'newsSinglePage', component: NewsSinglePage },
    { path: '/free_games', name: 'freeGames', component: FreeGames}

  ]
})

new Vue({
  render: h => h(App),
  router,
  store
}).$mount('#app')
