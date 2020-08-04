<template>
<div>
  <div class="CategoriesGame">
    <ul class="AllChooseUL">
      <li class="AllChooseLi"><a href="#!">Категории <img src="@/assets/img/VectorBottom.svg"></a> </li>
      <li class="AllChooseLi"><a href="#!">Скидки</a></li>
      <router-link :to="{name: 'freeGames'}"  style="text-decoration:none">
        <li class="AllChooseLi">Бесплатные игры</li>
      </router-link>
      <li class="AllChooseLi"><a href="#!">Ранний доступ</a></li>
    </ul>
  </div>
</div>
</template>
<script src="./InternalMenu.js">
</script>
<style lang="scss">
@import '@/assets/style/InternalMenu.scss'
</style>
