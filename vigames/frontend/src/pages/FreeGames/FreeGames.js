
import InternalMenu from '../../components/InternalMenu/InternalMenu.vue'
import SearchComponent from "../../components/SearchComponent/index.vue"

export default{

  name:"FreeGames",
  component:{
    InternalMenu,
    SearchComponent
  },
  data(){
    return{
      isVisible:false
    }
  }
}
