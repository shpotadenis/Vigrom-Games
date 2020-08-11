<template>
    <div class="popup-wrapper">
      <div class="container">
        <game-returned v-if="isBtnClick" @close="isBtnClick = false">  </game-returned>
        <div class="Header">
          <div class="head-name">Вернуть игру</div>
          <div class="closer">
            <button @click=" $emit('close')" class="close-icon">
                <img src="@/assets/img/close-outline.svg" alt="Close">
            </button>
          </div>
         </div>
         <hr>

        <div class="Content">
          Вы уверены, что хотите вернуть игру “DANGER CREW”? Она станет снова
          доступна для покупки, просмотра и поиска игроками.
         </div>
        <div class="Footer">
          <button class="Btn" @click="gameReturn">Вернуть</button>
        </div>
      </div>
    </div>
</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>
