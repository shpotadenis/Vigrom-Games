import FooterComponent from '../../components/FooterComponent/index.vue'
import SearchComponent from '../../components/SearchComponent/index.vue'
import BannerComponent from '../../components/BannerComponent/index.vue'
import ContentCardComponent from '../../components/ContentCardComponent/index.vue'
import GameCard from "@/components/GameCard/GameCard.vue"

const data =  [
    {
        id: 1,
        title: 'FARCRY5',
        author: 'Ubisoft Nadeo | Ubisoft',
        img: 'url', // Обложка картинки
        image: [
            {
                author: 'string',
                img: 'url'
            }], // Скриншоты
        price: 199.00
    },
]


export default {
    name: 'LibraryPage',
    components: {
        FooterComponent,
        SearchComponent,
        BannerComponent,
        ContentCardComponent,
        GameCard
    },
    data() {
        return {
            cards: data,
            loading: true,
            populars:[
                {
                    id:"1",
                    img:"MaskGroup.svg",
                    title:"DANGER CREW",
                    rating:"4.9",
                    undername:"Ubisoft Nadeo | Ubisoft",
                    price:"299.99",
                    scrin:'vessel-5.jpg',
                    scrin1:'c97a9.jpg',
                    scrin2:'Pic1.jpg',
                    scrin3:'c97a9.jpg',
                    icon:'cart-icon.png'
                },
                {
                    id:"2",
                    image:"MaskGroup.svg",
                    name:"DANGER CREW",
                    rating:"4.9",
                    undername:"Ubisoft Nadeo | Ubisoft",
                    price:"299.99",
                    scrin:'vessel-5.jpg',
                    scrin1:'c97a9.jpg',
                    scrin2:'Pic1.jpg',
                    scrin3:'c97a9.jpg',
                    icon:'cart-icon.png'
                },
            ]
        }
    },

    mounted() {
        this.fetchData()
    },
    computed: {
        getLibraryCards() {
            let libraryCards = this.$store.getters['user/getLibrary'] // Карточки, полученные из API
            let libraryComponentCards = [] // Сконвертированные карточки для компонента GameCard
            for (let i in libraryCards) {
                libraryComponentCards.push(this.convertApiToComponentObj(libraryCards[i]))
            }
            return libraryComponentCards
        }
    },
    methods: {
        fetchData() {
            this.$store.dispatch('user/getLibrary').then(response => {
                console.log('Library added:')
                console.log(response)
            }).catch(error => {
                console.log('Library error')
                console.log(error.response)
            })
        },

        convertApiToComponentObj(object) {
            let obj = {
                id: object.id,
                name: object.title,
                undername: object.author,
                scrin: object.img,
                icon: '',
                scrin1: object.image[0].img,
                scrin2: object.image[1].img,
                scrin3: object.image[2].img
            }
        }
    }
}
