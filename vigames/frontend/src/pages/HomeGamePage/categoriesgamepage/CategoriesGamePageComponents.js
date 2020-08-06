import TopCategory from "../../../components/Pop-ups/TopCategory/index.vue"

export default {
  name: 'CategoriesGamePageComponent',
  components: {
    TopCategory
  },
data(){
  return {
    TopCategory:{
      genre: 'Test complite'
    },
    isBtnClick: false
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
