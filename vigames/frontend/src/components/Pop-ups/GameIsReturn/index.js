import GameReturned from "../../../components/Pop-ups/GameReturned/index.vue"
import games from '../../../api/modules/games.js'

export default {
    name: "gameIsReturn",
    components: {
        GameReturned
    },
    data() {
        return {
          isBtnClick: false
        }
    },
    methods: {
        gameReturn(){
            games.show(this.Gamereturn.id).then(response => {
                if (response) {
                    this.isBtnClick = true;
                    this.$emit('show-game')
                }
            }).catch(error => {
                console.log(error)
            })

        },
        closeOk() {
            this.isBtnClick = false
            this.$emit('close')
        }
    },
    props:{
      Gamereturn:{
        type:Object,
        default(){
          return{}
        }
      }
    }
}
