import Router from 'vue-router'
import FeaturedPage from './pages/FeaturedPage/index.vue'
import NewsSinglePage from "./pages/NewsSinglePage/index.vue"
import ErrorPage404 from './pages/ErrorPage404/index.vue'
import ErrorPage403 from './pages/ErrorPage403/index.vue'
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
import NewsPage from "./pages/NewsGamePage/NewsPage.vue";
import HomePage from "./pages/HomeGamePage/HomePage.vue";
import SignInPage from "./pages/SignInPage/index.vue"
import SignUpRolePage from "./pages/SignUpRolePage/index.vue"
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
import ChangePass from './components/Pop-ups/ChangePass/index.vue'
import Checkout from './components/Pop-ups/Checkout/checkout.vue'
import GameDownloaded from './components/Pop-ups/GameDownloaded/index.vue'
import GoDownload from './components/Pop-ups/GoDownload/index.vue'
import MessageSent from './components/Pop-ups/MessageSent/index.vue'
import PasswordChanged from './components/Pop-ups/PasswordChanged/index.vue'
import PasswordReset from './components/Pop-ups/PasswordReset/index.vue'
import Support from './components/Pop-ups/Support/index.vue'
import Vue from "vue";


Vue.use(Router);

export const router = new Router({
    // TODO: Добавить " meta: { requiresAuth: true } " к страницам, требующим авторизации
    // TODO: Добавить " meta: { requiredRole: 'dev' } " к страницам, доступным только для разработчиков (для пользователя аналогичное пока недоступно)
    routes: [
        { path: '/home', name: 'homePage', component: HomePage },
        { path: '/login', name: 'loginPage', component: LoginPage },
        { path: '/game/:id', name: 'singlePage', component: GameSinglePage },
        { path: '/news', name: 'newsPage', component: NewsPage },
        { path: '/sign_in', name: 'signInPage', component: SignInPage },
        { path: '/sign_up_next', name: 'signUpRolePage', component: SignUpRolePage },
        { path: '/library', name: 'libraryPage', component: LibraryPage, meta: { requiresAuth: true } },
        { path: '/featured', name: 'featuredPage', component: FeaturedPage, meta: { requiresAuth: true } },
        { path: '/free_games', name: 'freeGames', component: FreeGames},
        { path: '/separate_news/:id', name: 'newsSinglePage', component: NewsSinglePage },
        { path: '/not_found', name: 'errorPage404', component: ErrorPage404 },
        { path: '/discountsGame', name: 'discountsGame', component: DiscountsGame },
        { path: '/earlyAccess', name: 'earlyAccessGame', component: EarlyAccessGame },
        { path: '/user_profile', name: 'userProfilePage', component: PersonPage, meta: { requiresAuth: true } },
        { path: '/forgot_pass', name: 'forgotPass', component: ForgotPass },
        { path: '/developer_profile', name: 'developerProfilePage', component: DeveloperPage, meta: { requiresAuth: true, requiredRole: 'dev' } },
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
        { path: '/Error403', name: 'ErrorPage403', component: ErrorPage403 },
        { path: '/UploadPage', name: 'uploadPage', component: UploadPage, meta: { requiresAuth: true, requiredRole: 'dev' }  },
        { path: '/profile', name: 'personPage', meta: { requiresAuth: true } }, // URL не относится к компоненту, нужен, чтобы перенаправлять на нужную страницу (ЛК разработчик или пользователь)
        { path: '/ChangePass', name: 'ChangePass', component: ChangePass },
        { path: '/Checkout', name: 'Checkout', component: Checkout },
        { path: '/GameDownloaded', name: 'GameDownloaded', component: GameDownloaded },
        { path: '/GoDownload', name: 'GoDownload', component: GoDownload },
        { path: '/MessageSent', name: 'MessageSent', component: MessageSent },
        { path: '/PasswordChanged', name: 'PasswordChanged', component: PasswordChanged },
        { path: '/PasswordReset', name: 'PasswordReset', component: PasswordReset },
        { path: '/Support', name: 'Support', component: Support }
    ]
})

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        // Проверка авторизации
        if (!router.app.$store.getters['user/isLoggedIn']) {
            next({
                path: '/sign_in',
                query: {redirect: to.fullPath}
            })
        }
    }
    // Перенаправление в нужный личный кабинет
    if (to.name == 'personPage') {
        console.log('profile route')
        if (router.app.$store.getters['user/isDeveloper']) {
            next({
                name: 'developerProfilePage'
            })
        } else {
            next({
                name: 'userProfilePage'
            })
        }
    }

    // Проверка роли для доступа к странице
    if (to.meta.requiredRole == 'dev' && !router.app.$store.getters['user/isDeveloper']) {
        alert('Доступ запрещен')
        next({
            name: 'homePage'
        })
    }

    next()

})
