<template>
    <div class="errorPage container">
        <div class="error row justify-content-center">403</div>
        <div class=" message row justify-content-center">Ой, доступ к странице ограничен</div>
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