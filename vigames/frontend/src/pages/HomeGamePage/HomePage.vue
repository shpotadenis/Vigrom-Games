<template>
<div class="container">
  <div class="col">
    <div class="wrappen">
      <categories/>
      <popular-games
        :Array_Slide="items"
        :Interval="4000"
      />
      <little-popular/>
      <new-game-page/>
      <bests-game-page/>
      <categories-game-page/>
      <recommendation-game-page/>
      <div class="Banner"></div>
      <div class="foot">
        <footer-components/>
      </div>
    </div>
  </div>
</div>
</template>

<script>

import Categories from "./startcomponents/Categories"
import PopularGames from "./catalogscomponents/PopularGames"
import LittlePopular from "./popularcomponents/LittlePopularPage.vue"
import NewGamePage from "./newgamepage/NewGamePage"
import BestsGamePage from "./bestsgamepage/BestsGamePage"
import CategoriesGamePage from "./categoriesgamepage/CategoriesGamePage"
import RecommendationGamePage from "./recommendationgamepage/RecommendationGamePage"
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

    ]
  }
}
}
</script>
<style>
.wrappen{
  width:1110px;
  margin:0 auto;
}
.Banner{
width:1110px;
height:434px;
margin-top:93px;
background: #2D2D42;
border-radius: 10px;
}
.foot{
width:1110px;
margin-top:100px;
}
</style>
