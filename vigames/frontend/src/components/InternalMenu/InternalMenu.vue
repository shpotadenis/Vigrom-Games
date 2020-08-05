<template>
<div>
  <div class="CategoriesGame">
    <ul class="AllChooseUL">
      <li class="AllChooseLi" @click="showCategories">
        Категории
        <img src="@/assets/img/VectorBottom.svg">
      </li>
      <transition name="Animation">
        <div class="AllCategoriesItem" v-show="isCategories">
            <ul class="AllUlBlock">
              <li class="LiBlock">Жанры игр</li>
              <li class="LiBlock">Платформа</li>
            </ul>
            <div class="LinkGerne">
              <ul class="UlComponent">
                  <li class="LiBlock1">Приключения</li>
                  <li class="LiBlock1">Головоломки</li>
                  <li class="LiBlock1">Экшн</li>
                  <li class="LiBlock1">РПГ</li>
              </ul>
              <ul class="UlComponent">
                  <li class="LiBlock1">Стратегии</li>
                  <li class="LiBlock1">Фермы</li>
                  <li class="LiBlock1">ММО</li>
                  <li class="LiBlock1">Шутеры</li>
              </ul>
              <ul class="UlComponent">
                  <li class="LiBlock1">Гонки</li>
                  <li class="LiBlock1">Симуляторы</li>

              </ul>
              <ul class="UlComponent">
                  <li class="LiBlock1">Windows</li>
                  <li class="LiBlock1">MacOS</li>

              </ul>
            </div>
        </div>
      </transition>
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
