<template>
    <footer class="footer">
        <div class="wrapper">
            <Support v-if="isBtnClick" @close="isBtnClick = false"> </Support>
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
                            <a @click="isBtnClick = true" class="list__link">Поддержка</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </footer>
</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>
