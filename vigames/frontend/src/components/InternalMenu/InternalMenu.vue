<template>
<div>
  <div class="CategoriesGame">
    <ul class="AllChooseUL">
      <li class="AllChooseLi" @click="showCategories">
        Жанры
        <img src="@/assets/img/VectorBottom.svg">
      </li>
      <transition name="Animation">
        <div class="AllCategoriesItem" v-show="isCategories" @mouseleave="mouseleave">
            <ul class="AllUlBlock">
              <li class="LiBlock">Жанры игр</li>
              <li class="LiBlock">Платформа</li>
            </ul>
            <div class="LinkGerne">
              <ul class="UlComponent">
                  <router-link :to="{name: 'AdventuresGame'}" class="LiBlock1">Приключения</router-link>
                  <router-link :to="{name: 'PuzzleGame'}" class="LiBlock1">Головоломки</router-link>
                  <router-link :to="{name: 'ActionGame'}" class="LiBlock1">Экшн</router-link>
                  <router-link :to="{name: 'RPGGame'}" class="LiBlock1">РПГ</router-link>
              </ul>
              <ul class="UlComponent">
                  <router-link :to="{name: 'StrategyGame'}" class="LiBlock1">Стратегии</router-link>
                  <router-link :to="{name: 'FarmGame'}" class="LiBlock1">Фермы</router-link>
                  <router-link :to="{name: 'MMOGame'}" class="LiBlock1">ММО</router-link>
                  <router-link :to="{name: 'ShooterGame'}" class="LiBlock1">Шутеры</router-link>
              </ul>
              <ul class="UlComponent">
                  <router-link :to="{name: 'RaceGame'}" class="LiBlock1">Гонки</router-link>
                  <router-link :to="{name: 'SimulatorGame'}" class="LiBlock1">Симуляторы</router-link>

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
