<template>
  <div class="BestsGamePageComponents">
    <img v-bind:src="require('@/assets/img/' + Bests_Game.image)" width="700" height="320" class="ImageGameBests">
    <div class="InfoBestsGame">
        <p class="CategoriesBestsGame">{{Bests_Game.categoreis}}</p>
        <p class="NameBestsGame">{{Bests_Game.name}}</p>
        <p class="UnderNameBestsGame">{{Bests_Game.undername}}</p>
        <button class="ButtonBestsGame">Подробнее <img class="ImageBests" src="@/assets/img/Vector.png"></button>
    </div>
  </div>
</template>

<script>



export default {
  name: 'BestsGamePageComponents',
  components: {
  },
  props:{
    Bests_Game:{
      type:Object,
      default(){
        return{}
      }
    }
  }
}
</script>
<style>
.BestsGamePageComponents{

height:295px;
display:flex;
border-radius:10px;
  margin-top:17px;
  background-color:#2D2D42;

}
.InfoBestsGame{
  margin-top:30px;
  margin-left:30px;
}
.ImageGameBests{
position:relative;
top:-12px;
}
.CategoriesBestsGame{
font-style: normal;
font-weight: normal;
font-size: 14px;
line-height: 19px;
color: #7A7A83;
}
.NameBestsGame{
margin-top:35px;
font-style: normal;
font-weight: 800;
font-size: 24px;
text-transform:uppercase;
line-height: 33px;
color: #FFFFFF;
}
.UnderNameBestsGame{
width:230px;
margin-right:30px;
font-style: normal;
font-weight: normal;
font-size: 14px;
line-height: 19px;

color: #7A7A83;

}
.ButtonBestsGame{
margin-top:20px;
width: 139px;
height: 38px;
color:#fff;
border:none;
text-indent:-10px;
background: #CE6796;
border-radius: 8px;

}
.ImageBests{
margin-left:20px;
}
</style>
