import { apiUrl } from './api/api.js'

// Конвертирует объект карточки игры, который пришел по API в объект для компонента GameCard.vue
export function convertApiToComponentObj(object) {
    let obj = {
        id: object.id,
        name: object.title,
        undername: object.author,
        image: getImageUrl(object.img),
        price: object.price
    }

    if (object.image[0]) {
        obj.scrin = getImageUrl(object.image[0].img)
    }

    if (object.image[1]) {
        obj.scrin1 = getImageUrl(object.image[1].img)
    }

    if (object.image[2]) {
        obj.scrin2 = getImageUrl(object.image[2].img)
    }

    if (object.image[3]) {
        obj.scrin3 = getImageUrl(object.image[3].img)
    }

    return obj
}

export function getImageUrl(partOfUrl) {
    return apiUrl + partOfUrl
}