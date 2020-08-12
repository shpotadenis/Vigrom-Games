<template>
    <div>
            <div class="wrapper">
                <div class="header">
                    <p class="title">Статистика</p>
                    <img src="@/assets/img/line.svg" alt="" class="img-1">
                </div>
                <div class="body">
                  <div class="Download_statistics">
                      <p class="StatName">Статистика скачиваний</p>
                      <div class="AllButton">
                        <button class="Arrow1"><img src="@/assets/img/chevron-right-icon.svg" class="Arrow1Image"></button>
                        <button class="button">Name1</button>
                        <button class="button">Name2</button>
                        <button class="button">Name3</button>
                        <button class="Arrow2"><img src="@/assets/img/chevron-right-icon.svg" class="Arrow1Image"></button>
                      </div>
                      <div class="Chart">
                        <line-chart :labels="labels" :datasets="datasets" class="Line"/>
                        <div class="AllDataButton">
                          <button class="Data">Неделя</button>
                          <button class="Data">Месяц</button>
                          <button class="Data">Год</button>
                        </div>
                      </div>

                  </div>
                  <div>
                    <div class="watch_statistics">
                        <p class="StatName1">Dager crew</p>
                        <div class="Stata">
                          <p>Просмотров за последних 7 дней</p>
                          <P>5638</p>
                        </div>
                        <div class="Stata">
                          <p>Всего просмотров</p>
                          <P>5638</p>
                        </div>
                        <div class="Stata">
                          <p>Добавления в избранное</p>
                          <P>5638</p>
                        </div>
                    </div>
                    <div class="games-rating">
                        <p class="StatName1">Рейтинг игр</p>
                        
                    </div>
                  </div>
                </div>
            </div>
        <footer-component></footer-component>
    </div>
</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>
