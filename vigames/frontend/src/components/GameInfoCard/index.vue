<template>
  <div class="wrapper">
    <div class="container">
      <div class="all-item">
        <div class="game-scrin">
          <img v-bind:src="require('@/assets/img/' + Game_Info_Card.image)" class="game-image">
        </div>
        <div class="content">
          <div class="game-name">
            {{Game_Info_Card.name}}
          </div>
          <div class="game-info1">
            {{Game_Info_Card.undername1}}
          </div>
          <div class="game-info2">
            {{Game_Info_Card.undername2}}
          </div>
          <div class="details">
            <p>Подробнее</p>
            <img src="@/assets/img/VectorPig.svg" class="arrow-pig">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>
