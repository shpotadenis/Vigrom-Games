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
                <form class="data row justify-content-center">
                    <div class="">
                    <div class="form-group container">
                        <label for="mail">E-mail</label><br />
                        <input type="text" class="form-control" id="mail" placeholder="Введите эл. почту..."/>
                    </div>
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
                    <div class="form-group container">
                        <label for="confirmPass">Повтор пароля</label><br />
                        <input :type="typeconf" class="form-control" id="confirmPass" placeholder="Повторите пароль..."/>
                        <div class="row justify-content-end" @click="hideconf">

                            <img src="@/assets/img/eye.png" class="confirmEye password-control" v-show="!nonEyeconf"/>
                            <img src="@/assets/img/eye-off.svg" class="confirmEye password-control" v-show="nonEyeconf">
                            <!--Глаз может поехать-->
                        </div>
                    </div>
                    </div>

                </form>
                    <div class="row justify-content-center">
                        <button class="next-btn ">Далее</button>
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