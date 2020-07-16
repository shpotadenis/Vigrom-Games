<template>
    <div class="wrapper">
        <div class="game-card">
            <img src="@/assets/img/top_banner.png" alt="Banner of game" class="full-banner">
            <div class="info-card">
                <h2 class="info-card__title">
                    Название игры
                </h2>
                <p class="info-card__author">
                    От Имя Разработчика
                </p>
                <div class="info-card__buy">
                    <a href="#!" class="buy__btn">Купить</a>
                    <span class="buy__price">125 Р</span>
                </div>
            </div>
        </div>

        <div class="about-game">
            <h2 class="game-info__about">
                Об игре
            </h2>

            <div class="game-info">
                <div class="game-info__desc">
                    <div>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae quam consectetur, auctor ligula a, rutrum nisl. Aenean eget hendrerit arcu. Pellentesque sodales ligula eget commodo pellentesque. Curabitur bibendum nisi at velit vulputate efficitur. Ut tempus massa erat, nec ultrices mi pellentesque sit amet. Donec hendrerit id diam nec consequat. Praesent sit amet dui cursus, euismod est id, elementum nunc. Integer ut justo urna.
                            Sed bibendum sollicitudin commodo. Curabitur sollicitudin, nisl a mattis egestas, mi metus iaculis nisi, et ornare eros orci cursus leo.</p>
                    </div>
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
                            Название
                        </li>
                        <li class="value">
                            Название
                        </li>
                        <li class="value">
                            Название
                        </li>
                        <li class="value">
                            Название
                        </li>
                        <li class="value">
                            Название
                        </li>
                        <li class="value">
                            Название
                        </li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="wrapper_2">
            <img src="@/assets/img/pic1.png" alt="" class="full-banner">
            <div class="desc__text">
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae quam consectetur, auctor ligula a, rutrum nisl. Aenean eget hendrerit arcu. Pellentesque sodales ligula eget commodo pellentesque. Curabitur bibendum nisi at velit vulputate efficitur. Ut tempus massa erat, nec ultrices mi pellentesque sit amet. Donec hendrerit id diam nec consequat. Praesent sit amet dui cursus, euismod est id, elementum nunc. Integer ut justo urna.
                </p>
            </div>
            <img src="@/assets/img/pic2.png" alt="" class="full-banner">
            <div class="desc__text">
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae quam consectetur, auctor ligula a, rutrum nisl. Aenean eget hendrerit arcu. Pellentesque sodales ligula eget commodo pellentesque. Curabitur bibendum nisi at velit vulputate efficitur. Ut tempus massa erat, nec ultrices mi pellentesque sit amet. Donec hendrerit id diam nec consequat. Praesent sit amet dui cursus, euismod est id, elementum nunc. Integer ut justo urna.
                </p>
            </div>
            <div class="grid-images">
                <img src="@/assets/img/pic3.png" alt="" class="full-banner">
                <img src="@/assets/img/pic4.png" alt="" class="full-banner">
            </div>
            <div class="desc__text">
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae quam consectetur, auctor ligula a, rutrum nisl. Aenean eget hendrerit arcu. Pellentesque sodales ligula eget commodo pellentesque. Curabitur bibendum nisi at velit vulputate efficitur. Ut tempus massa erat, nec ultrices mi pellentesque sit amet. Donec hendrerit id diam nec consequat. Praesent sit amet dui cursus, euismod est id, elementum nunc. Integer ut justo urna.
                </p>
            </div>
            <img src="@/assets/img/pic2.png" alt="" class="full-banner">
        </div>
        <reviews-component></reviews-component>
        <div class="wrapper_2">
            <img src="@/assets/img/top_banner.png" alt="" class="full-banner">
            <div class="privacy-policy">
                <a href="#!" class="privacy-policy__link">
                    Политика конфиденциальности
                </a>
            </div>
        </div>
    </div>
</template>

<script>
    import ReviewsComponent from "@/components/ReviewsComponent";

    export default {
        name: "GameSinglePage",
        components: {
            ReviewsComponent
        }
    }
</script>

<style scoped>
    .wrapper {
        margin: 0 auto;
        max-width: 1139px;
    }

    .game-card {
        width: 100%;
        height: auto;
        position: relative;
        margin-top: 30px;
        margin-bottom: 200px;
    }

    .info-card {
        max-width: 322px;
        background: #fff;
        position: absolute;
        bottom: 0;
        left: 67px;
        padding: 30px 86px 30px 30px;
    }

    .info-card__title {
        font-weight: bold;
        font-size: 18px;
        line-height: 21px;
        color: #000000;
        margin-bottom: 15px;
    }

    .info-card__author {
        margin-bottom: 20px;
    }

    .info-card p, .info-card span {
        font-size: 14px;
        line-height: 16px;
        color: #000000;
    }

    .info-card__buy {
        display: flex;
        flex-wrap: wrap;
    }

    .buy__price {
        font-weight: bold;
        margin-left: 30px;
        margin-top: 11px;
    }

    .buy__btn {
        padding: 11px 46px;
        text-decoration: none;
        background-color: #828282;
        font-size: 14px;
        line-height: 16px;
        font-weight: bold;
        color: #000000;
    }

    .about-game {
        margin: 200px 366px 0 97px;
    }

    .game-info {
        display: grid;
        grid-template-columns: 60% 40%;
        gap: calc(100% * 0.09);
    }

    .game__categories {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
    }


    .category__titles, .category__values {
        display: grid;
        grid-template-rows: repeat(6, 1fr);
        grid-row-gap: 20px;
    }

    .game-info__about {
        font-weight: bold;
        font-size: 18px;
        line-height: 21px;
        color: #000000;
        margin-bottom: 30px;
    }

    .about-game p, li {
        line-height: 16px;
        color: rgba(0, 0, 0, 0.8);
    }

    .full-banner {
        width: 100%;
        overflow: hidden;
    }

    .wrapper_2 {
        margin: 200px auto;
        max-width: 946px;
    }

    .desc__text {
        margin: 120px 0;
        font-weight: normal;
        font-size: 14px;
        line-height: 16px;
        color: rgba(0, 0, 0, 0.8);
    }

    .grid-images {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 31px;
    }

    .privacy-policy {
        margin-left: 367px;
        margin-top: 30px;
    }

    .privacy-policy__link {
        text-decoration: none;
        font-size: 14px;
        line-height: 16px;
        color: rgba(0, 0, 0, 0.8);
    }
</style>