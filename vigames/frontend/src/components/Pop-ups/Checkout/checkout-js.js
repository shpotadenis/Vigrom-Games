import GoDownload from "../../../components/Pop-ups/GoDownload/index.vue"


export default {
    name: "checkout",
    components: {
        GoDownload
    },
    props: ['gameData'],
    data() {
        return {
          ammount_donate: 0,
          isBtnDonate1Click: false,
          isBtnDonate2Click: false,
          isBtnDonate3Click: false,
          isBtnClick2: false
        }
    },

    methods: {
        isClick1() {
            this.ammount_donate = 0;
            this.isBtnDonate1Click = true;
            this.isBtnDonate2Click = false;
            this.isBtnDonate3Click = false;
        },
        isClick2() {
            this.ammount_donate = 100;
            this.isBtnDonate1Click = false;
            this.isBtnDonate2Click = true;
            this.isBtnDonate3Click = false;
        },
        isClick3() {
            this.ammount_donate = 200;
            this.isBtnDonate1Click = false;
            this.isBtnDonate2Click = false;
            this.isBtnDonate3Click = true;
        },

        buyGame() {
          this.$store.dispatch('user/buyGame', {
              gameId: this.getGameData.id
          }).then(response => {
              if (response) {
                  this.isBtnClick2 = true
              }
          }).catch(error => {
              console.log(error)
          })
        }
    },

    computed: {
        getGameData() {
            return this.gameData;
        }
    }

}
