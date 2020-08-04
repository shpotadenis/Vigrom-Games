import BreadcrumbsComponent from "../../components/BreadcrumbsComponent/index.vue"
import FooterComponent from "../../components/FooterComponent/index.vue"


export default {
    name: "NewsSinglePage",
    components: {
        BreadcrumbsComponent,
        FooterComponent
    },
    data() {
        return {
            breadcrumbs: [
                {
                    to: {
                        name: 'newsSinglePage'
                    },
                    title: 'Новости'
                },
                {
                    title: 'Заголовок новости'
                }
            ]
        }
    },






}
