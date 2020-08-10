<template>
    <div class="review__rating">
        <img :src="require('@/assets/img/star' + getFilledStatus(i) + '.svg')" alt="" class="review__star" @click="ratingClick(i)" v-for="i in 5" :key="'k' + i">
    </div>
</template>

<script src="./index.js">
</script>

<style scoped src="./index.css">
</style>