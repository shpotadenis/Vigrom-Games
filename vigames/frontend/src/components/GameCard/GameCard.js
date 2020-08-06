


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
<<<<<<< HEAD
=======
      console.log(this.SlideNumber)
>>>>>>> bbce1b56f6d0a86da1e390a9eab9bd7fc42908a5
		}
	},
  leftFunc(){
    if(this.SlideNumber<0){
      this.SlideNumber=3
    }else{
      this.SlideNumber--
<<<<<<< HEAD
=======
      console.log(this.SlideNumber)

>>>>>>> bbce1b56f6d0a86da1e390a9eab9bd7fc42908a5
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
