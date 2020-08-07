<template>
<div>
  <action v-if="isBtnClick_1" @close="isBtnClick_1 = false"/>
  <simulators v-if="isBtnClick_2" @close="isBtnClick_2 = false"/>
  <strategies v-if="isBtnClick_3" @close="isBtnClick_3 = false"/>
  <casual v-if="isBtnClick_4" @close="isBtnClick_4 = false"/>
  <adventures v-if="isBtnClick_5" @close="isBtnClick_5 = false"/>
  <imo v-if="isBtnClick_6" @close="isBtnClick_6 = false"/>
  <div class="AllCategories">
    <a @click="isBtnClick_1 = true">
    <div class="CategoriesGamePageComponent">
      <img src="@/assets/img/flash-icon.svg" class="ImageCategories">
      <p class="TitleCategories">Экшен</p>
    </div>
    </a>
    <a @click="isBtnClick_2 = true">
    <div class="CategoriesGamePageComponent">
      <img src="@/assets/img/cube-icon.svg" class="ImageCategories">
      <p class="TitleCategories">Симуляторы</p>
    </div>
    </a>
    <a @click="isBtnClick_3 = true">
    <div class="CategoriesGamePageComponent">
      <img src="@/assets/img/map-icon.svg" class="ImageCategories">
      <p class="TitleCategories">Стратегии</p>
    </div>
    </a>
    <a @click="isBtnClick_4 = true">
    <div class="CategoriesGamePageComponent">
      <img src="@/assets/img/smiling-face-outline.svg" class="ImageCategories">
      <p class="TitleCategories">Казуальные</p>
    </div>
    </a>
    <a @click="isBtnClick_5 = true">
    <div class="CategoriesGamePageComponent">
      <img src="@/assets/img/globe-icon.svg" class="ImageCategories">
      <p class="TitleCategories">Приключения</p>
    </div>
    </a>
    <a @click="isBtnClick_6 = true">
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
