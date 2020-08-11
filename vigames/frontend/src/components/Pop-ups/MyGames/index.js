import GameInfoCard from "../../../components/GameInfoCard/index.vue"
import user from '../../../api/modules/user.js'

export default {
    name: "action",

    components:{
      GameInfoCard
    },
    data() {
      return {
        loading: false,
        GameInfoCard:[]
      }
    },

    beforeMount() {
      this.fetchData()
    },

    methods: {
      fetchData() {
        this.loading = true
        user.getDeveloperGames().then(response => {
          this.GameInfoCard = response.data
          console.log(response)
          this.loading = false
        }).catch(error => {
          console.log(error)
        })
      }
    }
}
