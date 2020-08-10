<template>
<div class="container topComponent">
  <div class="PopularGameTitle row">
    <p class="Title col">Топ 8 игр</p>
  </div>
  <div class="row justify-content-center">

  <div class="AllCategories">
    <a @click="show!=show" class="col-2">
    <div class="CategoriesGamePageComponent">
      <img src="@/assets/img/flash-icon.svg" class="ImageCategories">
      <p class="TitleCategories">Экшен</p>
    </div>
    </a>
    <a @click="show!=show" class="col-2">
    <div class="CategoriesGamePageComponent">
      <img src="@/assets/img/cube-icon.svg" class="ImageCategories">
      <p class="TitleCategories">Симуляторы</p>
    </div>
    </a>
    <a @click="show!=show" class="col-2">
    <div class="CategoriesGamePageComponent">
      <img src="@/assets/img/map-icon.svg" class="ImageCategories">
      <p class="TitleCategories">Стратегии</p>
    </div>
    </a>
    <a @click="show!=show" class="col-2">
    <div class="CategoriesGamePageComponent">
      <img src="@/assets/img/smiling-face-outline.svg" class="ImageCategories">
      <p class="TitleCategories">Казуальные</p>
    </div>
    </a>
    <a @click="show!=show" class="col-2">
    <div class="CategoriesGamePageComponent">
      <img src="@/assets/img/globe-icon.svg" class="ImageCategories">
      <p class="TitleCategories">Приключения</p>
    </div>
    </a>
    <a @click="show!=show" class="col-2">
    <div class="CategoriesGamePageComponent">
      <img src="@/assets/img/shield-icon.svg" class="ImageCategories">
      <p class="TitleCategories">ММО</p>
    </div>
    </a>

  </div>
  </div>
  <div class="row justify-content-center cards" v-show="show">
    <game-card class="ItemCard col-3"
               v-for="game in topGames"
               :key="game.id"
               :Game="game"/>
  </div>
</div>
</template>

<script src="./CategoriesGamePageComponents.js">

</script>


<style lang="scss">
@import '@/assets/style/CategoriesGamePageComponents.scss'
</style>
