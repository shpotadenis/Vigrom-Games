<template>
    <div class="popup-wrapper">
      <div class="container">
        <div class="goDownload_Header">
          <div class="head-name">Спасибо за покупку!</div>
          <div class="closer">
            <button @click=" $emit('close')" class="close-icon">
                <img src="@/assets/img/close-outline.svg" alt="Close">
            </button>
          </div>
         </div>
         <hr>

        <div class="goDownload_Content">
          Теперь вы можете скачать файл на свой компьютер. Приятной игры!
         </div>
        <div class="goDownload_Footer">
          <button class="download">Cкачать</button>
        </div>
      </div>
    </div>
</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>
