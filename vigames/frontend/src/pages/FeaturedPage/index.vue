<template>
    <div>
        <div class="wrapper">
            <div class="head">
                <div class="head__header">
                    <h1 class="header__text">
                        Избранное
                    </h1>
                </div>
                <div class="head__search">
                    <search-component></search-component>
                </div>
            </div>

            <banner-component day="Сегодня"
                              header="Новые инди игры уже на главной"
                              description="Унитарное государство, однако, доказывает системный политический процесс в современной России"
                              btn_caption="Подробнее"
                              :btn_route="{ name: 'homePage' }">
            </banner-component>

            <div class="main-content">
                <div class="main-content__header">
                    <h1 class="header__text">
                        Избранные игры
                    </h1>
                </div>
                <div class="main-content__games">
                    <content-card-component v-for="(card, idx) in cards" :card="card" :key="'card' + idx"></content-card-component>
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
