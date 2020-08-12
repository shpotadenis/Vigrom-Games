
import { HorizontalBar } from 'vue-chartjs'

export default {
    extends: HorizontalBar,
    components: {

    },
    props:{

    },
    data(){
      return {
        datasets:[2,3,5,1,4]
      }
    },
    mounted () {
      this.renderChart({
          defaultFontColor:'#fff',
          labels:['game1','game2','game3','game4','game5'],
          datasets:[
            {
              data:this.datasets,
              backgroundColor:'#9F5175',
              scaleFontColor: "#FFFFFF",
              strokeColor : "rgba(51, 51, 51, 1)",
            }
          ]
        }, {
            responsive: true,
            maintainAspectRatio: false,
            legend:{
              display:false,
            },
            scales: {
               yAxes: [{
                 stacked: true,
                 ticks: {
                   beginAtZero: true,
                   min: 0,
                 },
               }],
               xAxes: [{
                 stacked: true,
                 ticks: {
                   beginAtZero: true,
                   categoryPercentage: 0.5,
                   barPercentage: 1,
                 },
               }],
             },
             labels : {
               fontColor : '#ffffff',
               scaleFontSize: 16
             },
          })
    }
  }
