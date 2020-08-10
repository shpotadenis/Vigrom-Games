<template>
  <div class="popup_wrapper">
    <div class="container">
      <div class="Header">
        <div class="head-name">Игра загружена!</div>
        <div class="closer">
            <button @click=" $emit('close')" class="close-icon">
                <img src="@/assets/img/close-outline.svg" alt="Close">
            </button>
        </div>
      </div>
      <hr>

      <div class="Content">
        Спасибо, что вы с нами! Теперь вы можете наблюдать за статистикой
        по игре в личном кабинете.
      </div>
      <div class="Footer">
        <div><button @click=" $emit('close')" class="Btn">Понятно</button></div>
      </div>
    </div>
  </div>

</template>



<script src="./index.js" type="application/javascript">
</script>

<style scoped src="./index.css" rel="stylesheet">
</style>
