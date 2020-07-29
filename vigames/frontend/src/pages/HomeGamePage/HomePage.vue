<template>
  <div class="wrappen">
    <categories/>
    <popular-games
      :Array_Slide="items"
      :Interval="4000"
    />
    <little-popular/>
  </div>
</template>

<script>

import Categories from "./startcomponents/Categories"
import PopularGames from "./catalogscomponents/PopularGames"

export default {
  name: 'HomePage',
  components: {
    Categories,
    PopularGames
  },
  data(){
  return{
  items:[
      {
      name:"Bastion",
      discription:'Мультиплатформенная компьютерная игра в жанре action/RPG, разработанная польской студией CD Projekt RED',
      img:"bastion_7.jpg",
      id:"1"
      },
      {
      name:"UnderRail",
      discription:'Мультиплатформенная компьютерная игра в жанре action/RPG, разработанная польской студией CD Projekt RED',
      img:"underrail_3.jpg",
      id:"2"
      },
      {
      name:"Vessel",
      discription:'Мультиплатформенная компьютерная игра в жанре action/RPG, разработанная польской студией CD Projekt RED',
      img:"vessel-5.jpg",
      id:"3"
      },
      {
      name:"Runic Games",
      discription:'Мультиплатформенная компьютерная игра в жанре action/RPG, разработанная польской студией CD Projekt RED',
      img:"Pic1.jpg",
      id:"4"
      },
      {
      name:"Light Fall",
      discription:'Мультиплатформенная компьютерная игра в жанре action/RPG, разработанная польской студией CD Projekt RED',
      img:"c97a9.jpg",
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
