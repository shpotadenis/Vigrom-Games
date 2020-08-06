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
        selectFile3:"Перетащите файл размером 324х255 или кликните здесь, чтобы добавить его"
      }
    },
    methods:{
      UpLoadFile(event){
        console.log(event.target.selectFile)
        this.selectFile = event.target.files[0].name;
      },
      UpLoadFile1(event){
        console.log(event.target.selectFile1)
        this.selectFile1 = event.target.files[0].name;
      },
      UpLoadFile2(event){
        console.log(event.target.selectFile2)
        this.selectFile2 = event.target.files[0].name;
      },
      UpLoadFile3(event){
        console.log(event.target.selectFile3)
        this.selectFile3 = event.target.files[0].name;
      }

    }

}
