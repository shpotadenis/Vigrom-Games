<template>
  <div class="wrappen">
      <div class="GameComponentPopular">
      <div class="AllScrin" v-if="isShow">
        <button class='Arrow1Popular' @click="leftFunc"></button>
        <button class='Arrow2Popular' @click="rightFunc"></button>
        <div class="AllScrinImage" @click="closeScrin" >
          <img
            v-bind:src="Game.scrin"
             :style="{'margin-left': '-' + (100 * SlideNumber) + '%'}"
             width="1000"
             height="500"
             class="ImageScrin"
             >
          <img
            v-bind:src="Game.scrin1"
            width="1000"
            height="500"
            class="ImageScrin"
            >
          <img
            v-bind:src="Game.scrin2"
            width="1000"
            height="500"
            class="ImageScrin"
            >
          <img
            v-bind:src="Game.scrin3"
            width="1000"
            height="500"
            class="ImageScrin"
            >
          </div>
      </div>
      <div class="ImagePopular">
        <div class="rotatePopular">
              <img class="ImageComponentPopular" v-bind:src="Game.image" wigth="255" height="324">
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
                v-bind:src="Game.scrin"
                width="220"
                height="220"
                class="AnimationSlider"
                >
            </div>
            <div>
              <img
                v-bind:src="Game.scrin1"
                width="220"
                height="220"
                class="AnimationSlider"
              >
            </div>
            <div>
              <img
                v-bind:src="Game.scrin2"
                width="220"
                height="220"
                class="AnimationSlider"
              >
            </div>
            <div>
              <img
                v-bind:src="Game.scrin3"
                width="220"
                height="220"
                class="AnimationSlider"
              >
<<<<<<< HEAD
            </div>
          </div>
            <img v-bind:src="require('@/assets/img/' + Game.icon)" class="BigScrin" @click="showScrin()">
              <div>
                <p class="TextComponentPopular">vnevnjehvnjiehv kjadb uib jab s sH YU</p>
              </div>
=======
            </swiper-slide>
          </swiper>
            <img v-bind:src="Game.icon" class="BigScrin" @click="showScrin()">
>>>>>>> 5696c1a88e4e29b0762fec4a33d46ccc8cb8b0c6
            </div>
          </div>
        </div>
      </div>
        <div class="RatingAndTitlePopular">
          <router-link :to="{ name: 'singlePage', params: { id: Game.id } }">
              <p class="NameGamePopular">{{Game.name}}</p>
          </router-link>
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
