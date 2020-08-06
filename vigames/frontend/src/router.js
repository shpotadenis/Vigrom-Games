import Router from 'vue-router'
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
import LibraryPage from "./pages/LibraryPage/index.vue"
import GameSinglePage from "./pages/GameSinglePage/index.vue";
import LoginPage from "./pages/LoginPage/index.vue";
import NewsPage from "./pages/NewsGamePage/NewsPage";
import HomePage from "./pages/HomeGamePage/HomePage.vue";
import SignInPage from "./pages/SignInPage/index.vue"
import SignUpRolePage from "./pages/SignUpRolePage/index.vue"
import Checkout from "./components/Pop-ups/Checkout/checkout.vue"
import Vue from "vue";

Vue.use(Router);

export const router = new Router({
    // TODO: Добавить " meta: { requiresAuth: true } " к страницам, требующим авторизации
    routes: [
        { path: '/login', name: 'loginPage', component: LoginPage },
        { path: '/game/:id', name: 'singlePage', component: GameSinglePage },
        { path: '/', name: 'homePage', component: HomePage },
        { path: '/news', name: 'newsPage', component: NewsPage },
        { path: '/sign_in', name: 'signInPage', component: SignInPage },
        { path: '/sign_up_next', name: 'signUpRolePage', component: SignUpRolePage },
        { path: '/checkout', name: 'checkout', component: Checkout },
        { path: '/library', name: 'libraryPage', component: LibraryPage, meta: { requiresAuth: true } },
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
        { path: '/upload', name: 'uploadPage', component: UploadPage }
    ]
})

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        // this route requires auth, check if logged in
        // if not, redirect to login page.
        if (!router.app.$store.getters['user/isLoggedIn']) {
            next({
                path: '/sign_in',
                query: { redirect: to.fullPath }
            })
        } else {
            next()
        }
    } else {
        next() // make sure to always call next()!
    }
})
