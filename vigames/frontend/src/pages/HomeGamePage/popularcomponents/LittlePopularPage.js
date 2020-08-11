import GameCard from "@/components/GameCard/GameCard.vue"
import games from '../../../api/modules/games.js'

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
        this.populars = response.data
        this.loading = false
      }).catch(error => {
        console.log(error)
      })
    }
  }

}
