export default {
name: 'GameCardSale',
components: {

},
data(){
  return{
    SlideNumber:0,
    isShow:false
}
},
props:{
  Game:{
  type:Object,
  default(){
    return{}
  }
}

}
}
