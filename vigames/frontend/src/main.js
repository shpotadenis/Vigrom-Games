import Vue from 'vue'
import App from './App.vue'
import store from './store/store.js'
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap-grid.min.css';
import VueAwesomeSwiper from 'vue-awesome-swiper'
import 'swiper/swiper-bundle.css'
import { router } from './router.js'
import VueScrollTo from 'vue-scrollto'
import vueDebounce from 'vue-debounce'


Vue.use(vueDebounce)

Vue.use(vueDebounce, {
  listenTo: 'input',
  defaultTime: '700ms'
})

Vue.use(VueScrollTo)
Vue.use(VueAwesomeSwiper);

Vue.config.productionTip = false

export default new Vue({
  render: h => h(App),
  router,
  store
}).$mount('#app')
