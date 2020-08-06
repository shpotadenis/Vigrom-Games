<template>
    <div v-if="!loading">
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

            <banner-component day="Сегодня"
                              header="Новые инди игры уже на главной"
                              description="Унитарное государство, однако, доказывает системный политический процесс в современной России"
                              btn_caption="Подробнее"
                              :btn_route="{ name: 'homePage' }">
            </banner-component>

            <div class="main-content">
                <div class="main-content__header">
                    <h1 class="header__text">
                        Ваши игры
                    </h1>
                </div>
                <div class="main-content__games" v-if="getLibraryCards.length > 0">
                    <game-card
                            v-for="item in getLibraryCards"
                            :key="item.id"
                            :Game="item"
                            class="game_card"
                    />
                </div>
                <div class="main-content__games" v-else>
                    Список игр пуст.
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
