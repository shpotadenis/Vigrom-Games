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
                      
                        <canvas ref="canvas" class="Chart"></canvas>
                  </div>
                  <div>
                    <div class="watch_statistics">
                        <p>Dager crew</p>
                    </div>
                    <div class="games-rating">
                        <p>Рейтинг игр</p>

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
