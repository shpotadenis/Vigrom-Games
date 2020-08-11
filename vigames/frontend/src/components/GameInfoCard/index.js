import { getImageUrl } from '../../utils.js'

export default {
    name: "GameInfoCard",
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
          isHide: false
        }
    },
    computed: {
        getImage() {
            return getImageUrl(this.Game_Info_Card.img)
        }
    },

    methods: {
        HideGame() {
          this.isHide = !this.isHide

        }
    }


}
