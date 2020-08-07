import Action from "../../../components/Pop-ups/TopCategory/Action/index.vue"
import Simulators from "../../../components/Pop-ups/TopCategory/Simulators/index.vue"
import Strategies from "../../../components/Pop-ups/TopCategory/Strategies/index.vue"
import Casual from "../../../components/Pop-ups/TopCategory/Casual/index.vue"
import Adventures from "../../../components/Pop-ups/TopCategory/Adventures/index.vue"
import Imo from "../../../components/Pop-ups/TopCategory/IMO/index.vue"
export default {
  name: 'CategoriesGamePageComponent',
  components: {
    Action,
    Simulators,
    Strategies,
    Casual,
    Adventures,
    Imo
  },
data(){
  return {
    isBtnClick_1: false,
    isBtnClick_2: false,
    isBtnClick_3: false,
    isBtnClick_4: false,
    isBtnClick_5: false,
    isBtnClick_6: false
  }
},
  props:{
    Categories_Game:{
      type:Object,
      default(){
        return{}
      }
    }
  },

}
