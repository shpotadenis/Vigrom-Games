<template>
    <div class="errorPage container">
        <div class="row justify-content-center">
            <img src="@/assets/img/working_in_a_laboratory.svg" class="image">
        </div>
        <div class="error row justify-content-center">404</div>
        <div class=" message row justify-content-center">Страница не найдена</div>
        <div class="row justify-content-center">
        <router-link :to="{name: 'homePage'}" class="homeBtn">
            <button>Вернуться на главную</button>
        </router-link>
        </div>
    </div>
</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>