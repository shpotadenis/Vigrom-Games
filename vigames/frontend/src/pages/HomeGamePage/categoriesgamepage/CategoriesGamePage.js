
import CategoriesGamePageComponents from "./CategoriesGamePageComponents.vue"

export default {
  name: 'CategoriesGamePage',
  components: {
    CategoriesGamePageComponents
  },
  data(){
    return{
      categories:[
      {
        name:"Экшен",
        image:"flash-icon.svg"
      },
      {
        name:"Симуляторы",
        image:"cube-icon.svg"
      },
      {
        name:"Стратегии",
        image:"map-icon.svg"
      },
      {
        name:"Инди",
        image:"smiling-face-outline.svg"
      },
      {
        name:"Приключения",
        image:"globe-icon.svg"
      },
      {
        name:"ММО",
        image:"shield-icon.svg"
      }
      ]
    }
  }
}
