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

<script src="./BestGamePageComponent.js">

</script>
<style lang="scss">
@import '@/assets/style/BestsGamePageComponents.scss'
</style>
