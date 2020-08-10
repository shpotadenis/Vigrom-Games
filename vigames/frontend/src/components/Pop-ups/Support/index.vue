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
          <div>
            <label class="email-name" for="mail">Контактный e-mail</label>
            <error-message :error="error_mail[0]"
                           v-show="error_mail.length>0">
            </error-message>
          </div>
          <div class="input-blank">
            <input type="text"
                   v-model="mail"
                   class="email-form"
                   id="mail"
                   placeholder="Введите e-mail"/>
          </div>
        </div>
        <div class="message">
          <div>
            <label class="message-name" for="message">Контактный e-mail</label>
            <error-message :error="error_mess[0]"
                           v-show="error_mess.length>0">
            </error-message>
          </div>
          <div class="msg">
            <textarea type="text"
                      class="message-form"
                      id="message"
                      v-model="mess"
                      placeholder="Напишите что нибудь">
            </textarea>
          </div>
        </div>
      </div>
      <div class="form_Footer">
        <button @click="checkForm" class="send">Отправить</button>
      </div>
  </div>
</div>
</div>





</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>
