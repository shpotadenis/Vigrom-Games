import user from "../../../api/modules/user.js";

export default {
    name: "goDownload",
    props: ['gameData'],
    components: {},
    data() {
        return {
        }
    },

    methods: {
        downloadGame() {
            user.downloadGame(this.gameData.id).then(response => {
                console.log(response)
                const url = window.URL.createObjectURL(new Blob([response.data]))
                const link = document.createElement('a')
                link.href = url
                link.setAttribute('download', this.gameData.name + '.zip') //or any other extension
                document.body.appendChild(link)
                link.click()
            }).catch(error => {
                console.log(error.response)
            })
        }
    }

}
