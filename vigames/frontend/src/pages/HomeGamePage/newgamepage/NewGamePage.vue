<template>
  <div class="wrappen">
    <div class="NewGamePageComponent">
      <div class="NewGameTitle">
        <p class="Title">Новинки</p>
        <a src="#1" class="Link">Больше игр <img src="@/assets/img/Vector.png"></a>
      </div>
      <div class="NewsGamePage">
        <new-game-page-component
        v-for="item in news"
        :key="item.id"
        :Game="item"
        />
      </div>
    </div>
  </div>
</template>

<script src="./NewGamePage.js">
</script>
<style lang="scss">
@import '@/assets/style/NewGamePage.scss'
</style>
