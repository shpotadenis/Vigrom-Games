<template>
  <div class="wrappen">
      <div class="GameComponentPopular">
      <div class="ImagePopular">
        <img class="ImageComponentPopular" v-bind:src="require('@/assets/img/' + Game.image)" wigth="255" height="324">
        <div class="Sale-block">
          <div class="Sale-value">СКИДКА {{Game.sale_index}} %</div>
        </div>
      </div>
        <div class="RatingAndTitlePopular">
          <router-link :to="{ name: 'singlePage', params: { id: Game.id } }">
              <p class="NameGamePopular">{{Game.name}}</p>
          </router-link>
          <p class="PriceAfter">{{Game.price_after}} <img src="@/assets/img/ruble-gold.svg" alt="Ruble"></p>
        </div>
        <div class="Footer">
          <p class="UnderNamePopular">{{Game.undername}}</p>
          <p class="PriceBefore">{{Game.price_before}} <img src="@/assets/img/ruble-gray-2.svg" alt="Ruble"></p>
        </div>


</div>
</div>
</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>
