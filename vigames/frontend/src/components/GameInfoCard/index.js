import { getImageUrl } from '../../utils.js'
import GameIsHide from"../Pop-ups/GameIsHide/index.vue"
import GameIsReturn from"../Pop-ups/GameIsReturn/index.vue"

export default {
    name: "GameInfoCard",
    components: {
        GameIsHide,
        GameIsReturn
    },
    props:{
      Game_Info_Card:{
      type:Object,
      default(){
        return{
        }
      }
    }
  },
    data(){
        return {
          isHide: false,
          Hide: false,
          Return: false,
          item:Object
        }
    },
    computed: {
        getImage() {
            return getImageUrl(this.Game_Info_Card.img)
        }
    },

    methods: {
        HideGame() {
          this.Hide = true;
        },
        ReturnGame() {
          this.Return = true;
        },

        hide() {
            this.Game_Info_Card.is_hidden = true
        },

        show() {
            this.Game_Info_Card.is_hidden = false
        }
    },
    mounted(){

    }


}
