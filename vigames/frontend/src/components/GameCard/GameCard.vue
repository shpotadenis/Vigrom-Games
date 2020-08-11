<template>
  <div class="wrappen">
      <div class="GameComponentPopular">
      <div class="ImagePopular">
        <img class="ImageComponentPopular" v-bind:src="Game.image" wigth="255" height="324">
        <div v-if="Game.sale > 0" class="Sale-block">
          <div class="Sale-value">СКИДКА {{Game.sale}} %</div>
        </div>
      </div>
        <div class="RatingAndTitlePopular">
          <router-link :to="{ name: 'singlePage', params: { id: Game.id } }">
              <p class="NameGamePopular">{{Game.name}}</p>
          </router-link>
          <p v-if="Game.sale == 0" class="PricePopular">{{Game.price}}</p>
          <p v-if="Game.sale > 0" class="PriceAfter">{{Math.floor(((Game.price * (100-Game.sale))/100)*100)/100}} <img src="@/assets/img/ruble-gold.svg" alt="Ruble"></p>
        </div>

        <div class="Footer">
          <p class="UnderNamePopular">{{Game.undername}}</p>
          <p v-if="Game.sale > 0" class="PriceBefore">{{Game.price}} <img src="@/assets/img/ruble-gray-2.svg" alt="Ruble"></p>
        </div>
    </div>
</div>
</template>

<script src='./GameCard.js'>
</script>

<style lang='scss'>
@import '@/assets/style/GameCard.scss'
</style>
