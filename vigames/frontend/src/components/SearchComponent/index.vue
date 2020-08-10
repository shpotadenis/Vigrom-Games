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
                        v-on:input="showGames"
                >
            </div>
        </div>
        <div class="BorderTop"></div>
          <div>
            <transition name="fade">
            <ul class="ListGame" v-if="isShow">
              <li
                v-for="game in searchData"
                :key="game.id"
                >
                <div class="SearchItemGame">
                  <img src="game.image" class="SearchItemImage">
                  <div>
                    <p class="SearchItemName">{{game.name}}</p>
                    <p class="SearchItemName">{{game.price}}</p>
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
