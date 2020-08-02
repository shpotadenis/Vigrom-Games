import BestsGamePageComponents from "./BestsGamePageComponents.vue"
import LittlePopularPageComponents from "../popularcomponents/LittlePopularPageComponents.vue"

export default {
  name: 'BestsGamePage',
  components: {
    BestsGamePageComponents,
    LittlePopularPageComponents
  },
  data(){
    return{
      bests:[
      {
        image:"bests.svg",
        name:"the last of ass 2",
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
        price:"299.99"
        },
        {
        id:"2",
        image:"MaskGroup.svg",
        name:"DANGER CREW",
        rating:"4.9",
        undername:"Ubisoft Nadeo | Ubisoft",
        price:"299.99"
        },
        {
        id:"3",
        image:"MaskGroup.svg",
        name:"DANGER CREW",
        rating:"4.9",
        undername:"Ubisoft Nadeo | Ubisoft",
        price:"299.99"
        },
        {
        id:"4",
        image:"MaskGroup.svg",
        name:"DANGER CREW",
        rating:"4.9",
        undername:"Ubisoft Nadeo | Ubisoft",
        price:"299.99"
        },
      ]
    }
  }
}
