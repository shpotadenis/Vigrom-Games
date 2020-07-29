import Vue from 'vue'
import App from './App.vue'
import Router from 'vue-router'
import store from './store/store.js'
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap-grid.min.css';
import GameSinglePage from "./pages/GameSinglePage/index.vue";
import LoginPage from "./pages/LoginPage/index.vue";

Vue.use(Router);

Vue.config.productionTip = false

const router = new Router({
  routes: [
    { path: '/login', name: 'loginPage', component: LoginPage },
    { path: '/shop', name: 'singlePage', component: GameSinglePage }
  ]
})

new Vue({
  render: h => h(App),
  router,
  store
}).$mount('#app')
