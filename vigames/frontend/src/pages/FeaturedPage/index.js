import FooterComponent from '../../components/FooterComponent/index.vue'
import SearchComponent from '../../components/SearchComponent/index.vue'
import BannerComponent from '../../components/BannerComponent/index.vue'
import ContentCardComponent from '../../components/ContentCardComponent/index.vue'

const data =  [
    {
        title: 'FARCRY5',
        subtitle: 'Ubisoft Nadeo | Ubisoft',
        price: 199.00
    },
    {
        title: 'FARCRY5',
        subtitle: 'Ubisoft Nadeo | Ubisoft',
        price: 1999.00
    },
    {
        title: 'FARCRY5',
        subtitle: 'Ubisoft Nadeo | Ubisoft',
        price: 1999.00
    },
    {
        title: 'FARCRY5',
        subtitle: 'Ubisoft Nadeo | Ubisoft',
        price: 1999.00
    },
    {
        title: 'FARCRY5',
        subtitle: 'Ubisoft Nadeo | Ubisoft',
        price: 1999.00
    },
    {
        title: 'FARCRY5',
        subtitle: 'Ubisoft Nadeo | Ubisoft',
        price: 1999.00
    },
    {
        title: 'FARCRY5',
        subtitle: 'Ubisoft Nadeo | Ubisoft',
        price: 1999.00
    },
    {
        title: 'FARCRY5',
        subtitle: 'Ubisoft Nadeo | Ubisoft',
        price: 1999.00
    },
    {
        title: 'FARCRY5',
        subtitle: 'Ubisoft Nadeo | Ubisoft',
        price: 1999.00
    },
    {
        title: 'FARCRY5',
        subtitle: 'Ubisoft Nadeo | Ubisoft',
        price: 1999.00
    },
    {
        title: 'FARCRY5',
        subtitle: 'Ubisoft Nadeo | Ubisoft',
        price: 1999.00
    },
    {
        title: 'FARCRY5',
        subtitle: 'Ubisoft Nadeo | Ubisoft',
        price: 1999.00
    }
]


export default {
    name: 'FeaturedPage',
    components: {
        FooterComponent,
        SearchComponent,
        BannerComponent,
        ContentCardComponent
    },
    data() {
        return {
            cards: data
        }
    }
}
