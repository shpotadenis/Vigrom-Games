import { instance } from '../api'


const login_endpoint = '/auth/token/login/'
const register_endpoint = '/auth/users/'
const role_endpoint = '/api/role'
const library_endpoint = '/api/accounts/profile/library'
const wishlist_endpoint = '/api/accounts/profile/wishlist'
const changepass_endpoint = '/auth/users/set_password/'
const changename_endpoint = '/auth/users/set_username/'
const question_endpoint = '/api/question'
const add_comments = '/api/commentnews/add'
//const addwishlist_endpoint = '/api/games/{0}/wishlist'

export default {
    login(credentials)
    {
        let fd = new FormData()
        fd.append('username', credentials.login)
        fd.append('password', credentials.password)

        return instance.post(login_endpoint, fd)
    },

    register(credentials)
    {
        let fd = new FormData()
        fd.append('username', credentials.login)
        fd.append('password', credentials.password)
        fd.append('email', credentials.email)

        return instance.post(register_endpoint, fd)
    },

    setRole(name, isDev) {
        let fd = new FormData()
        fd.append('username', name)
        fd.append('is_developer', isDev)

        return instance.post(role_endpoint, fd)
    },

    getGamesLibrary() {
        return instance.get(library_endpoint)
    },

    getWishlist() {
      return instance.get(wishlist_endpoint)
    },

    changePassword(credentials) {
        let fd = new FormData()
        fd.append('new_password', credentials.new_password)
        fd.append('re_new_password', credentials.new_password)
        fd.append('current_password', credentials.current_password)

        return instance.post(changepass_endpoint, fd)
    },

    changeName(credentials) {
        let fd = new FormData()
        fd.append('new_username', credentials.username)
        fd.append('current_password', credentials.password)

        return instance.post(changename_endpoint, fd)
    },

    addToWishlist(gameId) {
        return instance.post("/api/games/" + gameId +"/wishlist")
    },

    removeFromWishlist(gameId) {
        return instance.delete('/api/games/' + gameId + '/wishlist')
    },

    buyGame(gameId) {
        return instance.post('/api/games/' + gameId + '/buy')
    },

    downloadGame(gameId) {
        return instance({
            method: 'get',
            url: '/api/games/' + gameId + '/download',
            responseType: 'arraybuffer'
        })
    },

    createReview(gameId, data) {
        let fd = new FormData()
        fd.append('mark', data.mark)
        if (data.comment) {
            fd.append('comment', data.comment)
        }
        fd.append('title', data.title)
        return instance.post('/api/games/' + gameId + '/rating', fd)
    },

    createComment(newsId, data) {
        let fd = new FormData()
        fd.append('id', newsId)
        fd.append('text_comment', data.comment)
        if (data.parent) {
            fd.append('parent', data.parent)
        }
        return instance.post(add_comments, fd)
    },

    uploadGame(data) {
        let fd = new FormData()
        fd.append('title', data.title)
        fd.append('short_description', data.short_description)
        fd.append('price', data.price)
        fd.append('description', data.description)
        fd.append('file', data.file)
        fd.append('genre', data.genre)
        fd.append('img', data.img)
        fd.append('banner', data.banner)
        fd.append('gameplay_video_link', data.gameplay_video_link)
        for (let i in data.images) {
            fd.append('images[' + i + ']', data.images[i])
        }
        fd.append('imagesCount', data.images.length.toString())
        return instance.post('/api/games/add', fd, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
    },

    updateGame(gameId, data) {
        let fd = new FormData()
        fd.append('title', data.title)
        fd.append('short_description', data.short_description)
        fd.append('price', data.price)
        fd.append('description', data.description)
        if (data.file) {
            fd.append('file', data.file)
        }
        fd.append('genre', data.genre)
        if (data.img) {
            fd.append('img', data.img)
        }
        if (data.banner) {
            fd.append('banner', data.banner)
        }

        fd.append('gameplay_video_link', data.gameplay_video_link)
        if (data.images) {
            for (let i in data.images) {
                fd.append('images[' + i + ']', data.images[i])
            }
            fd.append('imagesCount', data.images.length.toString())
        } else {
            fd.append('imagesCount', '0')
        }

        return instance.put('/api/games/' + gameId + '/update', fd, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
    },

    getUploadInfo(gameId) {
        return instance.get('/api/games/' + gameId + '/show_info')
    },

    makeQuestion(data) {
        let fd = new FormData()
        fd.append('email', data.email)
        fd.append('question', data.question)

        return instance.post(question_endpoint, fd)
    }


}