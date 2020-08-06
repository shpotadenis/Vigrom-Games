import FooterComponent from '../../components/FooterComponent/index.vue'
import SearchComponent from '../../components/SearchComponent/index.vue'
import BannerComponent from '../../components/BannerComponent/index.vue'
import ContentCardComponent from '../../components/ContentCardComponent/index.vue'
import GameCard from "@/components/GameCard/GameCard.vue"
import { convertApiToComponentObj } from '../../utils.js'

export default {
    name: 'FeaturedPage',
    components: {
        FooterComponent,
        SearchComponent,
        BannerComponent,
        ContentCardComponent,
        GameCard
    },
    data() {
        return {
            loading: true
        }
    },
    mounted() {
        this.fetchData()
    },
    computed: {
      getFeaturedCards() {
          let wlCards = this.$store.getters['user/getWishlist'] // Карточки, полученные из API
          let wlComponentCards = [] // Сконвертированные карточки для компонента GameCard
          for (let i in wlCards) {
              wlComponentCards.push(convertApiToComponentObj(wlCards[i]))
          }
          return wlComponentCards
      }
    },
    methods: {
        fetchData() {
            this.$store.dispatch('user/getWishlist').then(response => {
                this.loading = false;
                console.log('Wishlist added:')
                console.log(response)
            }).catch(error => {
                console.log('Library error')
                console.log(error.response)
            })
        },
    }

}
