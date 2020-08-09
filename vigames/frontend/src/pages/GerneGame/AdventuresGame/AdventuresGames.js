
import InternalMenu from '../../../components/InternalMenu/InternalMenu.vue'
import SearchComponent from '../../../components/SearchComponent/index.vue'
import GameCard from  '../../../components/GameCard/GameCard.vue'
import BannerComponent from  '../../../components/BannerComponent/index.vue'
import FooterComponent from '../../../components/FooterComponent/index.vue'

export default{

  name:"AdventuresGames",
  components:{
    InternalMenu,
    SearchComponent,
    GameCard,
    BannerComponent,
    FooterComponent
  },
  data(){
    return{
      discountgames:[
        {
        id:"1",
        image:"MaskGroup.svg",
        name:"DANGER CREW",
        rating:"4.9",
        undername:"Ubisoft Nadeo | Ubisoft",
        price:"",
        scrin:'vessel-5.jpg',
        scrin1:'c97a9.jpg',
        scrin2:'Pic1.jpg',
        scrin3:'c97a9.jpg',
        icon:'cart-icon.png'
        },
        {
        id:"2",
        image:"MaskGroup.svg",
        name:"DANGER CREW",
        rating:"4.9",
        undername:"Ubisoft Nadeo | Ubisoft",
        price:"",
        scrin:'vessel-5.jpg',
        scrin1:'c97a9.jpg',
        scrin2:'Pic1.jpg',
        scrin3:'c97a9.jpg',
        icon:'cart-icon.png'
        },
        {
        id:"3",
        image:"MaskGroup.svg",
        name:"DANGER CREW",
        rating:"4.9",
        undername:"Ubisoft Nadeo | Ubisoft",
        price:"",
        scrin:'vessel-5.jpg',
        scrin1:'c97a9.jpg',
        scrin2:'Pic1.jpg',
        scrin3:'c97a9.jpg',
        icon:'cart-icon.png'
        },
        {
        id:"4",
        image:"MaskGroup.svg",
        name:"DANGER CREW",
        rating:"4.9",
        undername:"Ubisoft Nadeo | Ubisoft",
        price:"",
        scrin:'vessel-5.jpg',
        scrin1:'c97a9.jpg',
        scrin2:'Pic1.jpg',
        scrin3:'c97a9.jpg',
        icon:'cart-icon.png'
        },
        {
        id:"5",
        image:"MaskGroup.svg",
        name:"DANGER CREW",
        rating:"4.9",
        undername:"Ubisoft Nadeo | Ubisoft",
        price:"",
        scrin:'vessel-5.jpg',
        scrin1:'c97a9.jpg',
        scrin2:'Pic1.jpg',
        scrin3:'c97a9.jpg',
        icon:'cart-icon.png'
        },
        {
        id:"6",
        image:"MaskGroup.svg",
        name:"DANGER CREW",
        rating:"4.9",
        undername:"Ubisoft Nadeo | Ubisoft",
        price:"",
        scrin:'vessel-5.jpg',
        scrin1:'c97a9.jpg',
        scrin2:'Pic1.jpg',
        scrin3:'c97a9.jpg',
        icon:'cart-icon.png'
        },
        {
        id:"7",
        image:"MaskGroup.svg",
        name:"DANGER CREW",
        rating:"4.9",
        undername:"Ubisoft Nadeo | Ubisoft",
        price:"",
        scrin:'vessel-5.jpg',
        scrin1:'c97a9.jpg',
        scrin2:'Pic1.jpg',
        scrin3:'c97a9.jpg',
        icon:'cart-icon.png'
        },
        {
        id:"8",
        image:"MaskGroup.svg",
        name:"DANGER CREW",
        rating:"4.9",
        undername:"Ubisoft Nadeo | Ubisoft",
        price:"",
        scrin:'vessel-5.jpg',
        scrin1:'c97a9.jpg',
        scrin2:'Pic1.jpg',
        scrin3:'c97a9.jpg',
        icon:'cart-icon.png'
        },
        {
        id:"9",
        image:"MaskGroup.svg",
        name:"DANGER CREW",
        rating:"4.9",
        undername:"Ubisoft Nadeo | Ubisoft",
        price:"",
        scrin:'vessel-5.jpg',
        scrin1:'c97a9.jpg',
        scrin2:'Pic1.jpg',
        scrin3:'c97a9.jpg',
        icon:'cart-icon.png'
        },
        {
        id:"10",
        image:"MaskGroup.svg",
        name:"DANGER CREW",
        rating:"4.9",
        undername:"Ubisoft Nadeo | Ubisoft",
        price:"",
        scrin:'vessel-5.jpg',
        scrin1:'c97a9.jpg',
        scrin2:'Pic1.jpg',
        scrin3:'c97a9.jpg',
        icon:'cart-icon.png'
        },
        {
        id:"11",
        image:"MaskGroup.svg",
        name:"DANGER CREW",
        rating:"4.9",
        undername:"Ubisoft Nadeo | Ubisoft",
        price:"",
        scrin:'vessel-5.jpg',
        scrin1:'c97a9.jpg',
        scrin2:'Pic1.jpg',
        scrin3:'c97a9.jpg',
        icon:'cart-icon.png'
        },
        {
        id:"12",
        image:"MaskGroup.svg",
        name:"DANGER CREW",
        rating:"4.9",
        undername:"Ubisoft Nadeo | Ubisoft",
        price:"",
        scrin:'vessel-5.jpg',
        scrin1:'c97a9.jpg',
        scrin2:'Pic1.jpg',
        scrin3:'c97a9.jpg',
        icon:'cart-icon.png'
        },

      ],
      array:[],
      array2:[]
    }
},
      mounted(){
        for(let i = 0; i<this.discountgames.length; i++){
          if(i<8){
            this.array.push(this.discountgames[i])
          }else{
            this.array2.push(this.discountgames[i])
          }
        }
      }
}
