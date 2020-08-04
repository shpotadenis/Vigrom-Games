<template>
<div class="popup-wrapper">
  <div class="container">
    <messageSent v-if="isBtnClick" @close="isBtnClick = false"> </messageSent>
    <div class="picture">
      <div class="pic"><img src="@/assets/img/newsletter.svg" alt="newsletter"></div>
    </div>
    <div class="form">
      <div class="form_Header">
        <div class="head-name">Поддержка</div>
        <div class="closer">
          <button @click=" $emit('close')" class="close-icon">
              <img src="@/assets/img/close-outline.svg" alt="Close">
          </button>
        </div>
      </div>
      <hr>

      <div class="form_Content">
        <div class="email">
          <div class="email-name">Контактный e-mail</div>
          <div class="input-blank">
            <input type="text" class="email-form" id="mail" placeholder="Введите e-mail"/>
          </div>
        </div>
        <div class="message">
          <div class="message-name">Ваше сообщение</div>
          <div class="msg">
            <textarea type="text" class="message-form" id="message" placeholder="Напишите что нибудь">
            </textarea>
          </div>
        </div>
      </div>
      <div class="form_Footer">
        <button @click="isBtnClick = true" class="send">Отправить</button>
      </div>
  </div>
</div>
</div>





</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>
