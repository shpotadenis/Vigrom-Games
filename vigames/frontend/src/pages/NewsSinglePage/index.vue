<template>
  <div v-if="!loading">
  <div class="wrapper">
    <router-link :to="{name: 'newsPage'}">
    <breadcrumbs-component :items="breadcrumbs"></breadcrumbs-component>
    </router-link>
    <checkout v-if="isBtnClick" @close="isBtnClick = false"></checkout>
    <div class="container">
      <div class="Header">
        <div class="news-name">
          {{newsData.title}}
        </div>
        <div class="autor-name">
          {{newsData.author}}
        </div>
      </div>

      <div class="Content">
        <img :src="getImage" class="image img-1" alt="">
        <div class="text">
          {{newsData.text}}
        </div>
      </div>

     <!-- <div class="info_about_game">
        <div class="info-title">
          Узнайте больше об этой игре
        </div>
        <div class="image game-img"> </div>
        <div class="info-footer">
          <div>
            <div class="game-name">{{newsData.name_game}}</div>
            <div class="dev-name">От {{newsData.dev}}</div>
          </div>
          <div>
            <button @click="isBtnClick = true" class="btn-buy">Купить {{newsData.price}} <img src="@/assets/img/ruble-white.svg" alt="Ruble"></button>
          </div>
        </div>
      </div> !-->

      <div class="comments">
        <comments-component id="reviews"></comments-component>
      </div>
    </div>

  </div>
    <footer-component> </footer-component>
  </div>
</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>
