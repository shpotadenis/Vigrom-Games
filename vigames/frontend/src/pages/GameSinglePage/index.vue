<template>
    <div>
    <div class="wrapper">
        <breadcrumbs-component :items="breadcrumbs"></breadcrumbs-component>
        <checkout v-if="isBtnClick" @close="isBtnClick = false"></checkout>
        <div class="game-card">
            <div class="game-card__banner banner">
                <img src="@/assets/img/top_banner.png" alt="Banner of game" class="full-banner">
                <div class="banner__right">
                    <img src="@/assets/img/chevron-right-icon.svg" alt="" class="banner__right-pic">
                </div>
                <div class="banner__left">
                    <img src="@/assets/img/chevron-right-icon.svg" alt="" class="banner__left-pic">
                </div>
            </div>
            <div class="info-card">
                <div class="info-card__about">
                    <h2 class="info-card__title">
                        {{getGameData.name}}
                    </h2>
                    <p class="info-card__author">
                        От {{getGameData.dev}}
                    </p>
                </div>
                <div class="info-card__buy">
                    <button @click="isBtnClick = true" class="buy__btn">
                        Купить
                        <span class="buy__price">
                            {{getGameData.price}}
                            <img src="@/assets/img/ruble-white.svg" alt="" class="buy__btn-ruble">
                        </span>
                    </button>
                </div>
            </div>
        </div>

        <div class="about-game">
            <h2 class="game-info__about">
                Об игре
            </h2>

            <div class="game-info">
                <div class="game-info__desc">
                    <p>
                        {{getGameData.desc}}
                    </p>
                    <a v-scroll-to="'#reviews'" class="desc__show-reviews">
                        Посмотреть отзывы
                    </a>
                </div>
                <div class="game__categories">
                    <ul class="category__titles">
                        <li class="category__title">
                            Разработчик:
                        </li>
                        <li class="category__title">
                            Категория:
                        </li>
                        <li class="category__title">
                            Рейтинг:
                        </li>
                        <li class="category__title">
                            Совместимость:
                        </li>
                        <li class="category__title">
                            Размер:
                        </li>
                        <li class="category__title">
                            Языки:
                        </li>
                    </ul>
                    <ul class="category__values">
                        <li class="value">
                            {{getGameData.dev}}
                        </li>
                        <li class="value">
                            {{getGameData.category}}
                        </li>
                        <li class="value">
                            {{getGameData.rating}}
                        </li>
                        <li class="value">
                            {{getGameData.compatible}}
                        </li>
                        <li class="value">
                            {{getGameData.size}}
                        </li>
                        <li class="value">
                            <div v-for="lang in getGameData.languages" :key="lang">
                                {{lang}} <br>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="wrapper_2">
            <img src="@/assets/img/game-pic2.png" alt="" class="full-banner">
            <div class="desc__text">
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae quam consectetur, auctor ligula a, rutrum nisl. Aenean eget hendrerit arcu. Pellentesque sodales ligula eget commodo pellentesque. Curabitur bibendum nisi at velit vulputate efficitur. Ut tempus massa erat, nec ultrices mi pellentesque sit amet. Donec hendrerit id diam nec consequat. Praesent sit amet dui cursus, euismod est id, elementum nunc. Integer ut justo urna.
                </p>
            </div>
            <img src="@/assets/img/game-pic3.png" alt="" class="full-banner">
            <div class="desc__text">
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae quam consectetur, auctor ligula a, rutrum nisl. Aenean eget hendrerit arcu. Pellentesque sodales ligula eget commodo pellentesque. Curabitur bibendum nisi at velit vulputate efficitur. Ut tempus massa erat, nec ultrices mi pellentesque sit amet. Donec hendrerit id diam nec consequat. Praesent sit amet dui cursus, euismod est id, elementum nunc. Integer ut justo urna.
                </p>
            </div>
            <div class="grid-images">
                <img src="@/assets/img/game-pic4.png" alt="" class="full-banner">
                <img src="@/assets/img/game-pic5.png" alt="" class="full-banner">
            </div>
            <div class="desc__text">
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae quam consectetur, auctor ligula a, rutrum nisl. Aenean eget hendrerit arcu. Pellentesque sodales ligula eget commodo pellentesque. Curabitur bibendum nisi at velit vulputate efficitur. Ut tempus massa erat, nec ultrices mi pellentesque sit amet. Donec hendrerit id diam nec consequat. Praesent sit amet dui cursus, euismod est id, elementum nunc. Integer ut justo urna.
                </p>
            </div>
            <img src="@/assets/img/game-pic6.png" alt="" class="full-banner">
        </div>
        <reviews-component id="reviews"></reviews-component>
        <div class="wrapper_2">
            <img src="@/assets/img/top_banner.png" alt="" class="full-banner">
            <div class="privacy-policy">
                <a href="#!" class="privacy-policy__link">
                    Политика конфиденциальности
                </a>
            </div>
        </div>
    </div>
        <footer-component></footer-component>
    </div>
</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>
