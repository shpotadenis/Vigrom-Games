import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/swiper-bundle.css'


export default {
name: 'LittlePopularPageComponents',
components: {
Swiper,
SwiperSlide
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

		}
	},
  leftFunc(){
    if(this.SlideNumber<=0){
      this.SlideNumber=3

    }else{
      this.SlideNumber--

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
