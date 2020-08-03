<template>
  <div class="wrappen">
      <div class="GameComponentPopular">
      <div class="ImagePopular">
        <div class="rotatePopular">
              <img class="ImageComponentPopular" v-bind:src="require('@/assets/img/' + Game.image)" wigth="255" height="324">
          <div class="TextNewGamePopular">
          <div class="ComponentImagePopular">
              <div>
                <p class="TextComponentPopular">vnevnjehvnjiehv kjadb uib jab s sH YU</p>
              </div>
            </div>
          </div>
        </div>
      </div>
        <div class="RatingAndTitlePopular">
          <p class="NameGamePopular">{{Game.name}}</p>
          <div class="RatingGamePopular">{{Game.rating}}</div>
        </div>
        <p class="UnderNamePopular">{{Game.undername}}</p>
        <p class="PricePopular">{{Game.price}}</p>
      </div>

</div>
</template>

<script src='./LittlePopularPageComponents.js'>
</script>

<style lang='scss'>
@import '@/assets/style/LittlePopularPageComponents.scss'
</style>
