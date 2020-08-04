<template>
<div>
  <div class="CategoriesGame">
    <ul class="AllChooseUL">
      <li class="AllChooseLi">
        Категории
        <img src="@/assets/img/VectorBottom.svg">
      </li>
      <router-link :to="{name: 'discountsGame'}" class="AllChooseLi">
        Скидки
      </router-link>
      <router-link :to="{name: 'freeGames'}" class="AllChooseLi">
        Бесплатные игры
      </router-link>
      <router-link :to="{name: 'earlyAccessGame'}" class="AllChooseLi">
        Ранний доступ
      </router-link>
    </ul>
  </div>
</div>
</template>
<script src="./InternalMenu.js">
</script>
<style lang="scss">
@import '@/assets/style/InternalMenu.scss';
  .AllChooseLi{
    text-decoration: none;
  }
</style>
