<template>
  <div class="popup-wrapper">
    <div class="container">
      <div class="messageSent_Header">
        <div class="head-name">Ваше сообщение отправлено</div>
        <div class="closer">
            <button @click=" $emit('close')" class="close-icon">
                <img src="@/assets/img/close-outline.svg" alt="Close">
            </button>
        </div>
      </div>
      <hr>

      <div class="messageSent_Container">
        <p>Наши специалисты обрабатывают ваш запрос и свяжутся с вами по e-mail.
        До встречи!</p>
      </div>
      <div class="messageSent_Footer">
        <button @click=" $emit('close')" class="iWait">Жду</button>
      </div>
    </div>
  </div>
</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>
