import TopCategory from "../../../components/Pop-ups/TopCategory/index.vue"

export default {
  name: 'CategoriesGamePageComponent',
  components: {
    TopCategory
  },
data(){
  return {
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
  }

}
