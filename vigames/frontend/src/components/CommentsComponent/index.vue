<template>
  <div class="comments__wrapper">
      <div class="header">
          <h3 class="header__text">
              Комментарии
          </h3>
      </div>
      <div class="comments__replay">
          <a href="#window" class="replay__link">
              <div class="replay__text">
                  Оставьте свой комментарий
              </div>
              <div><img src="@/assets/img/chevron-down-icon.svg" alt="" class="replay__icon"></div>
          </a>
      </div>

      <div id="window">
        <div class="send_block">
          <textarea type="text" class="sms" id="message" placeholder="Оставьте свой комментарий">
          </textarea>
        </div>
        <div>
          <button class="send_btn">Отправить</button>
        </div>
      </div>

      <div class="comments__cards">
          <div class="comments__card" v-for="comments in getComments" :key="comments.id">
              <div class="comments__userplate">
                  <img src="@/assets/img/userpic.png" alt="avatar" class="userplate__pic">
              </div>
              <div class="comments__content">
                  <div class="comments__header">
                      <h4 class="comments__username">{{comments.user_nickname}}</h4>
                  </div>
                  <div class="comments__text">
                      <p>{{comments.text}}</p>
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
