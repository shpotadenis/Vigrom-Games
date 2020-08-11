<template>
    <div class="search">
        <div class="SpaceBetweenImageAndText">
            <div class="SearchImage">
                <img src="@/assets/img/search-icon.png">
            </div>
            <div class="SearchText">
                <input
                        type="search"
                        class="InputFilterGames"
                        placeholder="Поиск..."
                        v-model="searchGames"
                        v-debounce:500ms="showGames"
                >
            </div>
        </div>
        <div class="BorderTop"></div>
          <div>
            <transition name="fade">
            <ul class="ListGame" v-if="searchGames.length > 0">
              <li
                v-for="(game, idx) in searchData"
                :key="game.id"
                >
                  <router-link :to="game.link" class="LinkNoStyle">
                    <div class="SearchItemGame">
                      <img :src="getImg(idx)" class="SearchItemImage">
                      <div>
                        <p class="SearchItemName">{{game.title}}</p>
                        <p class="SearchItemName">{{game.sub_title}}</p>
                      </div>
                    </div>
                  </router-link>
            </li>
                <li v-if="noResults">
                    <div class="SearchItemGame">
                        <div>
                            <p class="SearchItemName NoResults">Поиск не дал результатов</p>
                        </div>
                    </div>
                </li>
            </ul>
          </transition>
          </div>
    </div>
</template>


<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>
