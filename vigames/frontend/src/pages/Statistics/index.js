import FooterComponent from '../../components/FooterComponent/index.vue'
import { Line } from 'vue-chartjs'
import BarChart from './index1.vue'

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
      return {};
    },
    mounted () {
      this.renderChart({
            labels:['3.08','6.08','9.08','12.08','15.08','19.08','24.08','29.08','2.09','5.09'],
              datasets: [{
                type:'line',
                fill:false,
                borderColor:"#874463",
                pointBackgroundColor:"#874463",
                pointRadius:5,
                lineTension:0,
                borderWidth:1,
                data: [19,59,69,150,189,201,376,320,298,406],
            }],


      })
    }
  }
