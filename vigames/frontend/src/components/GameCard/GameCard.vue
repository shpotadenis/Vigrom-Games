<template>
  <div class="wrappen">
      <div class="GameComponentPopular">
      <div class="AllScrin" v-if="isShow">
        <div class="Arrow">
          <img src="@/assets/img/Vector.svg" class="Arrow1Popular" @click="leftFunc" width="100" height="100">
        </div>
        <div class="Arrow">
          <img src="@/assets/img/Vector.svg" class="Arrow2Popular" @click="rightFunc" width="100" height="100">
        </div>
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

          <img src="@/assets/img/Vector.svg" class="strelk1Popular" @click="leftFunc" width="40" height="40">
          <img src="@/assets/img/Vector.svg" class="strelk2Popular" @click="rightFunc" width="40" height="40">

          <swiper class="AllSlide">
            <swiper-slide
               :style="{'margin-left': '-' + (100 * SlideNumber) + '%' }"
               class="AnimationSlider"
             >
              <img
                v-bind:src="Game.scrin"
                width="220"
                height="220"
                class="AnimationSlider"
                >
            </swiper-slide>
            <swiper-slide>
              <img
                v-bind:src="Game.scrin1"
                width="220"
                height="220"
                class="AnimationSlider"
              >
            </swiper-slide>
            <swiper-slide>
              <img
                v-bind:src="Game.scrin2"
                width="220"
                height="220"
                class="AnimationSlider"
              >
            </swiper-slide>
            <swiper-slide>
              <img
                v-bind:src="Game.scrin3"
                width="220"
                height="220"
              >
            </swiper-slide>
          </swiper>
            <img v-bind:src="Game.icon" class="BigScrin" @click="showScrin()">
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
