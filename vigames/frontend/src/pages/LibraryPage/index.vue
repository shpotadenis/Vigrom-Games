<template>
    <div>
        <div class="wrapper">
            <div class="head">
                <div class="head__header">
                    <h1 class="header__text">
                        Библиотека
                    </h1>
                </div>
                <div class="head__search">
                    <search-component></search-component>
                </div>
            </div>

            <div class="head-banner">
                <div class="head-banner__desc">
                    <h3 class="desc__header">
                        Сегодня
                    </h3>
                    <div class="desc__content">
                        <h2 class="content__header">
                            Новые инди игры уже на главной
                        </h2>
                        <p class="content__text">
                            Унитарное государство, однако, доказывает системный политический процесс в современной России
                        </p>
                        <div class="content__btn">
                            <span>
                                Подробнее
                            </span>
                            <span>
                                <img src="@/assets/img/arrow-right.png" alt="" class="btn__arrow">
                            </span>
                        </div>
                    </div>
                </div>
                <div class="head-banner__image">
                    <img src="@/assets/img/library_head-banner.png" alt="" class="head-banner__image-pic">
                </div>
            </div>
            <div class="main-content">
                <div class="main-content__header">
                    <h1 class="header__text">
                        Ваши игры
                    </h1>
                </div>
                <div class="main-content__games">
                    <div class="game-card" v-for="i in 10" :key="i">test</div>
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
