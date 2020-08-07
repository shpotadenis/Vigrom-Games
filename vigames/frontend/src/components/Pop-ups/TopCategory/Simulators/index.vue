<template>
  <div class="popup-wrapper">
  <div class="scroll-opacity">
    <div class="container">
      <div class="Header">
        <div class="head-name" >
          Топ 10 игр в категории Симуляторы
        </div>
        <div class="closer">
          <button @click=" $emit('close')" class="close-icon">
              <img src="@/assets/img/close-outline.svg" alt="Close">

          </button>
        </div>
      </div>
      <hr>

      <div class="Content">
        <game-info-card
          v-for="info in GameInfoCard"
          :key="info.id"
          :Game_Info_Card="info"
        />
      </div>
    </div>
  </div>
</div>

</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>
