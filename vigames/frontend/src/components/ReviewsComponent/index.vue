<template>
    <div class="reviews__wrapper" v-if="!loading">
        <div class="header">
            <h3 class="header__text">
                Отзывы
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
        <div>
            <div class="reviews__replay" v-if="canReview">
                <a class="replay__link" @click="reviewFormShow = !reviewFormShow">
                    <span class="replay__text" v-if="!reviewFormShow">
                        Оставить свой отзыв
                    </span>
                    <span class="replay__text" v-else>
                        Скрыть
                    </span>
                    <img src="@/assets/img/chevron-down-icon.svg" :class="{ activeForm: reviewFormShow }" alt="" class="replay__icon">
                </a>
            </div>
            <div id="window" v-if="reviewFormShow">
                <div class="send_block">
                    <div class="review__header">
                        <div class="review__title">
                            <input type="text" class="sms__header" v-model="title" placeholder="Заголовок">
                        </div>
                        <StarComponent @rating-select="selectedRating" class="review__rating"></StarComponent>
                    </div>
                  <textarea type="text" class="sms" id="message" v-model="content" placeholder="Оставьте свой отзыв">
                  </textarea>
                </div>
                <div>
                    <button class="send_btn" @click="sendBtnClick">Отправить</button>
                </div>
            </div>
        </div>
        <div class="review__cards" v-if="this.reviews.length > 0">
            <div class="review__card" v-for="(review, idx) in this.reviews" :key="idx">
                <div class="review__userplate">
                    <img src="@/assets/img/userpic.png" alt="" class="userplate__pic" v-if="review.avatar == 'None'">
                    <img :src="getImage(idx)" alt="" class="userplate__pic">
                    <p class="review__username">
                        {{review.author}}
                    </p>
                </div>
                <div class="review__content">
                    <div class="review__header">
                        <h4 class="review__title">{{review.title}}</h4> <!-- Заголовок отзыва !-->
                        <div class="review__rating">
                            <img src="@/assets/img/star-filled.svg" alt="" class="review__star" v-for="i in review.mark" :key="'r' + i + review.id">
                            <img src="@/assets/img/star.svg" alt="" class="review__star" v-for="i in 5 - review.mark" :key="'rf' + i + review.id">
                        </div>
                    </div>
                    <div class="review__text">
                        <p>{{review.comment}}</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="review__cards" v-else>

        </div>
    </div>
</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>
