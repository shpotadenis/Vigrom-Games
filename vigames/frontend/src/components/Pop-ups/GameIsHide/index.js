import GameHide from "../../../components/Pop-ups/GameHide/index.vue"

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
            this.isBtnClick = true;
            this.$emit('hide-game')
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
