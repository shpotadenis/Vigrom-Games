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
            Selected: [],
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
                this.Feeds = response.data.news
                this.Selected = response.data.news_fav
                console.log(response)
                this.loading = false
            }).catch(error => {
                console.log(error)
            })
        }
    }
}