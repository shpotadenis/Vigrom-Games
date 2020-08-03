<template>

        <div class="GameComponent" >
            <div class="AllScrin" v-if="isShow">
              <div class="Arrow">
                <img src="@/assets/img/arrow3.png" class="Arrow1" @click="leftFunc" width="100" height="100">
              </div>
              <div class="Arrow">
                <img src="@/assets/img/arrow3.png" class="Arrow2" @click="rightFunc" width="100" height="100">
              </div>
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
          <div class="ImageNewGame">
              <div class="rotate">
                <img class="ImageComponent" v-bind:src="require('@/assets/img/' + Game.image)">
                <div class="TextNewGame">
                <div class="ComponentImage">

                  <img src="@/assets/img/arrow3.png" class="strelk1" @click="leftFunc" width="40" height="40">
                  <img src="@/assets/img/arrow3.png" class="strelk2" @click="rightFunc" width="40" height="40">

                  <swiper class="AllSlide">
                    <swiper-slide
                       :style="{'margin-left': '-' + (100 * SlideNumber) + '%' }"
                       class="AnimationSlider"
                     >
                      <img
                        v-bind:src="require('@/assets/img/' + Game.scrin)"
                        width="200"
                        height="200"
                        >
                    </swiper-slide>
                    <swiper-slide>
                      <img
                        v-bind:src="require('@/assets/img/' + Game.scrin1)"
                        width="200"
                        height="200"
                      >
                    </swiper-slide>
                    <swiper-slide>
                      <img
                        v-bind:src="require('@/assets/img/' + Game.scrin2)"
                        width="200"
                        height="200"
                      >
                    </swiper-slide>
                    <swiper-slide>
                      <img
                        v-bind:src="require('@/assets/img/' + Game.scrin3)"
                        width="200"
                        height="200"
                      >
                    </swiper-slide>
                  </swiper>

                    <img v-bind:src="require('@/assets/img/' + Game.icon)" class="BigScrin" @click="showScrin()">

                </div>
                  <p class="TextComponent">vnevnjehvnjiehv kjadb uib jab s sH YU</p>
                </div>
            </div>
          </div>
          <div class="RatingAndTitle">
            <p class="NameGame">{{Game.name}}</p>
            <div class="RatingGame">{{Game.rating}}</div>
          </div>
          <p class="UnderName">{{Game.undername}}</p>
          <p class="Price">{{Game.price}}</p>
        </div>


</template>

<script src="./NewGamePageComponents.js">
</script>
<style lang="scss">
@import '@/assets/style/NewGamePageComponents.scss'
</style>
