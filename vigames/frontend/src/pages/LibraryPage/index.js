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
    name: 'LibraryPage',
    components: {
        FooterComponent,
        SearchComponent,
        BannerComponent,
        ContentCardComponent
    },
    data() {
        return {
            cards: data,
            loading: true
        }
    },

    mounted() {
        this.fetchData()
    },
    computed: {
        getLibraryCards() {
            return this.$store.getters['user/getLibrary']
        }
    },
    methods: {
        fetchData() {
            this.$store.dispatch('user/getLibrary').then(response => {
                console.log('Library added:')
                console.log(response)
            }).catch(error => {
                console.log('Library error')
                console.log(error)
            })
        }
    }
}
