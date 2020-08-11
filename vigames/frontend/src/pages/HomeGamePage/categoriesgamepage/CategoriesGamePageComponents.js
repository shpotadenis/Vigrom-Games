import Action from "../../../components/Pop-ups/TopCategory/Action/index.vue"
import Simulators from "../../../components/Pop-ups/TopCategory/Simulators/index.vue"
import Strategies from "../../../components/Pop-ups/TopCategory/Strategies/index.vue"
import Casual from "../../../components/Pop-ups/TopCategory/Casual/index.vue"
import Adventures from "../../../components/Pop-ups/TopCategory/Adventures/index.vue"
import Imo from "../../../components/Pop-ups/TopCategory/IMO/index.vue"
import GameCard from "../../../components/GameCard/GameCard.vue";
export default {
  name: 'CategoriesGamePageComponent',
  components: {
    Action,
    Simulators,
    Strategies,
    Casual,
    Adventures,
    Imo,
    GameCard
  },
data(){
  return {
    isBtnClick_1: false,
    isBtnClick_2: false,
    isBtnClick_3: false,
    isBtnClick_4: false,
    isBtnClick_5: false,
    isBtnClick_6: false,
    show: false,
    topGames:[
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

    ]
  }
},
  props:{
    Categories_Game:{
      type:Object,
      default(){
        return{}
      }
    }
  },

}
