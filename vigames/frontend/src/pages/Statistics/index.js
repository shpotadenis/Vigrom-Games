import FooterComponent from '../../components/FooterComponent/index.vue'
import { Line } from 'vue-chartjs'
import BarChart from './index1.vue'
import games from '../../api/modules/games.js'

export default {
    extends: Line,
    name: "Statistics",
    components: {
        FooterComponent,
        BarChart
    },
    props:{

    },
    data(){
      return {
          loading: false,
          games: [],
          selectedGameIdx: -1,
          detailedStatistics: {}, // подробная статистика об одной игре
          noGames: false
      };
    },
    beforeMount() {
        this.fetchData()
    },
    computed: {
      getLabelsForRating() {
          // eslint-disable-next-line no-unused-vars
          return this.games.map((val, idx, arr) => val.title)
      },
      getRatings() {
          // eslint-disable-next-line no-unused-vars
          return this.games.map((val, idx, arr) => val.rating)
      },
    },

    methods: {
      fetchData() {
          this.loading = true
          games.getStatisticsGameList().then(response => {
              this.games = response.data.rating
              if (response.data.rating && response.data.rating.length > 0) {
                  this.selectGame(0)
              } else {
                  this.noGames = true
              }
              this.loading = false
          }).catch(error => {
              console.log(error)
          })
      },

        selectGame(idx) { // Индекс в массиве this.games
          games.getStatistics(this.games[idx].id).then(response => {
            this.detailedStatistics = response.data
            this.selectedGameIdx = idx

            let orders = this.detailedStatistics.orders
            let keys = Object.keys(orders).sort()
            let labels = []
            let datasets = []
            for (let i = 0, l = keys.length; i < l; i++) {
                labels.push(keys[i])
                datasets.push(orders[keys[i]])
            }

            this.render(labels, datasets)
          }).catch(error => {
              console.log(error)
          })
        },

        render(labels, datasets) {
            this.renderChart({
                labels: labels,
                datasets: [{
                    type:'line',
                    fill:false,
                    label: 'Покупки',
                    borderColor:"#874463",
                    pointBackgroundColor:"#874463",
                    pointRadius:5,
                    lineTension:0,
                    borderWidth:1,
                    data: datasets,
                }],
            })
        }

    },

    mounted () {

    }
  }
