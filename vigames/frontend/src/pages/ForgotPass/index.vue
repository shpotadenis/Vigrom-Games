<template>
    <div class="ForgotPass container">
        <div class="log row justify-content-center">
            <div  class="login-form pic-form col-5">
                <img class="login-pic" src="@/assets/img/enter_img_girl.svg">
            </div>
            <div class="login-form col-4" v-if="nonEye == true">
                <p class="head_login">Восстановление пароля</p>
                <div class="container">
                    <form class="data row justify-content-center">
                        <div class="">
                            <div class="form-group container">
                                <label for="mail">E-mail</label><br />
                                <input type="text"
                                       class="form-control"
                                       id="mail"
                                       placeholder="Введите e-mail"/>
                                <div class="errors__mail errors"></div>
                            </div>
                            <div class="title"><span id="message">На ваш e-mail будет отправлено письмо со ссылкой на сброс пароля.</span></div>
                        </div>
                    </form>
                    <div class="btn_and_link">
                        <div class="row justify-content-center">
                            <!--                            Перенаправление в личный кабинет через программную навигацию в методе checkForm-->
                            <button class="next-btn" @click="checkForm">Отправить</button>
                        </div>
                        <router-link :to="{name: 'signInPage'}" class="back-link row justify-content-center">
                            Вернуться назад
                        </router-link>
                    </div>
                </div>
            </div>
            <div class="login-form col-4" v-if="nonEye == false">
                <p class="head_login">Восстановление пароля</p>
                <div class="container">
                    <form class="data row justify-content-center">
                        <div class="">
                            <div class="form-group container">
                                <label for="mail">E-mail</label><br />
                                <input type="text"
                                       class="form-control"
                                       id="mail"
                                       placeholder="Введите e-mail"/>
                                <div class="errors__mail errors"></div>
                            </div>
                            <div class="title"><span id="message">На ваш e-mail будет отправлено письмо со ссылкой на сброс пароля.</span></div>
                        </div>
                    </form>
                    <div class="btn_and_link">
                        <div class="row justify-content-center">
                            <!--                            Перенаправление в личный кабинет через программную навигацию в методе checkForm-->
                            <button class="next-btn" @click="checkForm">Отправить</button>
                        </div>
                        <router-link :to="{name: 'loginPage'}" class="back-link row justify-content-center">
                            Создать аккаунт
                        </router-link>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script src="./index.js"></script>

<style scoped src="./index.css"></style>