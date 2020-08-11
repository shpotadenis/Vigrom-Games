import GameCard from "../../../components/GameCard/GameCard.vue";
import games from '../../../api/modules/games.js'
import { convertApiToComponentObj } from '../../../utils.js'

export default {
  name: 'CategoriesGamePageComponent',
  components: {
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
