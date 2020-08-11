import FooterComponent from '../../components/FooterComponent/index.vue'
import { Line, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
    extends: Line,
    mixins: [reactiveProp],
    props: ['options'],
    name: "Statistics",
    components: {
        FooterComponent,

    },
    data(){
      return {};
    },
    methods:{
    },
    computed:{
    },
    chartData:{
      labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
          datasets: [{
              label: 'My First dataset',
              backgroundColor: 'rgb(255, 99, 132)',
              borderColor: 'rgb(255, 99, 132)',
              data: [0, 10, 5, 2, 20, 30, 45]
          }]
    },
    mounted () {
      this.renderChart(this.chartData, this.options)
    }

}