<template>
    <div class="loginPage container">
        <div >
        <div class="log row justify-content-center">
            <div  class="login-form pic-form col-5">
                <img class="login-pic" src="@/assets/img/space-discovery-1.svg">
            </div>
            <div class="login-form col-4">
                <p class="head_login">РЕГИСТРАЦИЯ</p>
                <div class="container">
                <form class="data row justify-content-center" method="post">
                    <div class="">
                    <div class="form-group container">
                        <div>
                            <label for="mail">E-mail</label>
                            <error-message :error="error_mail[0]"
                                           v-show="error_mail.length>0">
                            </error-message>
                        </div>
                        <input type="text"
                               v-model="email"
                               class="form-control"
                               id="mail"
                               placeholder="Введите эл. почту..."/>

                    </div>

                    <div class="form-group container">
                        <div>
                            <label for="login">Логин</label>
                            <error-message :error="error_name[0]"
                                           v-show="error_name.length>0">
                            </error-message>
                        </div>
                        <input type="text"
                               v-model="name"
                               class="form-control"
                               id="login"
                               placeholder="Введите логин..."/>
                    </div>


                    <div class="form-group container">
                        <div>
                            <label for="password">Пароль</label>
                            <error-message :error="error_pass[0]"
                                           v-show="error_pass.length>0">
                            </error-message>
                        </div>
                        <input :type="type"
                               v-model="pass"
                               class="form-control"
                               id="password"
                               placeholder="Введите пароль..."/>

                        <div class="row justify-content-end eyeClick" @click="hide">
                            <img src="@/assets/img/eye.png"   class="passEye password-control" v-show="!nonEye"/>
                            <img src="@/assets/img/eye-off.svg"  class="passEye password-control" v-show="nonEye">
                            <!--Глаз может поехать-->
                        </div>

                    </div>
                    <div class="form-group container">
                        <div>
                            <label for="confirmPass">Повтор пароля</label>
                            <error-message :error="error_confirm[0]"
                                           v-show="error_confirm.length>0">
                            </error-message>
                        </div>
                        <input :type="typeconf"
                               v-model="confirmPass"
                               class="form-control"
                               id="confirmPass"
                               placeholder="Повторите пароль..."/>

                        <div class="row justify-content-end eyeClick" @click="hideconf">
                            <img src="@/assets/img/eye.png" class="confirmEye password-control" v-show="!nonEyeconf"/>
                            <img src="@/assets/img/eye-off.svg" class="confirmEye password-control" v-show="nonEyeconf">
                            <!--Глаз может поехать-->
                        </div>
                    </div>
                    </div>

                </form>
                    <div class="row justify-content-center">
                        <button class="next-btn" @click="checkForm">Далее</button>
                    </div>
                    <router-link :to="{name: 'signInPage'}" class="signin-link row justify-content-center">
                        Уже есть аккаунт?
                    </router-link>

                </div>
            </div>
        </div>
        </div>
    </div>
</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>