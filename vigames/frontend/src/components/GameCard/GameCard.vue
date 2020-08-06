<template>
  <div class="wrappen">
      <div class="GameComponentPopular">
      <div class="AllScrin" v-if="isShow">
        <button class='Arrow1Popular' @click="leftFunc"></button>
        <button class='Arrow2Popular' @click="rightFunc"></button>
        <div class="AllScrinImage" @click="closeScrin" >
          <img
            v-bind:src="require('@/assets/img/' +   Game.scrin)"
             :style="{'margin-left': '-' + (100 * SlideNumber) + '%'}"
             width="1000"
             height="500"
             class="ImageScrin"
             >
          <img
            v-bind:src="require('@/assets/img/' +   Game.scrin1)"
            width="1000"
            height="500"
            class="ImageScrin"
            >
          <img
            v-bind:src="require('@/assets/img/' +   Game.scrin2)"
            width="1000"
            height="500"
            class="ImageScrin"
            >
          <img
            v-bind:src="require('@/assets/img/' +   Game.scrin3)"
            width="1000"
            height="500"
            class="ImageScrin"
            >
          </div>
      </div>
      <div class="ImagePopular">
        <div class="rotatePopular">
              <img class="ImageComponentPopular" v-bind:src="require('@/assets/img/' + Game.image)" wigth="255" height="324">
          <div class="TextNewGamePopular">
          <div class="ComponentImagePopular">
          <div class="AllSlide">
            <button class='strelk1Popular' @click="leftFunc"></button>
            <button class='strelk2Popular' @click="rightFunc"></button>
            <div
               :style="{'margin-left': '-' + (100 * SlideNumber) + '%' }"
               class="AnimationSlider"
             >
              <img
                v-bind:src="require('@/assets/img/' + Game.scrin)"
                width="220"
                height="220"
                class="AnimationSlider"
                >
            </div>
            <div>
              <img
                v-bind:src="require('@/assets/img/' + Game.scrin1)"
                width="220"
                height="220"
                class="AnimationSlider"
              >
            </div>
            <div>
              <img
                v-bind:src="require('@/assets/img/' + Game.scrin2)"
                width="220"
                height="220"
                class="AnimationSlider"
              >
            </div>
            <div>
              <img
                v-bind:src="require('@/assets/img/' + Game.scrin3)"
                width="220"
                height="220"
                class="AnimationSlider"
              >
            </div>
          </div>
            <img v-bind:src="require('@/assets/img/' + Game.icon)" class="BigScrin" @click="showScrin()">
              <div>
                <p class="TextComponentPopular">vnevnjehvnjiehv kjadb uib jab s sH YU</p>
              </div>
            </div>
          </div>
        </div>
      </div>
        <div class="RatingAndTitlePopular">
          <p class="NameGamePopular">{{Game.name}}</p>
            <p class="PricePopular">{{Game.price}}</p>
        </div>
        <p class="UnderNamePopular">{{Game.undername}}</p>
      </div>

</div>
</template>

<script src='./GameCard.js'>
</script>

<style lang='scss'>
@import '@/assets/style/GameCard.scss'
</style>
