
import { Line, HorizontalBar ,mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
  extends: Line, HorizontalBar,
  mixins: [reactiveProp],
  props: {
    labels: Array,
    datasets: Array,
    options: Object
  },
  mounted () {
    this.renderChart({
      labels: this.labels,
      datasets: this.datasets,
      options: this.options
    }, {responsive: true, maintainAspectRatio: false})
  }
}
