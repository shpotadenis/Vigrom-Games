<template>
  <div class="comments__wrapper">
      <div class="header">
          <h3 class="header__text">
              Комментарии
          </h3>
      </div>
      <div class="comments__replay">
          <a class="replay__link" @click="commentFormShow = !commentFormShow">
              <div class="replay__text" v-if="!commentFormShow">
                  Оставьте свой комментарий
              </div>
              <div class="replay__text" v-else>
                  Скрыть
              </div>
              <div><img src="@/assets/img/chevron-down-icon.svg" :class="{ activeForm: commentFormShow }"  alt="" class="replay__icon"></div>
          </a>
      </div>

      <div v-if="commentFormShow">
        <div class="send_block">
          <textarea type="text" class="sms" id="message" v-model="message" placeholder="Оставьте свой комментарий">
          </textarea>
        </div>
        <div>
          <button class="send_btn" :disabled="message.length == 0" @click="sendCommentClick">Отправить</button>
        </div>
      </div>

      <div class="comments__cards">
          <comment-component v-for="comment in comments"
                             :commentData="comment"
                             :key="comment.id">
          </comment-component>
      </div>
  </div>
</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>
