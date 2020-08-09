<template>
  <div class="popup-wrapper">
    <div class="checkout container">
        <goDownload v-if="isBtnClick2" :gameData="this.getGameData" @close="isBtnClick2 = false">  </goDownload>
        <div class="checkout_header">
            <div class="head-block">
                <div class="head-name">Оформление покупки</div>
                <div class="closer">
                    <button @click=" $emit('close')" class="close-icon">
                        <img src="@/assets/img/close-outline.svg" alt="Close">
                    </button>
                </div>
            </div>
        </div>
        <hr>
    <!-- TODO: Добавить функциональность
        <div class="checkout_content">
            <div class="text-1">
                После оплаты вы получите письмо с ключом для скачивания игры в Dowload Manager на указанный вами email
            </div>

            <div class="email-block">
                <input type="text" id="mail" :placeholder="getGameData.email"/>
            </div>
        </div>
    !-->
        <div class="donate">
            <div class="text-2">Поддержать разработчика</div>
            <div class="btns_donate">
              <button @click='isClick1' class="btn-donate" :class='{"yellow": isBtnDonate1Click}' id="btn-1"><img src="@/assets/img/plus-outline-white.svg" alt="Plus">0 <img src="@/assets/img/ruble-white.svg" alt="Ruble"></button>
              <button @click='isClick2' class="btn-donate" :class='{"yellow": isBtnDonate2Click}' id="btn-2"><img src="@/assets/img/plus-outline-white.svg" alt="Plus">100 <img src="@/assets/img/ruble-white.svg" alt="Ruble"></button>
              <button @click='isClick3' class="btn-donate" :class='{"yellow": isBtnDonate3Click}' id="btn-3"><img src="@/assets/img/plus-outline-white.svg" alt="Plus">200 <img src="@/assets/img/ruble-white.svg" alt="Ruble"></button>
            </div>
        </div>
        <hr>

        <div class="info">
            <div class="info-game">
                <div class="game-name">{{getGameData.name}}</div>
                <div class="game-price">{{getGameData.price}} <img src="@/assets/img/ruble-gray.svg" alt="Ruble"></div>
            </div>
            <div class="info-donate">
                <div>Бонус Разработчику</div>
                <div class="donate-sum"> {{ammount_donate}} <img src="@/assets/img/ruble-gray.svg" alt="Ruble"></div>
            </div>
        </div>
        <hr>

        <div class="footer">
            <div class="price">
                <div class="price-text">Всего:</div>
                <div class="price-sum">{{getGameData.price+ammount_donate}}<img src="@/assets/img/ruble-white.svg" alt="Ruble"></div>
            </div>
            <div class="btns-footer">
            <div><button @click="buyGame" class="payment">Перейти к оплате</button></div>
            <!-- <div><button @click="isBtnClick2 = true" class="payment">Всплывашка после покупки</button></div>
            !-->
          </div>
        </div>
    </div>
  </div>

</template>

<script src="./checkout-js.js" type="application/javascript">
</script>

<style scoped src="./checkout-css.css" rel="stylesheet">
</style>
