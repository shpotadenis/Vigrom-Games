<template>
    <div class="signInPage container">
        <div class="log row justify-content-center">
            <div  class="login-form pic-form col-5">
                <img class="login-pic" src="@/assets/img/enter_img_girl.svg">
            </div>
            <div class="login-form col-4">
                <p class="head_login">ВХОД</p>
                <div class="container">
                    <form class="data row justify-content-center">
                        <div class="">
                            <div class="form-group container">
                                <label for="login">Логин</label><br />
                                <input type="text"
                                       v-model="name"
                                       class="form-control"
                                       id="login"
                                       placeholder="Введите логин..."/>
                                <div class="errors__name errors" v-if="error_name.length">
                                    {{error_name[0]}}
                                </div>
                            </div>
                            <div class="form-group container">
                                <label for="password">Пароль</label><br />
                                <input :type="type"
                                       v-model="pass"
                                       class="form-control"
                                       id="password"
                                       placeholder="Введите пароль..."/>
                                <div class="errors__pass errors" v-if="error_pass.length">
                                    {{error_pass[0]}}
                                </div>
                                <div class="row justify-content-end" @click="hide">
                                    <img src="@/assets/img/eye.png"   class="passEye password-control" v-show="!nonEye"/>
                                    <img src="@/assets/img/eye-off.svg"  class="passEye password-control" v-show="nonEye">
                                    <!--Глаз может поехать-->
                                </div>
                                <router-link :to="{name: 'forgotPass'}" class="forgot-pass-link row justify-content-center">
                                    Забыли пароль?
                                </router-link>
                            </div>
                            <span>{{errorMessage}}</span>
                        </div>
                    </form>
                    <div class="btn_and_link">
                        <div class="row justify-content-center">
<!--                            Перенаправление в личный кабинет через программную навигацию в методе checkForm-->
                                <button class="next-btn" @click="checkForm">Войти</button>
                        </div>
                        <router-link :to="{name: 'loginPage'}" class="signin-link row justify-content-center">
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