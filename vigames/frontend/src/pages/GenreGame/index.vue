<template>
    <div>
        <div class="wrappen">
            <div class="AdventuresGames">
                <internal-menu/>
                <div class="FilterGames">
                    <search-component searchzone="games" />
                </div>
            </div>
            <div class="AdventuresGamesTitle">
                <p class="Title">{{getGenreName()}}</p>
            </div>

            <div class="AdventuresGamesComponents">

                <game-card
                        class="ItemCard"
                        v-for="discount in array"
                        :key="discount.id"
                        :Game="discount"
                />
            </div>

            <banner-component day="Сегодня"
                              header="НОВЫЕ ИНДИ ИГРЫ УЖЕ НА ГЛАВНОЙ"
                              description="Унитарное государство, однако, доказывает системный политический процесс в современной России"
                              btn_caption="Подробнее"
                              :btn_route="{ name: 'homePage' }">
            </banner-component>
            <div class="AdventuresGamesComponents">
                <game-card
                        class="ItemCard"
                        v-for="discount in array2"
                        :key="discount.id"
                        :Game="discount"
                />
            </div>
        </div>
        <footer-component></footer-component>
    </div>
</template>


<script src="./index.js" type="application/javascript">
</script>

<style lang="scss" scoped>
    @import "@/assets/style/AdventuresGame.scss";
</style>
