<template>
    <div class="ForgotPass container">
        <!-- Pop-up PasswordReset должен всплывать после перехода с e-mail, если show_reset_pass == true во vue, для
        этого нужна функция во vue, сейчас он всплывает автоматически при нажатии на кнопку отправить -->
        <PasswordReset
                v-if="show_reset_pass"
                @closePopup="closePopup"
                @SaveNewPass="SaveNewPass"
        >
        </PasswordReset>
        <PasswordChanged
                v-if="isPassChangePopupVisible"
                @close="close"
        >
        </PasswordChanged>
        <div class="log row justify-content-center">
            <div  class="login-form pic-form col-5">
                <img class="login-pic" src="@/assets/img/enter_img_girl.svg">
            </div>
            <div class="login-form col-4" v-if="first_btn == true">
                <p class="head_login">Восстановление пароля</p>
                <div class="container">
                    <form class="data row justify-content-center">
                        <div class="">
                            <div class="form-group container">
                                <div>
                                    <label for="mail">E-mail</label>
                                    <error-message :error="error_mail[0]"
                                                   v-show="error_mail.length>0">
                                    </error-message>
                                </div>
                                <input type="text"
                                       class="form-control"
                                       id="mail"
                                       placeholder="Введите e-mail"
                                       v-model="email"
                                >
                            </div>
                            <div class="title"><span id="message">На ваш e-mail будет отправлено письмо со ссылкой на сброс пароля.</span>
                            </div>
                        </div>
                    </form>
                    <div class="btn_and_link">
                        <div class="row justify-content-center" @click="hide">
                            <!--                            Перенаправление в личный кабинет через программную навигацию в методе checkForm-->
                            <button class="next-btn" @click="checkform">Отправить</button>
                        </div>
                        <router-link :to="{name: 'signInPage'}" class="back-link row justify-content-center">
                            Вернуться назад
                        </router-link>
                    </div>
                </div>
            </div>
            <div class="login-form col-4" v-if="first_btn == false">
                <p class="head_login">Восстановление пароля</p>
                <div class="container">
                        <div class="title_email">
                            <span id="message_email">Запрос принят. Для сброса пароля перейдите по ссылке из письма, отправленного на ваш e-mail.</span>
                        </div>
                    <div class="btn_and_link">
                        <div class="row justify-content-center">
                            <router-link :to="{name: 'signInPage'}">
                                <button class="back-btn">Вернуться</button>
                            </router-link>
                        </div>
                        <a @click="support = true" class="back-link row justify-content-center">
                            Мне не пришло письмо
                        </a>
                        <support v-if="support" @close="support = false"></support>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script src="./index.js"></script>

<style scoped src="./index.css"></style>