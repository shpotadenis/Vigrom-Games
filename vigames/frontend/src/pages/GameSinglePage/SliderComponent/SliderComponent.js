import SliderElement from "./SliderElement.vue"

export default {
	name: 'SliderComponent',
	components: {
		SliderElement
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

			}else{
				this.currentsSlideIndex--

			}
		},
		rightFunc(){
			if(this.currentsSlideIndex >= 4){
				this.currentsSlideIndex=0

			}else{
				this.currentsSlideIndex++

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
