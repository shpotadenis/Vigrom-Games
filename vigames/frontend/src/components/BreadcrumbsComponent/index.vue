<template>
    <div class="wrapper">
        <ul class="breadcrumbs">
            <li class="breadcrumb" v-for="(item, idx) in items" :key="idx">
                <router-link v-if="item.to !== undefined" :to="item.to" class="breadcrumb__link">
                    {{item.title}}
                    <img v-if="idx != items.length - 1" src="@/assets/img/chevron-right-icon.svg" alt=">" class="breadcrumb__right">
                </router-link>
                <span v-else class="breadcrumb__link">
                    {{item.title}}
                    <img v-if="idx != items.length - 1" src="@/assets/img/chevron-right-icon.svg" alt=">" class="breadcrumb__right">
                </span>
            </li>
        </ul>
    </div>
</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>