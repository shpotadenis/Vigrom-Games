import FooterComponent from '../../components/FooterComponent/index.vue'
import { Line } from 'vue-chartjs'

export default {
  extends:Line,
    name: "Statistics",
    components: {
        FooterComponent,
    },
    data(){
      return {

      }
    },
    mounted(){
      this.renderChart({
        labels: ["1.08","25.09","23.011"],
        datasets: [{
            label: '# of Votes',
            data: [20, 10, 30],

        }]
      })
    }

}
