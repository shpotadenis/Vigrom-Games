import BreadcrumbsComponent from "../../components/BreadcrumbsComponent/index.vue"
import FooterComponent from "../../components/FooterComponent/index.vue"
import Checkout from "../../components/Pop-ups/Checkout/checkout"
import CommentsComponent from "../../components/CommentsComponent/index.vue"

const data = {
    name_news: 'Здесь будет большой заголовок',
    name_game: 'Название игры',
    autor: 'Имя Автора',
    dev: 'Имя Разработчика',
    price: 125
}

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
          isBtnClick: false,
            breadcrumbs: [
                {
                    to: {
                        name: 'newsPage'
                    },
                    title: 'Новости'
                },
                {
                    title: 'Заголовок новости'
                }
            ]
        }
    },
    computed: {
        getGameData() {
            return data;
        }
    }






}
