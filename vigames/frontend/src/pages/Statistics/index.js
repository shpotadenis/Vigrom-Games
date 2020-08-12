import FooterComponent from '../../components/FooterComponent/index.vue'
import LineChart from "./index2.js"

export default {
    name: "Statistics",
    components: {
        FooterComponent,
        LineChart
    },

    data(){
      return {
            labels:['3.08','6.08','9.08','12.08','15.08','19.08','24.08','29.08','2.09','5.09'],
            labels2: ['Foo', 'Bar','Bar1'],
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


      }
    }
  }
