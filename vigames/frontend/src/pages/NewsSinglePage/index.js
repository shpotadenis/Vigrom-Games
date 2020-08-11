import BreadcrumbsComponent from "../../components/BreadcrumbsComponent/index.vue"
import FooterComponent from "../../components/FooterComponent/index.vue"
import Checkout from "../../components/Pop-ups/Checkout/checkout"
import CommentsComponent from "../../components/CommentsComponent/index.vue"
import news from '../../api/modules/news.js'
import { getImageUrl } from '../../utils.js'

export default {
    name: "NewsSinglePage",
    components: {
        BreadcrumbsComponent,
        FooterComponent,
        Checkout,
        CommentsComponent
    },
    data() {
        return {
            loading: false,
            isBtnClick: false,
            newsData: {}
        }
    },
    computed: {
        getImage() {
            return getImageUrl(this.newsData.img)
        },

        breadcrumbs() {
            return [
                {
                    to: {
                        name: 'homePage'
                    },
                    title: 'Главная'
                },
                {
                  to: {
                      name: 'newsPage'
                  },
                  title: 'Новости'
                },
                {
                    title: this.newsData.title
                }
            ]
        },
    },

    beforeMount() {
        this.fetchData(this.$route.params.id)
    },

    methods: {
        fetchData(id) {
            this.loading = true
            news.getNewsInfo(id).then(response => {
                this.newsData = response.data
                console.log(response)
                this.loading = false
            }).catch(error => {
                console.log(error)
            })
        },

        newsUpdate() {
            this.fetchData(this.$route.params.id)
            this.$scrollTo('#comments', 300)
        }
    }

}
