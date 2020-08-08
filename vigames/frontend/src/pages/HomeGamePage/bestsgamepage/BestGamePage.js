import BestsGamePageComponents from "./BestsGamePageComponents.vue"
import GameCard from "@/components/GameCard/GameCard.vue"

export default {
  name: 'BestsGamePage',
  components: {
    BestsGamePageComponents,
    GameCard
  },
  data(){
    return{
      bests:[
      {
        image:"bests.svg",
        name:"the last of us 2",
        categoreis:"MMOPRG",
        undername:"Компьютерная игра в жанре action-adventure с элементами survival horror и стелс-экшена, разработанная студией Naughty Dog."
      }
      ],
      bestscomponents:[
        {
        id:"1",
        image:"MaskGroup.svg",
        name:"DANGER CREW",
        rating:"4.9",
        undername:"Ubisoft Nadeo | Ubisoft",
        price:"299.99",
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
        price:"299.99",

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
        price:"299.99",

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
        price:"299.99",

        scrin:'vessel-5.jpg',
        scrin1:'c97a9.jpg',
        scrin2:'Pic1.jpg',
        scrin3:'c97a9.jpg',
        icon:'cart-icon.png'
        },
      ]
    }
  }
}
