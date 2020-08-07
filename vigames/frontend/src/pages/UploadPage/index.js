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
        selectFile2:"Перетащите файл размером 1100х441 или кликните здесь, чтобы добавить его",
        selectFile3:"Перетащите файл размером 324х255 или кликните здесь, чтобы добавить его",
        b:"",
        a:[]

      }
    },
    methods:{
      UpLoadFile(event){
        console.log(event.target.selectFile)
        this.selectFile = event.target.files[0].name;       //Это имя файла

      },
      UpLoadFile1(){
          for(let i=0; i<6;i++){
            this.b = event.target.files[i]
            this.a = this.b.name
            this.selectFile1 = this.a

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

    }

}
