import GameReturned from "../../../components/Pop-ups/GameReturned/index.vue"

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
        this.isBtnClick = true;
      }
    }
}
