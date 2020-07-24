<template>
    <div class="reviews__wrapper">
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
        <div class="reviews__replay">
            <a href="#!" class="replay__link">
                <span class="replay__text">
                    Оставить свой отзыв
                </span>
                <img src="@/assets/img/chevron-down-icon.svg" alt="" class="replay__icon">
            </a>
        </div>

        <div class="review__cards">
            <div class="review__card" v-for="review in getReviews" :key="review.id">
                <div class="review__userplate">
                    <img src="@/assets/img/userpic.png" alt="" class="userplate__pic">
                    <p class="review__username">
                        {{review.user_nickname}}
                    </p>
                </div>
                <div class="review__content">
                    <div class="review__header">
                        <h4 class="review__title">{{review.title}}</h4>
                        <div class="review__rating">
                            <img src="@/assets/img/star.png" alt="" class="review__star" v-for="i in review.rating" :key="i">
                        </div>
                    </div>
                    <div class="review__text">
                        <p>{{review.text}}</p>
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
