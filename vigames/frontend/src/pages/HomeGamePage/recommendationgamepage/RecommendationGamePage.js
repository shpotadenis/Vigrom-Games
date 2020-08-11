import games from '../../../api/modules/games.js'
import GameCard  from "@/components/GameCard/GameCard.vue"

export default {
  name: 'RecommendationGamePage',
  components: {
    GameCard
  },
  data(){
    return{
      recommendation:[]
    }
  },
  
}
