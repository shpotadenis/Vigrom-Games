import Vue from 'vue'
import App from './App.vue'
import Router from 'vue-router'
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap-grid.min.css';
import GameSinglePage from "./pages/GameSinglePage/index.vue";
import LoginPage from "./pages/LoginPage/index.vue";
import NewsPage from "./pages/NewsGamePage/NewsPage";
import HomePage from "./pages/HomeGamePage/HomePage";

Vue.use(Router);

Vue.config.productionTip = false

const router = new Router({
  routes: [
    { path: '/login', name: 'loginPage', component: LoginPage },
    { path: '/shop', name: 'singlePage', component: GameSinglePage },
    { path: '/home', name: 'homePage', component: HomePage },
    { path: '/news', name: 'newsPage', component: NewsPage }
  ]
})

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
