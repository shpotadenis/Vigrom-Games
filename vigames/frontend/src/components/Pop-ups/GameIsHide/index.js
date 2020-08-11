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
