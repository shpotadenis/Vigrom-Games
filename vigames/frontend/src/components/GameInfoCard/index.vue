<template>
  <div class="wrapper">
    <div class="container">
      <game-is-hide v-if="Hide" @close="Hide = false">  </game-is-hide>
      <game-is-return v-if="Return" @close="Return = false">  </game-is-return>
      <hr>
      <div class="all-item">
        <div class="game-scrin">
          <img v-bind:src="require('@/assets/img/' + Game_Info_Card.image)" class="game-image" :class='{"Hide-img": isHide}'>
        </div>
        <div class="content">
          <div class="game-title">
            <div class="game-name">{{Game_Info_Card.name}}</div> <div class="notification" v-if="isHide">(Игра скрыта)</div>
          </div>
          <div class="views">
            <div class="views-name">Всего просмотров</div>
            <div class="views-value">{{Game_Info_Card.views}}</div>
          </div>
          <div class="purchases">
            <div class="purchases-name">Покупок</div>
            <div class="purchases-value">{{Game_Info_Card.purchases}}</div>
          </div>
          <div class="details">
            <p>Подробнее</p>
            <img src="@/assets/img/VectorPig.svg" class="arrow-pig">
          </div>
          <div class="Btns">
            <div>
              <router-link :to="{name: 'EditPage'}">
              <button class="Btn-1">Редактировать</button>
              </router-link>
            </div>
            <div>
              <button v-if="!isHide" @click="HideGame" class="Btn-2">
                Скрыть игру
              </button>
              <button v-if="isHide" @click="ReturnGame" class="Btn-2">
                Вернуть игру
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>
