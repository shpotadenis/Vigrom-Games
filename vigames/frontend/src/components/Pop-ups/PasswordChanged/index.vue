<template>
    <div class="popup-wrapper">
        <div class="container">
            <div class="goDownload_Header">
                <div class="head-name">Готово!</div>
                <div class="closer">
                    <button
                            @click=" $emit('close')"
                            class="close-icon"
                    >
                        <img src="@/assets/img/close-outline.svg" alt="Close">
                    </button>
                </div>
            </div>
            <hr>
            <div class="goDownload_Content">
                Ваш пароль изменён
            </div>
            <div class="goDownload_Footer">
                <button
                        class="download"
                        @click=" $emit('close') "
                >
                    Хорошо
                </button>
            </div>
        </div>
    </div>
</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>