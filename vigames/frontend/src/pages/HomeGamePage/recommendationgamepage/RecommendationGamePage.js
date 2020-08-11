import games from '../../../api/modules/games.js'
import GameCard  from "@/components/GameCard/GameCard.vue"
import {convertApiToComponentObj} from "../../../utils";

export default {
  name: 'RecommendationGamePage',
  components: {
    GameCard
  },
  data(){
    return{
      recommendation:[],
      loading: false
    }
  },
  beforeMount() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.loading = true
      games.getRecommendation().then(response => {
        let gameCards = response.data // Карточки, полученные из API
        let gameComponentCards = [] // Сконвертированные карточки для компонента GameCard
        for (let i in gameCards) {
          gameComponentCards.push(convertApiToComponentObj(gameCards[i]))
        }
        this.recommendation = gameComponentCards
        this.loading = false
        console.log(response)
      }).catch(error => {
        console.log(error)
      })
    }
  }
  
}
