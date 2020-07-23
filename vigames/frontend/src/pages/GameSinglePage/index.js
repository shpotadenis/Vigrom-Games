import ReviewsComponent from "../../components/ReviewsComponent/index.vue";

const data = {
    id: 1,
    name: 'Название игры',
    dev: 'Имя Разработчика',
    price: 125,
    desc: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae quam consectetur, auctor ligula a, rutrum nisl. Aenean eget hendrerit arcu. Pellentesque sodales ligula eget commodo pellentesque. Curabitur bibendum nisi at velit vulputate efficitur. Ut tempus massa erat, nec ultrices mi pellentesque sit amet. Donec hendrerit id diam nec consequat. Praesent sit amet dui cursus, euismod est id, elementum nunc. Integer ut justo urna.\n' +
        '                           Sed bibendum sollicitudin commodo. Curabitur sollicitudin, nisl a mattis egestas, mi metus iaculis nisi, et ornare eros orci cursus leo.',
    category: 'Название категориии',
    rating: 'Положительный',
    compatible: 'x64',
    size: '1.57 GB',
    languages: ['Русский', 'English']
}

export default {
    name: "GameSinglePage",
    components: {
        ReviewsComponent
    },
    computed: {
        getGameData() {
            return data;
        }
    }

}