<template>
    <div class="loginPage container">
        <div >
            <div class="log row justify-content-center">
                <div  class="login-form pic-form col-5">
                    <img class="login-pic" src="@/assets/img/development-1.svg">
                </div>
                <div class="login-form col-4">
                    <p class="head_login">РЕГИСТРАЦИЯ</p>
                    <div class="container">
                        <form class="data">
                            <div class="form-group container">
                                <input type="radio" class="form-control" name="role" id="gamer"/>
                                <label class="words" for="gamer">Я игрок</label>
                            </div>
                            <div class="form-group container">
                                <input type="radio" class="form-control" name="role" id="developer"/>
                                <label class="words" for="developer"> Я разработчик</label>
                            </div>

                        </form>
                        <div class="btn_and_link">
                            <div class="row justify-content-center">
                                <button class="next-btn ">Регистрация</button>
                            </div>
                            <router-link :to="{name: 'loginPage'}" class="signin-link row justify-content-center">
                                Вернуться на предыдущую страницу
                            </router-link>
                        </div>
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