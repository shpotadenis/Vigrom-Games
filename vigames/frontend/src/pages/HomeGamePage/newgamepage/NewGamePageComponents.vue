<template>

        <div class="GameComponent">
          <div class="ImageNewGame">
              <div class="rotate">
                <img class="ImageComponent" v-bind:src="require('@/assets/img/' + Game.image)">
                <div class="TextNewGame">
                <div class="ComponentImage">
                <div class="ButtonArrow">
                  <img src="@/assets/img/arrow3.png" class="strelka1" @click="leftFunc" width="40" height="40">
                  <img src="@/assets/img/arrow3.png" class="strelka2" @click="rightFunc" width="40" height="40">
                </div>
                  <swiper>
                    <swiper-slide  :style="{'margin-left': '-' + (100 * SlideNumber) + '%' }">
                      <img v-bind:src="require('@/assets/img/' + Game.scrin)" width="200" height="200">
                    </swiper-slide>
                    <swiper-slide>
                      <img v-bind:src="require('@/assets/img/' + Game.scrin1)" width="200" height="200">
                    </swiper-slide>
                    <swiper-slide>
                      <img v-bind:src="require('@/assets/img/' + Game.scrin2)" width="200" height="200">
                    </swiper-slide>
                    <swiper-slide>
                      <img v-bind:src="require('@/assets/img/' + Game.scrin3)" width="200" height="200">
                    </swiper-slide>
                  </swiper>

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
