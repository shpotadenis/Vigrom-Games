import NewsPageStart from "./Allcomponents/NewsPageStart/NewsPageStart.vue"
import SelectedArticles from "./Allcomponents/NewsPageStart/SelectedArticles.vue"
import NewsFeed from "./Allcomponents/NewsPageStart/NewsFeed.vue"
import FooterComponent from "../../components/FooterComponent/index.vue"
import news from '../../api/modules/news.js'


export default{
    name:"NewsPage",
    components:{
        NewsPageStart,
        SelectedArticles,
        NewsFeed,
        FooterComponent
    },
    props:{},
    data(){
        return{
            loading: false,
            Selected:[
                {
                    date:"Сегодня",
                    name:"Новое оборудование на серверах Vigrom",
                    id:"1"
                },
                {
                    date:"Сегодня",
                    name:"Новое оборудование на серверах Vigrom",
                    id:"2"
                },
                {
                    date:"Сегодня",
                    name:"Новое оборудование на серверах Vigrom",
                    id:"3"
                },
                {
                    date:"Сегодня",
                    name:"Новое оборудование на серверах Vigrom",
                    id:"4"
                },
            ],
            Feeds: []
        }
    },

    beforeMount() {
        this.fetchData()
    },

    methods: {
        fetchData() {
            this.loading = true
            news.getListOfNews().then(response => {
                this.Feeds = response.data
                console.log(response)
            }).catch(error => {
                console.log(error)
            })
        }
    }
}