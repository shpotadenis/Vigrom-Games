<template>
  <div class="wrappen">
      <div class="GameComponent">
      <div class="ImagePopular">
        <img v-bind:src="require('@/assets/img/' + Game.image)" wigth="255" height="324">
      </div>
        <div class="RatingAndTitle">
          <p class="NameGame">{{Game.name}}</p>
          <div class="RatingGame">{{Game.rating}}</div>
        </div>
        <p class="UnderName">{{Game.undername}}</p>
        <p class="Price">{{Game.price}}</p>
      </div>

  </div>
</template>

<script src='./LittlePopularPageComponents.js'>
</script>

<style lang='scss'>
@import '@/assets/style/LittlePopularPageComponents.scss'
</style>
