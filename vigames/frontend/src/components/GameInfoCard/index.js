

export default {
    name: "GameInfoCard",
    props:{
      GameInfo:{
      type:Object,
      default(){
        return{}
      }
    },
    computed: {
        getGameData() {
            return gamedata;
        }
    }

}
