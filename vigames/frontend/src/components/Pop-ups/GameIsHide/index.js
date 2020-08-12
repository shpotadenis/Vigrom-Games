import GameHide from "../../../components/Pop-ups/GameHide/index.vue"
import games from '../../../api/modules/games.js'

export default {
    name: "gameIsHide",
    components: {
        GameHide,
    },
    data() {
        return {
          isBtnClick: false
        }
    },
    methods: {
        hideGame(){
            games.hide(this.Gamehide.id).then(response => {
                if (response) {
                    this.isBtnClick = true;
                    this.$emit('hide-game')
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
      Gamehide:{
        type:Object,
        default(){
          return{}
        }
      }
    }
}
