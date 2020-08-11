import Action from "../../../components/Pop-ups/TopCategory/Action/index.vue"
import Simulators from "../../../components/Pop-ups/TopCategory/Simulators/index.vue"
import Strategies from "../../../components/Pop-ups/TopCategory/Strategies/index.vue"
import Casual from "../../../components/Pop-ups/TopCategory/Casual/index.vue"
import Adventures from "../../../components/Pop-ups/TopCategory/Adventures/index.vue"
import Imo from "../../../components/Pop-ups/TopCategory/IMO/index.vue"
import GameCard from "../../../components/GameCard/GameCard.vue";
import games from '../../../api/modules/games.js'
import { convertApiToComponentObj } from '../../../utils.js'

export default {
  name: 'CategoriesGamePageComponent',
  components: {
    Action,
    Simulators,
    Strategies,
    Casual,
    Adventures,
    Imo,
    GameCard
  },
  methods:{
    hideShow(genre){
      if (genre==this.genre && this.show){
        this.show = false;
      }
      else{
        this.show = true;
        this.fetchData(genre)
      }
      this.genre = genre
    },
    fetchData(genre) {
      games.getTopInGenre(genre).then(response => {
        if (response.data) {
          for (let i in response.data) {
            response.data[i] = convertApiToComponentObj(response.data[i])
          }
          this.topGames = response.data
        }
      }).catch(error => {
        console.log(error)
      })
    }
  },
data(){
  return {
    show: false,
    genre: '',
    topGames:[]
  }
},
  props:{
    Categories_Game:{
      type:Object,
      default(){
        return{}
      }
    }
  },

}
