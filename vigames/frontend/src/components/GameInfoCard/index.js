import GameIsHide from"../Pop-ups/GameIsHide/index.vue"
import GameIsReturn from"../Pop-ups/GameIsReturn/index.vue"
import EditingSuccessful from"../Pop-ups/EditingSuccessful/index.vue"

export default {
    name: "GameInfoCard",
    components: {
        GameIsHide,
        GameIsReturn,
        EditingSuccessful
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
          isEdit: false
        }
    },

    methods: {
        HideGame() {
          this.isHide = !this.isHide;
          this.Hide = true;
        },
        ReturnGame() {
          this.isHide = !this.isHide;
          this.Return = true;
        },
        Edit(){
          this.isEdit = true;
        }
    }


}
