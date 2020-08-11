// eslint-disable-next-line no-unused-vars
import games from '../../../api/modules/games.js'
import GameCard  from "@/components/GameCard/GameCard.vue"

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
        this.loading = false
        this.recommendation = response.data
        console.log(response)
      }).catch(error => {
        console.log(error)
      })
    }
  }
  
}
