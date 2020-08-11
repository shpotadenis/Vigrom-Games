import GameCard from "@/components/GameCard/GameCard.vue"
import games from '../../../api/modules/games.js'
import { convertApiToComponentObj } from '../../../utils.js'

export default {
  name: 'LittlePopularPage',
  components: {
    GameCard

  },
  data(){
    return{
      populars:[],
      loading: false
    }
  },

  beforeMount() {
    this.fetchData()
  },

  methods: {
    fetchData() {
      this.loading = true
      games.getPopular().then(response => {
        let gameCards = response.data // Карточки, полученные из API
        let gameComponentCards = [] // Сконвертированные карточки для компонента GameCard
        for (let i in gameCards) {
          gameComponentCards.push(convertApiToComponentObj(gameCards[i]))
        }
        this.populars = gameComponentCards
        this.loading = false
      }).catch(error => {
        console.log(error)
      })
    }
  }

}
