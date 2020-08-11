import GameCard from "../../../components/GameCard/GameCard.vue";
export default {
  name: 'CategoriesGamePageComponent',
  components: {
    GameCard
  },
  methods:{
    hideShow(id){
      if (id==this.thisId && this.show){
        this.show = false;
      }
      else{
        this.show = true;
      }
      this.thisId = id
    }
  },
data(){
  return {
    show: false,
    thisId: 0,
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
