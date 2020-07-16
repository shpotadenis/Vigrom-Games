<template>
    <header class="header">
        <div class="wrapper">
            <div class="header__wrapper">
                <div class="header__logo">
                    <a href="#!">
                        <img src="@/assets/img/logo.svg" alt="Vigrom" class="header__logo-pic">
                    </a>
                </div>

                <nav class="header__nav">
                    <ul class="header__nav-list">
                        <li class="header__item">
                            <a href="#!" class="header__link">Магазин</a>
                        </li>
                        <li class="header__item">
                            <a href="#!" class="header__link">Новости</a>
                        </li>
                        <li class="header__item">
                            <a href="#!" class="header__link">Библиотека</a>
                        </li>
                        <li class="header__item">
                            <a href="#!" class="header__link">Комьюнити</a>
                        </li>
                        <li class="header__item">
                            <a href="#!" class="header__link">Справка</a>
                        </li>
                    </ul>
                </nav>

                <div class="header__icons">
                    <div class="header__icon">
                        <a href="#!">
                            <img src="@/assets/img/search-icon.png" alt="Search" class="header__icon-pic">
                        </a>
                    </div>
                    <div class="header__icon">
                        <a href="#!">
                            <img src="@/assets/img/cart-icon.png" alt="Cart" class="header__icon-pic">
                        </a>
                    </div>
                    <div class="header__icon">
                        <a href="#!">
                            <img src="@/assets/img/person-icon.png" alt="Person" class="header__icon-pic">
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </header>
</template>

<script>
    export default {
        name: "HeaderComponent"
    }
</script>

<style scoped>
    .wrapper {
        margin: 0 auto;
        max-width: 1124px;
    }

    .header__wrapper {
        display: flex;
        flex-wrap: wrap;
    }

    .header {
        background-color: #848484;
    }

    .header__logo {
        margin: 20px 0;
    }

    .header__nav-list {
        display: flex;
        flex-wrap: wrap;
        flex-direction: row;
        margin-bottom: 31px;
        margin-top: 33px;
    }

    .header__item {
        margin-right: 31px;
    }

    .header__item:last-child {
        margin-right: 0;
    }

    .header__link {
        font-weight: bold;
        font-size: 14px;
        line-height: 16px;
        color: #000;
        text-decoration: none;
    }

    .header__link:hover, .header__link:active, .header__link:focus {
        opacity: .75;
    }

    .header__nav {
        margin-left: 119px;
    }

    .header__icons {
        margin: 28px 0 28px 348px;
        display: flex;
        flex-wrap: wrap;
    }

    .header__icon {
        margin-right: 25px;
    }

    .header__icon:last-child {
        margin-right: 0;
    }

</style>