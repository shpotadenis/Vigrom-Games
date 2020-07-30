import FooterComponent from '../../components/FooterComponent/index.vue'
import SearchComponent from '../../components/SearchComponent/index.vue'
import BannerComponent from '../../components/BannerComponent/index.vue'
import ContentItemsComponent from '../../components/ContentItemsComponent/index.vue'

const data =  [
    {
        header: 'FARCRY5',
        sub_header: 'Ubisoft Nadeo | Ubisoft'
    },
    {
        header: 'FARCRY5',
        sub_header: 'Ubisoft Nadeo | Ubisoft'
    },
    {
        header: 'FARCRY5',
        sub_header: 'Ubisoft Nadeo | Ubisoft'
    },
    {
        header: 'FARCRY5',
        sub_header: 'Ubisoft Nadeo | Ubisoft'
    },
    {
        header: 'FARCRY5',
        sub_header: 'Ubisoft Nadeo | Ubisoft'
    }
]


export default {
    name: 'LibraryPage',
    components: {
        FooterComponent,
        SearchComponent,
        BannerComponent,
        ContentItemsComponent
    },
    data() {
        return {
            cards: data
        }
    }
}