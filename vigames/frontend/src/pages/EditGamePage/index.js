import FooterComponent from '../../components/FooterComponent/index.vue'
import GameDownloaded from "../../components/Pop-ups/GameDownloaded/index.vue"
import user from '../../api/modules/user.js'

export default {
    name: "UploadPage",
    components:{
        FooterComponent,
        GameDownloaded
    },
    data(){
        return{
            isBtnClick: false,
            selectFile:"Перетащите файл или кликните здесь, чтобы добавить его*",
            selectFile1:"Перетащите 3-5 файлов размером 324х255 или кликните здесь, чтобы добавить их",
            array:[{name: 'Перетащите 3-5 файлов размером 324х255 или кликните здесь, чтобы добавить их'}],
            selectFile2:"Перетащите файл размером 1100х441 или кликните здесь, чтобы добавить его",
            selectFile3:"Перетащите файл размером 324х255 или кликните здесь, чтобы добавить его",
            archiveGame: null,
            img: null,
            agreement: false,
            banner: null,
            title: '',
            short_description: '',
            genre: '',
            price: '',
            block1: '',
            block2: '',
            block3: '',
            youtube_link: '',
            b:"",
            OS: '',
            a:[],
            options: [
                {name: 'Приключения', value: 'adventures'},
                {name: 'Головоломки', value: 'puzzles'},
                {name: 'Экшн', value: 'action'},
                {name: 'РПГ', value: 'rpg'},
                {name: 'Стратегии', value: 'strategy'},
                {name: 'Фермы', value: 'farms'},
                {name: 'ММО', value: 'mmo'},
                {name: 'Шутеры', value: 'shooters'},
                {name: 'Гонки', value: 'race'},
                {name: 'Симуляторы', value: 'simulators'},
            ],
            options_second: [
                {name: 'Windows', value: 'windows'},
                {name: 'MacOS', value: 'macos'},
                {name: 'Обе платформы', value: 'both'},
            ],
            areOptionsVisible: false,
            areOptionsVisible_second: false,
            selected: 'Выберите жанр',
            selected_two: 'Выберите платформу'
        }
    },

    methods:{
        UpLoadFile(event){
            console.log(event.target.selectFile)
            this.selectFile = event.target.files[0].name       //Это имя файла
            this.archiveGame = event.target.files[0]
        },
        UpLoadFile1(event){
            console.log(event.target.files[0])
            for(let i=0; i<5;i++) {
                this.selectFile1 = event.target.files[i].name
                this.array[i] = event.target.files[i]
            }
        },
        UpLoadFile2(event){
            console.log(event.target.selectFile)
            this.selectFile2 = event.target.files[0].name       //Это имя файла
            this.banner = event.target.files[0]
        },
        UpLoadFile3(event){
            console.log(event.target.selectFile)
            this.selectFile3 = event.target.files[0].name       //Это имя файла
            this.img = event.target.files[0]
        },
        uploadButtonClick() {
            this.isBtnClick = true;
            let data = {
                title: this.title,
                short_description: this.short_description,
                genre: this.genre,
                price: this.price,
                description: this.block1 + this.block2 + this.block3,
                file: this.archiveGame,
                img: this.img,
                banner: this.banner,
                gameplay_video_link: this.youtube_link,
                images: this.array,
                OS: this.OS
            }
            console.log(data)
            user.uploadGame(data).then(response => {
                console.log(response)
                this.$router.push({
                    name: 'singlePage',
                    params: {
                        id: response.data.id
                    }
                })
            }).catch(error => {
                console.log(error)
                console.log(error.response)
            })
        },
        selectOption(option) {
            this.genre = option.value;
            this.selected = option.name;
            this.areOptionsVisible = false;
        },
        select_second_Option(option) {
            this.OS = option.value;
            this.selected_two = option.name;
            this.areOptionsVisible_second = false;
        },
    }

}
