<template>
  <div class="comments__wrapper">
      <div class="header">
          <h3 class="header__text">
              Комментарии
          </h3>
          <div class="filter">
              <a href="#!" class="filter__link">
                  <span class="filter__text">
                      Фильтр
                  </span>
                  <img src="@/assets/img/chevron-down-icon.svg" alt="" class="filter__icon">
              </a>
          </div>
      </div>
      <div class="comments__replay">
          <a href="#!" class="replay__link">
              <span class="replay__text">
                  Оставить свой комментрарий
              </span>
              <img src="@/assets/img/chevron-down-icon.svg" alt="" class="replay__icon">
          </a>
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
