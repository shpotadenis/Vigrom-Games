

export default {
    name: 'InternalMenu',
    component:{

    },
    data(){
      return{
        isCategories:false
      }
    },
    methods:{
      showCategories(){
        this.isCategories = !this.isCategories
      }
    }


}
