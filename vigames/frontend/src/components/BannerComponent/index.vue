<template>
    <div class="banner">
        <div class="banner__desc">
            <h3 class="desc__header">
                {{day}}
            </h3>
            <div class="desc__content">
                <h2 class="content__header">
                    {{header}}
                </h2>
                <p class="content__text">
                    {{description}}
                </p>
                <div class="content__btn">
                    <span>
                        {{btn-caption}}
                    </span>
                    <span>
                        <img src="@/assets/img/arrow-right.png" alt="" class="btn__arrow">
                    </span>
                </div>
            </div>
        </div>
        <div class="banner__image">
            <img src="@/assets/img/library_banner.png" alt="" class="banner__image-pic">
        </div>
    </div>
</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>