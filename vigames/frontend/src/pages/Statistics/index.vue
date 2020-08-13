<template>
    <div>
            <div class="wrapper" v-if="!noGames">
                <div class="header">
                    <p class="title">Статистика</p>
                    <img src="@/assets/img/line.svg" alt="" class="img-1">
                </div>
                <div class="body">
                  <div class="Download_statistics">
                      <p class="StatName">Статистика покупок</p>
                      <div class="AllButton">
                        <button class="Arrow1"><img src="@/assets/img/chevron-right-icon.svg" class="Arrow1Image"></button>
                          <button v-for="(game, idx) in games"
                                  :key="game.id"
                                  :class="selectedGameIdx == idx ? 'button button-active' : 'button'"
                                  @click="selectGame(idx)"
                          >
                              {{game.title}}
                          </button>
                        <button class="Arrow2"><img src="@/assets/img/chevron-right-icon.svg" class="Arrow1Image"></button>
                      </div>

                        <canvas  ref="canvas" class="Line"></canvas>


                  </div>
                  <div>
                    <div class="watch_statistics" v-if="selectedGameIdx != -1">
                        <p class="StatName1">{{games[selectedGameIdx].title}}</p>
                        <div class="Stata">
                          <p>Просмотров за последних 7 дней</p>
                          <P>{{detailedStatistics.views_week}}</p>
                        </div>
                        <div class="Stata">
                          <p>Всего просмотров</p>
                          <P>{{detailedStatistics.views_all}}</p>
                        </div>
                        <div class="Stata">
                          <p>Добавления в избранное</p>
                          <P>{{detailedStatistics.wishlist}}</p>
                        </div>
                    </div>
                    <div class="games-rating" v-if="!loading">
                        <p class="StatName1">Рейтинг игр</p>
                        <bar-chart :labels="getLabelsForRating" :datasets="getRatings" />
                    </div>
                  </div>
                </div>
            </div>
        <div class="wrapper" v-else>
            <div class="header">
                <p class="title">Статистика</p>
                <img src="@/assets/img/line.svg" alt="" class="img-1">
            </div>
            Нет данных для отображения
        </div>
        <footer-component></footer-component>
    </div>
</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>
