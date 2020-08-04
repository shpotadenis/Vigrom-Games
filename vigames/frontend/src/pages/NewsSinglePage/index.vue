<template>
  <div>
  <div class="wrapper">
    <router-link :to="{name: 'newsPage'}">
    <breadcrumbs-component :items="breadcrumbs"></breadcrumbs-component>
    </router-link>
    <checkout v-if="isBtnClick" @close="isBtnClick = false"></checkout>
    <div class="container">
      <div class="Header">
        <div class="news-name">
          {{getGameData.name_news}}
        </div>
        <div class="autor-name">
          {{getGameData.autor}}
        </div>
      </div>

      <div class="Content">
        <div class="image img-1"></div>
        <div class="text">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Sed vitae quam consectetur, auctor ligula a, rutrum nisl. Aenean eget hendrerit
            arcu. Pellentesque sodales ligula eget commodo pellentesque.
            Curabitur bibendum nisi at velit vulputate efficitur. Ut tempus massa erat,
            nec ultrices mi pellentesque sit amet. Donec hendrerit id diam nec consequat.
            Praesent sit amet dui cursus, euismod est id, elementum nunc. Integer ut justo urna
          </p>
          <p>
            Curabitur bibendum nisi at velit vulputate efficitur. Ut tempus massa
            erat, nec ultrices mi pellentesque sit amet. Donec hendrerit id diam nec consequat.
            Praesent sit amet dui cursus, euismod est id, elementum nunc. Integer ut justo.
          </p>
        </div>
        <div class="image img-2"></div>
        <div class="text">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Sed vitae quam consectetur, auctor ligula a, rutrum nisl. Aenean eget hendrerit
            arcu. Pellentesque sodales ligula eget commodo pellentesque.
            Curabitur bibendum nisi at velit vulputate efficitur. Ut tempus massa erat,
            nec ultrices mi pellentesque sit amet. Donec hendrerit id diam nec consequat.
            Praesent sit amet dui cursus, euismod est id, elementum nunc. Integer ut justo urna
          </p>
          <p>
            Curabitur bibendum nisi at velit vulputate efficitur. Ut tempus massa
            erat, nec ultrices mi pellentesque sit amet. Donec hendrerit id diam nec consequat.
            Praesent sit amet dui cursus, euismod est id, elementum nunc. Integer ut justo.
          </p>
        </div>
        <div class="two-images">
          <div class="image img-3"></div>
          <div class="image img-3"></div>
        </div>
        <div class="text">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Sed vitae quam consectetur, auctor ligula a, rutrum nisl. Aenean eget hendrerit
            arcu. Pellentesque sodales ligula eget commodo pellentesque.
            Curabitur bibendum nisi at velit vulputate efficitur. Ut tempus massa erat,
            nec ultrices mi pellentesque sit amet. Donec hendrerit id diam nec consequat.
            Praesent sit amet dui cursus, euismod est id, elementum nunc. Integer ut justo urna
          </p>
          <p>
            Curabitur bibendum nisi at velit vulputate efficitur. Ut tempus massa
            erat, nec ultrices mi pellentesque sit amet. Donec hendrerit id diam nec consequat.
            Praesent sit amet dui cursus, euismod est id, elementum nunc. Integer ut justo.
          </p>
        </div>
      </div>

      <div class="info_about_game">
        <div class="info-title">
          Узнайте больше об этой игре
        </div>
        <div class="image game-img"> </div>
        <div class="info-footer">
          <div>
            <div class="game-name">{{getGameData.name_game}}</div>
            <div class="dev-name">От {{getGameData.dev}}</div>
          </div>
          <div>
            <button @click="isBtnClick = true" class="btn-buy">Купить {{getGameData.price}} <img src="@/assets/img/ruble-white.svg" alt="Ruble"></button>
          </div>
        </div>
      </div>

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
