<template>
    <div v-if="!loading">
        <div class="wrapper">
            <div class="head">
                <div class="head__header">
                    <h1 class="header__text">
                        Избранное
                    </h1>
                </div>
                <div class="head__search">
                    <search-component searchzone="wishlist"></search-component>
                </div>
            </div>


            <div class="main-content">
                <div class="main-content__header">
                    <h1 class="header__text">
                        Избранные игры
                    </h1>
                </div>
                <div class="main-content__games" v-if="getFeaturedCards.length > 0">
                    <game-card
                            v-for="item in getFeaturedCards"
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
