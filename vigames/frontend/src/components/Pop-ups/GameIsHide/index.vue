<template>
    <div class="popup-wrapper">
      <div class="container">
        <game-hide v-if="isBtnClick" @close="closeOk">  </game-hide>
        <div class="Header">
          <div class="head-name">Скрыть игру</div>
          <div class="closer">
            <button @click="$emit('close')" class="close-icon">
                <img src="@/assets/img/close-outline.svg" alt="Close">
            </button>
          </div>
         </div>
         <hr>

        <div class="Content" >
          Вы уверены, что хотите скрыть игру {{Gamehide.title}}? Она будет недоступна
          для покупки, просмотра и поиска игроками, а также исчезнет из ленты.
          Возможность просмотра и скачивания сохранится у игроков, купивших игру.
         </div>
        <div class="Footer">
          <button class="Btn" @click="hideGame">Cкрыть</button>
        </div>
      </div>
    </div>
</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>
