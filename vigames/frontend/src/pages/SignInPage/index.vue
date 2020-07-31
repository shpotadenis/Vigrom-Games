<template>
    <div class="signInPage container">
        <div class="log row justify-content-center">
            <div  class="login-form pic-form col-5">
                <img class="login-pic" src="@/assets/img/undraw_launch_day.svg">
            </div>
            <div class="login-form col-4">
                <p class="head_login">ВХОД</p>
                <div class="container">
                    <form class="data row justify-content-center">
                        <div class="">
                            <div class="form-group container">
                                <label for="login">Логин</label><br />
                                <input type="text" class="form-control" id="login" placeholder="Введите логин..."/>
                            </div>
                            <div class="form-group container">
                                <label for="password">Пароль</label><br />
                                <input :type="type" class="form-control" id="password" placeholder="Введите пароль..."/>
                                <div class="row justify-content-end" @click="hide">

                                    <img src="@/assets/img/eye.png"   class="passEye password-control" v-show="!nonEye"/>
                                    <img src="@/assets/img/eye-off.svg"  class="passEye password-control" v-show="nonEye">
                                    <!--Глаз может поехать-->
                                </div>
                            </div>
                        </div>
                    </form>
                    <div class="btn_and_link">
                        <div class="row justify-content-center">
                            <div class="">
                                <button class="next-btn ">Войти</button>
                            </div>
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