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
import ErrorPage from './pages/ErrorPage/index.vue'
import FreeGames from "./pages/FreeGames/FreeGames.vue"
import DiscountsGame from "./pages/DiscountsGame/DiscountGame";
import EarlyAccessGame from "./pages/EarlyAccessGame/EarlyAccessGame.vue";
import PersonPage from './pages/PersonPage/index.vue'
import DeveloperPage from './pages/DeveloperPage/index.vue'
import UploadPage from './pages/UploadPage/index.vue'
import ForgotPass from './pages/ForgotPass/index.vue'
import ActionGame from './pages/GerneGame/ActionGame/ActionGame.vue'
import AdventuresGame from './pages/GerneGame/AdventuresGame/AdventuresGames.vue'
import FarmGame from './pages/GerneGame/FarmGame/FarmGame.vue'
import MMOGame from './pages/GerneGame/MMOGame/MMOGame.vue'
import PuzzleGame from './pages/GerneGame/PuzzleGame/PuzzleGame.vue'
import RaceGame from './pages/GerneGame/RaceGame/RaceGame.vue'
import RPGGame from './pages/GerneGame/RPGGame/RPGGame.vue'
import ShooterGame from './pages/GerneGame/ShooterGame/ShooterGame.vue'
import SimulatorGame from './pages/GerneGame/SimulatorGame/SimulatorGame.vue'
import StrategyGame from './pages/GerneGame/StrategyGame/StrategyGame.vue'

Vue.use(VueScrollTo)

Vue.use(VueAwesomeSwiper);

Vue.use(Router);

Vue.config.productionTip = false

const router = new Router({
  routes: [
    { path: '/login', name: 'loginPage', component: LoginPage },
    { path: '/game/:id', name: 'singlePage', component: GameSinglePage },
    { path: '/', name: 'homePage', component: HomePage },
    { path: '/news', name: 'newsPage', component: NewsPage },
    { path: '/sign_in', name: 'signInPage', component: SignInPage },
    { path: '/sign_up_next', name: 'signUpRolePage', component: SignUpRolePage },
    { path: '/checkout', name: 'checkout', component: Checkout },
    { path: '/library', name: 'libraryPage', component: LibraryPage },
    { path: '/featured', name: 'featuredPage', component: FeaturedPage },
    { path: '/free_games', name: 'freeGames', component: FreeGames},
    { path: '/separate_news', name: 'newsSinglePage', component: NewsSinglePage },
    { path: '/not_found', name: 'errorPage', component: ErrorPage },
    { path: '/discountsGame', name: 'discountsGame', component: DiscountsGame },
    { path: '/earlyAccess', name: 'earlyAccessGame', component: EarlyAccessGame },
    { path: '/user_profile', name: 'personPage', component: PersonPage },
    { path: '/developer_profile', name: 'DeveloperPage', component: DeveloperPage },
    { path: '/forgot_pass', name: 'forgotPass', component: ForgotPass },
    { path: '/developer_profile', name: 'DeveloperPage', component: DeveloperPage },
    { path: '/ActionGame', name: 'ActionGame', component: ActionGame },
    { path: '/AdventuresGame', name: 'AdventuresGame', component: AdventuresGame },
    { path: '/FarmGame', name: 'FarmGame', component: FarmGame },
    { path: '/MMOGame', name: 'MMOGame', component: MMOGame },
    { path: '/PuzzleGame', name: 'PuzzleGame', component: PuzzleGame },
    { path: '/RaceGame', name: 'RaceGame', component: RaceGame },
    { path: '/RPGGame', name: 'RPGGame', component: RPGGame },
    { path: '/ShooterGame', name: 'ShooterGame', component: ShooterGame },
    { path: '/SimulatorGame', name: 'SimulatorGame', component: SimulatorGame },
    { path: '/StrategyGame', name: 'StrategyGame', component: StrategyGame },
    { path: '/UploadPage', name: 'uploadPage', component: UploadPage }
  ]
})

export default new Vue({
  render: h => h(App),
  router,
  store
}).$mount('#app')
