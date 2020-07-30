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

export default {
  name: 'HomePage',
  components: {
    Categories,
    PopularGames,
    LittlePopular,
    NewGamePage,
    BestsGamePage
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
  width:1000px;
  margin:auto;
}
</style>
