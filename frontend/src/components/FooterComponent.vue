<template>
    <footer class="footer">
        <div class="wrapper">
            <div class="footer__wrapper">
                <div class="footer__logo">
                    <a href="#!">
                        <img src="@/assets/img/footer_logo.svg" alt="" class="footer__logo-pic">
                    </a>
                </div>
                <div class="footer__copyright">
                    <span class="copyright">
                        Все права защищены.
                    </span>
                </div>
                <div class="footer__links">
                    <ul class="footer__links-list">
                        <li class="list__item">
                            <a href="#!" class="list__link">Поддержка</a>
                        </li>
                        <li class="list__item">
                            <a href="#!" class="list__link">Дистрибуция</a>
                        </li>
                        <li class="list__item">
                            <a href="#!" class="list__link">Правовая информация</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </footer>
</template>

<script>
    export default {
        name: "FooterComponent"
    }
</script>

<style scoped>
    .footer {
        background-color: #848484;
    }

    .wrapper {
        margin: 0 auto;
        max-width: 1124px;
    }

    .footer__logo {
        margin: 30px 0;
    }

    .footer__wrapper {
        display: flex;
        flex-wrap: wrap;
    }

    .footer__copyright {
        margin: 30px 0 30px 30px;
    }

    .copyright {
        font-size: 14px;
        line-height: 16px;
        color: #E1E1E1;
    }

    .footer__links {
        margin: 30px 0 28px 373px;
    }

    .footer__links-list {
        display: flex;
        flex-wrap: wrap;
    }

    .list__item {
        margin-right: 34px;
    }

    .list__item:last-child {
        margin-right: 0;
    }

    .list__link {
        font-size: 14px;
        line-height: 16px;
        color: #FFFFFF;
        text-decoration: none;
    }
</style>