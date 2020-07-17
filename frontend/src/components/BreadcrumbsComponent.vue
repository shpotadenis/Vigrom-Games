<template>
    <div class="wrapper">
        <ul class="breadcrumbs">
            <li class="breadcrumb">
                <a href="#!" class="breadcrumb__link">
                    Главная
                    <img src="@/assets/img/right.svg" alt=">" class="breadcrumb__right">
                </a>
                <a href="#!" class="breadcrumb__link">
                    Магазин
                    <img src="@/assets/img/right.svg" alt=">" class="breadcrumb__right">
                </a>
                <a class="breadcrumb__link">
                    Название игры
                </a>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "BreadcrumbsComponent"
    }
</script>

<style scoped>
    .wrapper {
        margin: 0 auto;
        max-width: 1140px;
    }

    .breadcrumbs {
        display: inline-block;
    }

    .breadcrumb__link {
        font-weight: normal;
        font-size: 14px;
        line-height: 16px;
        color: #000000;
        opacity: 0.8;
        text-decoration: none;
    }

    .breadcrumb__right {
        margin: 0 10px;
    }


</style>