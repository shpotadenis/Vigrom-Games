

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

    methods: {
        HideGame() {
          this.isHide = !this.isHide
        }
    }


}
