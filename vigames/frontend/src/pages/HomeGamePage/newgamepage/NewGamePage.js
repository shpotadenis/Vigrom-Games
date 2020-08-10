
import GameCard from "@/components/GameCard/GameCard.vue"
import { convertApiToComponentObj } from '../../../utils.js'
import games from '../../../api/modules/games.js'

export default {
  name: 'NewGamePage',
  components: {
      GameCard
  },
  data(){
    return{
      loading: false,
      list:[
            {
            id:"1",
            image:"MaskGroup.svg",
            name:"DANGER CREW",
            undername:"Ubisoft Nadeo | Ubisoft",
            price:"299.99"
            },
            {
            id:"2",
            image:"MaskGroup.svg",
            name:"DANGER CREW",
            undername:"Ubisoft Nadeo | Ubisoft",
            price:"299.99"
            },
            {
            id:"3",
            image:"MaskGroup.svg",
            name:"DANGER CREW",
            undername:"Ubisoft Nadeo | Ubisoft",
            price:"299.99"
            },
            {
            id:"4",
            image:"MaskGroup.svg",
            name:"DANGER CREW",
            undername:"Ubisoft Nadeo | Ubisoft",
            price:"299.99"
            },
          ]
    }
  },
  beforeMount() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.loading = true
      games.getListOfGames().then(response => {

        let gameCards = response.data // Карточки, полученные из API
        let gameComponentCards = [] // Сконвертированные карточки для компонента GameCard
        for (let i in gameCards) {
          gameComponentCards.push(convertApiToComponentObj(gameCards[i]))
        }
        this.list = gameComponentCards

        this.loading = false
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
