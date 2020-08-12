import PopularGamesComponents from "./PopularGamesComponents.vue"

export default {
name: 'PopularGames',
components: {
   PopularGamesComponents
},
props:{
	Array_Slide:{
		type:Array,
		default(){
			return[]
		}
	},


},
data(){
	return{
		currentsSlideIndex:0,
    Interval:4000

	}
},
methods:{
	leftFunc(){
		if(this.currentsSlideIndex<=0){
			this.currentsSlideIndex=4

		}else{
			this.currentsSlideIndex--

		}
	},
	rightFunc(){
		if(this.currentsSlideIndex >= 4){
			this.currentsSlideIndex=0

		}else{
			this.currentsSlideIndex++
      console.log(this.Interval)
		}
	}

	},
	mounted(){
		if(this.Interval>0){
			let vm = this;
			setInterval(function(){
        if(this.currentsSlideIndex++){
          vm.Interval = 0
        }else{
          vm.rightFunc()
        }

			},vm.Interval)
		}
}

}
