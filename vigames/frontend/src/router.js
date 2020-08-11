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
import GenreGame from './pages/GenreGame/index.vue'
import LibraryPage from "./pages/LibraryPage/index.vue"
import GameSinglePage from "./pages/GameSinglePage/index.vue";
import LoginPage from "./pages/LoginPage/index.vue";
import NewsPage from "./pages/NewsGamePage/NewsPage.vue";
import HomePage from "./pages/HomeGamePage/HomePage.vue";
import SignInPage from "./pages/SignInPage/index.vue"
import SignUpRolePage from "./pages/SignUpRolePage/index.vue"
import ChangePass from './components/Pop-ups/ChangePass/index.vue'
import Checkout from './components/Pop-ups/Checkout/checkout.vue'
import GameDownloaded from './components/Pop-ups/GameDownloaded/index.vue'
import GoDownload from './components/Pop-ups/GoDownload/index.vue'
import MessageSent from './components/Pop-ups/MessageSent/index.vue'
import PasswordChanged from './components/Pop-ups/PasswordChanged/index.vue'
import PasswordReset from './components/Pop-ups/PasswordReset/index.vue'
import Support from './components/Pop-ups/Support/index.vue'
import MyGames from './components/Pop-ups/MyGames/index.vue'
import GameIsHide from './components/Pop-ups/GameIsHide/index.vue'
import GameHide from './components/Pop-ups/GameHide/index.vue'
import GameIsReturn from './components/Pop-ups/GameIsReturn/index.vue'
import GameReturned from './components/Pop-ups/GameReturned/index.vue'
import Statistics from './pages/Statistics/index.vue'
import EditPage from './pages/EditGamePage/index.vue'
import Vue from "vue";


Vue.use(Router);

export const router = new Router({
    // TODO: Добавить " meta: { requiresAuth: true } " к страницам, требующим авторизации
    // TODO: Добавить " meta: { requiredRole: 'dev' } " к страницам, доступным только для разработчиков (для пользователя аналогичное пока недоступно)
    routes: [
        { path: '/home', name: 'homePage', component: HomePage },
        { path: '/login', name: 'loginPage', component: LoginPage },
        { path: '/game/:id', name: 'singlePage', component: GameSinglePage },
        { path: '/genre/:genre', name: 'genrePage', component: GenreGame },
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
        { path: '/Error403', name: 'ErrorPage403', component: ErrorPage403 },
        { path: '/UploadPage', name: 'uploadPage', component: UploadPage, meta: { requiresAuth: true, requiredRole: 'dev' }  },
        { path: '/profile', name: 'personPage', meta: { requiresAuth: true } }, // URL не относится к компоненту, нужен, чтобы перенаправлять на нужную страницу (ЛК разработчик или пользователь)
        { path: '/change', name: 'change', component: UploadPage},
        { path: '/ChangePass', name: 'ChangePass', component: ChangePass },
        { path: '/Checkout', name: 'Checkout', component: Checkout },
        { path: '/GameDownloaded', name: 'GameDownloaded', component: GameDownloaded },
        { path: '/GoDownload', name: 'GoDownload', component: GoDownload },
        { path: '/MessageSent', name: 'MessageSent', component: MessageSent },
        { path: '/PasswordChanged', name: 'PasswordChanged', component: PasswordChanged },
        { path: '/PasswordReset', name: 'PasswordReset', component: PasswordReset },
        { path: '/Support', name: 'Support', component: Support },
        { path: '/MyGames', name: 'MyGames', component: MyGames },
        { path: '/GameIsHide', name: 'GameIsHide', component: GameIsHide },
        { path: '/GameHide', name: 'GameHide', component: GameHide },
        { path: '/GameIsReturn', name: 'GameIsReturn', component: GameIsReturn },
        { path: '/GameReturned', name: 'GameReturned', component: GameReturned },
        { path: '/Statistics', name: 'Statistics', component: Statistics },
        { path: '/edit', name: 'EditPage', component: EditPage }
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
