import user from "../../../api/modules/user";

export default {
    name: "goDownload",
    components: {},
    data() {
        return {
        }
    },

    methods: {
        downloadGame() {
            user.downloadGame(this.$route.params.id).then(response => {
                console.log(response)
                const url = window.URL.createObjectURL(new Blob([response.data]))
                const link = document.createElement('a')
                link.href = url
                link.setAttribute('download', this.getGameData.title + '.zip') //or any other extension
                document.body.appendChild(link)
                link.click()
            }).catch(error => {
                console.log(error.response)
            })
        }
    }

}
