<template>
  <div class="wrapper">
    <div class="container">
      <div v-if="Hide">
      <game-is-hide @close="Hide = false" :Gamehide="this.Game_Info_Card" @hide-game="hide">  </game-is-hide>
    </div>
    <div v-if="Return">
      <game-is-return @close="Return = false" :Gamereturn="this.Game_Info_Card" @show-game="show">  </game-is-return>
    </div>
      <hr>
      <div class="all-item">
        <div class="game-scrin">
          <img v-bind:src="getImage" class="game-image" :class='{"Hide-img": isHide}'>
        </div>
        <div class="content">
          <div class="game-title">
            <div class="game-name">{{Game_Info_Card.title}}</div> <div class="notification" v-if="isHide">(Игра скрыта)</div>
          </div>
          <div class="views">
            <div class="views-name">Всего просмотров</div>
            <div class="views-value">{{Game_Info_Card.count_views}}</div>
          </div>
          <div class="purchases">
            <div class="purchases-name">Покупок</div>
            <div class="purchases-value">{{Game_Info_Card.count_players}}</div>
          </div>
          <router-link :to="{name: 'singlePage', params: { id: Game_Info_Card.id }}">
            <div class="details">
              <p>Подробнее</p>
              <img src="@/assets/img/VectorPig.svg" class="arrow-pig">
            </div>
          </router-link>
          <div class="Btns">
            <div>
              <router-link :to="{name: 'EditPage', params: { id: Game_Info_Card.id }}">
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
