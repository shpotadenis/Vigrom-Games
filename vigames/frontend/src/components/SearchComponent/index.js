import games from '../../api/modules/games.js'
import news from '../../api/modules/news.js'
import { getImageUrl } from '../../utils.js'

export default {
    name: 'SearchComponent',
    data(){
      return{
          noResults:false,
          searchGames:'',
          searchData: ''
      }
    },
    props:['searchzone'],
    methods:{
        showGames(){
            if (this.searchGames != null && this.searchGames.length != 0) {
                this.noResults = false
                this.search()
            }
        },
        // FIXME: Осторожно! Расположенный ниже код может нанести вред психическому здоровью.
        // FIXME: Нуждается в рефакторинге

        // Производит поиск в связи с поисковой зоной (игры, библиотека, вишлист, новости)
        search() {
            if (this.searchzone == 'games') {
                games.search(this.searchGames).then(response => {
                    this.searchData = response.data
                    if (this.searchData.length == 0) {
                        this.noResults = true
                    } else {
                        this.noResults = false
                        for (let i in this.searchData) {
                            this.searchData[i] = this.convertGameObjToSearch(this.searchData[i])
                        }
                    }
                    console.log(response)
                }).catch(error => {
                    console.log(error)
                })
            } else if (this.searchzone == 'library') {
                games.searchLibrary(this.searchGames).then(response => {
                    this.searchData = response.data
                    if (this.searchData.length == 0) {
                        this.noResults = true
                    } else {
                        this.noResults = false
                        for (let i in this.searchData) {
                            this.searchData[i] = this.convertGameObjToSearch(this.searchData[i])
                        }
                    }
                    console.log(response)
                }).catch(error => {
                    console.log(error)
                })
            } else if (this.searchzone == 'wishlist') {
                games.searchWishlist(this.searchGames).then(response => {
                    this.searchData = response.data
                    if (this.searchData.length == 0) {
                        this.noResults = true
                    } else {
                        this.noResults = false
                        for (let i in this.searchData) {
                            this.searchData[i] = this.convertGameObjToSearch(this.searchData[i])
                        }
                    }
                    console.log(response)
                }).catch(error => {
                    console.log(error)
                })
            } else if(this.searchzone == 'news') {
                news.search(this.searchGames).then(response => {
                    this.searchData = response.data
                    if (this.searchData.length == 0) {
                        this.noResults = true
                    } else {
                        this.noResults = false
                        for (let i in this.searchData) {
                            this.searchData[i] = this.convertNewsObjToSearch(this.searchData[i])
                        }
                    }
                    console.log(response)
                }).catch(error => {
                    console.log(error)
                })
            }
        },

        getImg(idx) {
            return getImageUrl(this.searchData[idx].image)
        },

        convertNewsObjToSearch(obj) {
            return {
                title: obj.title,
                sub_title: obj.author,
                image: obj.img,
                link: {
                    name: 'newsSinglePage',
                    params: {
                        id: obj.id
                    }
                }
            }
        },

        convertGameObjToSearch(obj) {
            return {
                title: obj.title,
                sub_title: obj.price,
                image: obj.img,
                link: {
                    name: 'singlePage',
                    params: {
                        id: obj.id
                    }
                }
            }
        }

    },
    computed: {

    }
}
