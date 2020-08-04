<template>
  <div class="PopularGameIndi">
    <div class="PopularGameTitle">
      <p class="Title">Популярное</p>
      <a src="#1" class="Link">Больше игр <img src="@/assets/img/Vector.png"></a>
    </div>
    <div class="IndiPopularGame">
      <game-card
        v-for="item in populars"
        :key="item.id"
        :Game="item"
      />
      </div>
  </div>
</template>

<script src="./LittlePopularPage.js">
</script>

<style lang="scss">
@import '@/assets/style/LittlePopularPage.scss'
</style>
