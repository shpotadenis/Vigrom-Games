<template>
    <div class="checkout">
        <div class="checkout_header">
            <div class="head-block">
                <div class="head-name">Оформление покупки</div>
                <div class="closer"><button class="close-icon"><img src="@/assets/img/close-outline.svg" alt="Close"></button></div>
            </div>
        </div>
        <hr>

        <div class="checkout_content">
            <div class="text-1">
                После оплаты вы получите письмо с ключом для скачивания игры в Dowload Manager на указанный вами email
            </div>

            <div class="email-block">
                <input type="text" id="mail" placeholder="        useremail@gmail.com"/>
            </div>
        </div>

        <div class="donate">
            <div class="text-2">Поддержать разработчика</div>
            <div class="btns_donate">
                <button class="btn-donate" id="btn-1">+ 0₽</button>
                <button class="btn-donate" id="btn-2">+ 100₽</button>
                <button class="btn-donate" id="btn-3">+ 200₽</button>
            </div>
        </div>
        <hr>

        <div class="info">
            <div class="info-game">
                <div class="game-name">Название игры***</div>
                <div class="game-price">100₽***</div>
            </div>
            <div class="info-donate">
                <div>Бонус Разработчику</div>
                <div class="donate-sum">150₽***</div>
            </div>
        </div>
        <hr>

        <div class="footer">
            <div class="price">
                <div class="price-text">Всего:</div>
                <div class="price-sum">250₽***</div>
            </div>
            <button class="payment">Перейти к оплате</button>
        </div>
    </div>

</template>

<script src="./checkout-js.js" type="application/javascript">
</script>

<style scoped src="./checkout-css.css" rel="stylesheet">
</style>
