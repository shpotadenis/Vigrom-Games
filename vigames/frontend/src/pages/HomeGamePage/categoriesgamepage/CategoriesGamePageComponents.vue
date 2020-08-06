<template>
<div>
  <top-category v-if="isBtnClick" @close="isBtnClick = false"/>
  <div class="AllCategories">
    <a @click="isBtnClick = true">
    <div class="CategoriesGamePageComponent">
      <img src="@/assets/img/flash-icon.svg" class="ImageCategories">
      <p class="TitleCategories">Экшен</p>
    </div>
    </a>
    <a @click="isBtnClick = true">
    <div class="CategoriesGamePageComponent">
      <img src="@/assets/img/cube-icon.svg" class="ImageCategories">
      <p class="TitleCategories">Симуляторы</p>
    </div>
    </a>
    <a @click="isBtnClick = true">
    <div class="CategoriesGamePageComponent">
      <img src="@/assets/img/map-icon.svg" class="ImageCategories">
      <p class="TitleCategories">Стратегии</p>
    </div>
    </a>
    <a @click="isBtnClick = true">
    <div class="CategoriesGamePageComponent">
      <img src="@/assets/img/smiling-face-outline.svg" class="ImageCategories">
      <p class="TitleCategories">Казуальные</p>
    </div>
    </a>
    <a @click="isBtnClick = true">
    <div class="CategoriesGamePageComponent">
      <img src="@/assets/img/globe-icon.svg" class="ImageCategories">
      <p class="TitleCategories">Приключения</p>
    </div>
    </a>
    <a @click="isBtnClick = true">
    <div class="CategoriesGamePageComponent">
      <img src="@/assets/img/shield-icon.svg" class="ImageCategories">
      <p class="TitleCategories">ММО</p>
    </div>
    </a>
  </div>
</div>
</template>

<script src="./CategoriesGamePageComponents.js">

</script>


<style lang="scss">
@import '@/assets/style/CategoriesGamePageComponents.scss'
</style>
