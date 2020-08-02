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
	Interval:{
		type: Number,
		default: 0
	}

},
data(){
	return{
		currentsSlideIndex:0

	}
},
methods:{
	leftFunc(){
		if(this.currentsSlideIndex<=0){
			this.currentsSlideIndex=4
			console.log(this.currentsSlideIndex)
		}else{
			this.currentsSlideIndex--
			console.log(this.currentsSlideIndex)
		}
	},
	rightFunc(){
		if(this.currentsSlideIndex >= 4){
			this.currentsSlideIndex=0
			console.log(this.currentsSlideIndex)
		}else{
			this.currentsSlideIndex++
			console.log(this.currentsSlideIndex)
		}
	}

	},
	mounted(){
		if(this.Interval>0){
			let vm = this;
			setInterval(function(){
				vm.rightFunc()
			},vm.Interval)
		}
}

}
