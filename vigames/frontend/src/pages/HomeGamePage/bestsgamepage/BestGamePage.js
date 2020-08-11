import BestsGamePageComponents from "./BestsGamePageComponents.vue"
import GameCard from "@/components/GameCard/GameCard.vue"
import games from '../../../api/modules/games.js'
import {convertApiToComponentObj} from "../../../utils";

export default {
  name: 'BestsGamePage',
  components: {
    BestsGamePageComponents,
    GameCard
  },
  data(){
    return{
      bests:[
      {
        image:"bests.svg",
        name:"the last of us 2",
        categoreis:"MMOPRG",
        undername:"Компьютерная игра в жанре action-adventure с элементами survival horror и стелс-экшена, разработанная студией Naughty Dog."
      }
      ],
      bestscomponents:[],
        loading: false
    }
  },
    beforeMount() {
      this.fetchData()
    },
    methods: {
      fetchData() {
          this.loading = true
          games.getBestsellers().then(response => {
              let gameCards = response.data // Карточки, полученные из API
              let gameComponentCards = [] // Сконвертированные карточки для компонента GameCard
              for (let i in gameCards) {
                  gameComponentCards.push(convertApiToComponentObj(gameCards[i]))
              }
              this.bestscomponents = gameComponentCards
              this.loading = false
          }).catch(error => {
              console.log(error)
          })
      }
    }
}
