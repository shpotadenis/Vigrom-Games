


export default {
name: 'GameCard',
components: {

},
data(){
  return{
    SlideNumber:0,
    isShow:false
}
},
methods:{
	rightFunc(){
		if(this.SlideNumber >= 3){
			this.SlideNumber=0
		}else{
			this.SlideNumber++

      console.log(this.SlideNumber)

		}
	},
  leftFunc(){
    if(this.SlideNumber<0){
      this.SlideNumber=3
    }else{
      this.SlideNumber--

      console.log(this.SlideNumber)


    }
  },
  showScrin(){
    this.isShow=true;
  },
  closeScrin(){
    this.isShow=false;
  }
  },
props:{
  Game:{
  type:Object,
  default(){
    return{}
  }
},

}
}
