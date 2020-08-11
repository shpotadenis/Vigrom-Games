<template>
  <div class="BestsGamePageComponents">
    <img v-bind:src="Bests_Game.img" width="700" height="320" class="ImageGameBests">
    <div class="InfoBestsGame">
        <p class="CategoriesBestsGame">{{Bests_Game.genre}}</p>
        <p class="NameBestsGame">{{Bests_Game.title}}</p>
        <p class="UnderNameBestsGame">{{Bests_Game.undername}}</p>
        <button class="ButtonBestsGame">Подробнее <img class="ImageBests" src="@/assets/img/Vector.png"></button>
    </div>
  </div>
</template>

<script src="./BestGamePageComponent.js">

</script>
<style lang="scss">
@import '@/assets/style/BestsGamePageComponents.scss'
</style>
