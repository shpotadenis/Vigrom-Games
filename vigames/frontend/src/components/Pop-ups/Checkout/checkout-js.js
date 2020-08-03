import GoDownload from "../../../components/Pop-ups/GoDownload/index.vue"

export default {
    name: "checkout",
    components: {
        GoDownload
    },
    data() {
        return {
          isBtnClick2: false,
          isBtnDonate1Click: false,
          isBtnDonate2Click: false,
          isBtnDonate3Click: false
        }
    },

    methods: {
      isClick1() {
        this.isBtnDonate1Click = true;
        this.isBtnDonate2Click = false;
        this.isBtnDonate3Click = false;
      },
      isClick2() {
        this.isBtnDonate1Click = false;
        this.isBtnDonate2Click = true;
        this.isBtnDonate3Click = false;
      },
      isClick3() {
        this.isBtnDonate1Click = false;
        this.isBtnDonate2Click = false;
        this.isBtnDonate3Click = true;
      }
    }

}
