<template>

  <div class="BestsGamePage">
    <div class="BestsGameTitle">
      <p class="Title">Бестселлеры</p>
    </div>
    <bests-game-page-components
      v-for="game in bests"
      :key="game.image"
      :Bests_Game="game"
    />
    <div class="BestsGameComponents">
      <little-popular-page-components
        v-for="gamebests in bestscomponents"
        :key="gamebests.id"
        :Game="gamebests"
      />
    </div>

</div>
</template>

<script>

import BestsGamePageComponents from "./BestsGamePageComponents"
import LittlePopularPageComponents from "../popularcomponents/LittlePopularPageComponents"

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
</script>
<style>
.BestsGamePage{
margin-top:100px;
}
.BestsGameComponents{
display:flex;
justify-content:space-between;
margin-top:60px;
}
</style>
