import FooterComponent from '../../components/FooterComponent/index.vue'

export default {
    name: "UploadPage",
    components:{
        FooterComponent
    },
    data(){
      return{
        selectFile:"Перетащите файл или кликните здесь, чтобы добавить его*",
        selectFile1:"Перетащите 3-5 файлов размером 324х255 или кликните здесь, чтобы добавить их",
        array:[],
        selectFile2:"Перетащите файл размером 1100х441 или кликните здесь, чтобы добавить его",
        selectFile3:"Перетащите файл размером 324х255 или кликните здесь, чтобы добавить его",
<<<<<<< HEAD
        title: '',
        short_description: '',
        genre: '',
        price: '',
        block1: '',
        block2: '',
        block3: '',
        youtube_link: '',
        b:"",
        a:[]
=======
>>>>>>> 43d6222689cd29a3a93df39f79714df90132e8ec

      }
    },

    methods:{
        UpLoadFile(event){
            console.log(event.target.selectFile)
            this.selectFile = event.target.files[0].name;       //Это имя файла

        },
        UpLoadFile1(event){
            console.log(event.target.selectFile)
            for(let i=0; i<5;i++){
              this.selectFile1 = event.target.files[i].name;
            }
        },
        UpLoadFile2(event){
            console.log(event.target.selectFile)
            this.selectFile2 = event.target.files[0].name;       //Это имя файла
        },
        UpLoadFile3(event){
            console.log(event.target.selectFile)
            this.selectFileZ = event.target.files[0].name;       //Это имя файла
        },
        uploadButtonClick() {
      },
<<<<<<< HEAD
    }
=======
      UpLoadFile1(){
        if(this.array.lenght !=0){
          this.selectFile1 = ""
        }
        for(let i=0; i<5;i++){
          this.array.push(event.target.files[i].name)
        }

      },
      UpLoadFile2(event){
        console.log(event.target.selectFile)
        this.selectFile2 = event.target.files[0].name;       //Это имя файла
      },
      UpLoadFile3(event){
        console.log(event.target.selectFile)
        this.selectFile3 = event.target.files[0].name;       //Это имя файла
      },

    },

>>>>>>> 43d6222689cd29a3a93df39f79714df90132e8ec

}
