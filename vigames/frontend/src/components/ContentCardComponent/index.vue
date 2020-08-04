<template>
    <div class="card">
        <div class="card__image">
            <img src="@/assets/img/card-pic.png" alt="" class="card__image-pic">
        </div>
        <div class="card-body">
            <div>
                <div class="card__title">
                    <h3 class="card__title-text">
                        {{card.title}}
                    </h3>
                </div>
                <div class="card__subtitle">
                    <p class="card__subtitle-text">
                        {{card.subtitle}}
                    </p>
                </div>
            </div>
            <div class="card-body__price">
                {{card.price}}
                <img src="@/assets/img/ruble-white.svg" alt="" class="card-body__price-pic">
            </div>
        </div>
    </div>
</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>