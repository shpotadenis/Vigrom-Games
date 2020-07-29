<template>
  <div class="wrapper">
  <div class="Slider" :style="{'margin-left': '-' + (100 * currentsSlideIndex) + '%' }">
    <popular-games-components
    v-for="item in Array_Slide"
    :key="item.id"
	:Game_Popular="item"
    />
    <img src="@/assets/img/arrow3.png" class="strelka1" @click="leftFunc">
    <img src="@/assets/img/arrow3.png" class="strelka2" @click="rightFunc">
  </div>

  </div>
</template>

<script>

import PopularGamesComponents from "./PopularGamesComponents"

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
</script>

<style>
.wrapper{
	max-width:1000px;
	overflow:hidden;
	margin:0 auto;
}
.Slider{
	display:flex;
	transition: all ease 1s;
}
.strelka1{
	position:absolute;
	transform:rotate(180deg);
	left:15%;
	top:35%;
}
.strelka2{
	position:absolute;
	top:35%;
	left:80%;
}
</style>
