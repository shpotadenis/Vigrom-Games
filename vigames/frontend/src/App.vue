<template>
  <div id="app">
    <header-component></header-component>
    <router-view></router-view>
  </div>
</template>

<script>
  import HeaderComponent from "./components/HeaderComponent/index.vue";
  export default {
    name: 'App',
    components: {
      HeaderComponent
    }
  }
</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700;800&display=swap');
  #app {
    font-family: Roboto;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #ccc;
    font-style: normal;
    font-size: 16px;
    font-weight: normal;
    padding: 10px;
  }
  body {
    margin: 0;
    background: #212130;
  }
  /* fonts */
  /* roboto-regular - latin_cyrillic */
  @font-face {
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    src: local('Roboto'), local('Roboto-Regular'),
    url('/fonts/roboto-v20-latin_cyrillic-regular.woff2') format('woff2'), /* Chrome 26+, Opera 23+, Firefox 39+ */
    url('/fonts/roboto-v20-latin_cyrillic-regular.woff') format('woff'); /* Chrome 6+, Firefox 3.6+, IE 9+, Safari 5.1+ */
  }
  /* roboto-700 - latin_cyrillic */
  @font-face {
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 700;
    src: local('Roboto Bold'), local('Roboto-Bold'),
    url('/fonts/roboto-v20-latin_cyrillic-700.woff2') format('woff2'), /* Chrome 26+, Opera 23+, Firefox 39+ */
    url('/fonts/roboto-v20-latin_cyrillic-700.woff') format('woff'); /* Chrome 6+, Firefox 3.6+, IE 9+, Safari 5.1+ */
  }
  /* fonts end */
</style>