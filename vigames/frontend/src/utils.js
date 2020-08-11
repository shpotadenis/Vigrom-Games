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
    // Отображение скидки
    if (object.sale_percent) {
        obj.sale = object.sale_percent
    } else {
        obj.sale = 0
    }

    return obj
}

export function getImageUrl(partOfUrl) {
    return apiUrl + partOfUrl
}