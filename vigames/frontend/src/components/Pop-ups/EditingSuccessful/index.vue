<template>
    <div class="popup-wrapper">
      <div class="container">
        <div class="Header">
          <div class="head-name">Игра отредактирована!</div>
          <div class="closer">
            <button @click=" $emit('close')" class="close-icon">
                <img src="@/assets/img/close-outline.svg" alt="Close">
            </button>
          </div>
         </div>
         <hr>

        <div class="Content">
          Данные о вашей игре обновлены.
         </div>
        <div class="Footer">
          <button @click=" $emit('close')" class="Btn">Понятно</button>
        </div>
      </div>
    </div>
</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>
