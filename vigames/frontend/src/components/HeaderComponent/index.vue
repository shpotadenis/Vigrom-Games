<template>
    <header class="header">
        <div class="wrapper">
          <Support v-if="isBtnClick" @close="isBtnClick = false"> </Support>
            <div class="header__wrapper">
                <div class="header__logo">
                    <router-link :to="{name: 'homePage'}">
                        <img src="@/assets/img/logo.svg" alt="Vigrom" class="header__logo-pic">
                    </router-link>
                </div>

                <nav class="header__nav">
                    <ul class="header__nav-list">
                        <li class="header__item">
                            <router-link :to="{name: 'singlePage'}" class="header__link">
                                Магазин
                            </router-link>
                        </li>
                        <li class="header__item">
                            <router-link :to="{name: 'newsPage'}" class="header__link">
                                Новости
                            </router-link>
                        </li>
                        <li class="header__item">
                            <router-link :to="{name: 'libraryPage'}" class="header__link">
                                Библиотека
                            </router-link>
                        </li>
                        <li class="header__item">
                            <router-link :to="{name: 'featuredPage'}" class="header__link">
                            Избранное
                            </router-link>
                        </li>
                        <li class="header__item">
                            <a @click="isBtnClick = true" class="header__link">Поддержка</a>
                        </li>
                    </ul>
                </nav>

                <div class="header__icons">
                    <div class="header__icon">
                        <router-link :to="{name: 'signInPage'}">
                            <div class="header__icon-link">
                                <img src="@/assets/img/person-icon.png" alt="Person" class="header__icon-pic">
                            </div>
                        </router-link>
                    </div>
                </div>
            </div>
        </div>
    </header>
</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>
