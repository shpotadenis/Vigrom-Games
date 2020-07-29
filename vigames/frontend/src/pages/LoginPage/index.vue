<template>
    <div class="loginPage container">
        <div >
        <div class="log row justify-content-center">
            <img src="@/assets/img/login-pic.png" class="login-pic col-4">
            <div class="login-form col-4">
                <p class="head_login">РЕГИСТРАЦИЯ</p>
                <form class="data">
                    <div class="form-group">
                        <label for="name">E-mail</label><br />
                        <input type="text" class="form-control" id="name" />
                    </div>
                    <div class="form-group">
                        <label for="login">Логин</label><br />
                        <input type="text" class="form-control" id="login" />
                    </div>
                    <div class="form-group">
                        <label for="password">Пароль</label><br />
                        <input type="password" class="form-control" id="password" />
                    </div>
                    <div class="form-group">
                        <label for="confirmPass">Повтор пароля</label><br />
                        <input type="password" class="form-control" id="confirmPass" />
                    </div>
                </form>
                <div class="container">
                    <div class="justify-content-center"></div>
                    <button class="next-btn col-4">Далее</button>
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