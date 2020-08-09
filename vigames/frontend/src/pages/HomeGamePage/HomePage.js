import Categories from "./startcomponents/Categories.vue"
import PopularGames from "./catalogscomponents/PopularGames.vue"
import LittlePopular from "./popularcomponents/LittlePopularPage.vue"
import NewGamePage from "./newgamepage/NewGamePage.vue"
import BestsGamePage from "./bestsgamepage/BestsGamePage.vue"
import CategoriesGamePage from "./categoriesgamepage/CategoriesGamePage.vue"
import RecommendationGamePage from "./recommendationgamepage/RecommendationGamePage.vue"
import FooterComponents from "../../components/FooterComponent/index.vue"

export default {
  name: 'HomePage',
  components: {
    Categories,
    PopularGames,
    LittlePopular,
    NewGamePage,
    BestsGamePage,
    CategoriesGamePage,
    RecommendationGamePage,
    FooterComponents
  },
  data(){
  return{
  items:[
      {
      name:"Bastion",
      discription:'Мультиплатформенная компьютерная игра в жанре action/RPG, разработанная польской студией CD Projekt RED',
      image:"bastion_7.jpg",
      id:"1"
      },
      {
      name:"UnderRail",
      discription:'Мультиплатформенная компьютерная игра в жанре action/RPG, разработанная польской студией CD Projekt RED',
      image:"underrail_3.jpg",
      id:"2"
      },
      {
      name:"Vessel",
      discription:'Мультиплатформенная компьютерная игра в жанре action/RPG, разработанная польской студией CD Projekt RED',
      image:"vessel-5.jpg",
      id:"3"
      },
      {
      name:"Runic Games",
      discription:'Мультиплатформенная компьютерная игра в жанре action/RPG, разработанная польской студией CD Projekt RED',
      image:"Pic1.jpg",
      id:"4"
      },
      {
      name:"Light Fall",
      discription:'Мультиплатформенная компьютерная игра в жанре action/RPG, разработанная польской студией CD Projekt RED',
      image:"c97a9.jpg",
      id:"5"
      },

    ],

}
},
}
