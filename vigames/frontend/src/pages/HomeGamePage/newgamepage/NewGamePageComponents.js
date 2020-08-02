import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/swiper-bundle.css'


export default {
name: 'NewGamePageComponent',
components: {
Swiper,
SwiperSlide
},
data(){
  return{
    SlideNumber:0
}
},
methods:{
	rightFunc(){
		if(this.SlideNumber >= 3){
			this.SlideNumber=0
			console.log(this.SlideNumber)
		}else{
			this.SlideNumber++
			console.log(this.SlideNumber)
		}
	},
  leftFunc(){
    if(this.SlideNumber<=0){
      this.SlideNumber=3
      console.log(this.SlideNumber)
    }else{
      this.SlideNumber--
      console.log(this.SlideNumber)
    }
  },

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
