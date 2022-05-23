<template>
    <div class="row align-items-center">
        <div class="col-sm-7">
            <canvas style="max-width: 100%; max-height: 400px;" ref="pieChartArea"></canvas>
        </div>
        <div class="col-sm-5">
            <div ref="chartLegend" class="d-flex flex-column flex-wrap" style="width: 100%; max-height: 300px">
            </div>
        </div>
    </div>
</template>
<style scoped>
.legend-item:hover, .active-legend {
    color: #1a5069;
}
</style>
<script>
import Chart from 'chart.js/auto';

export default {
    name: 'PieChart',
    props: ['canvas_ref', 'labels', 'datasets', 'title', 'chartType', 'color', 'slicerColors', 'activeColor', 'defaultColor'],
    data() {
        return {
            activeLegend: null,
            config: {
                plugins: [this.htmlLegendPlugin()],
                type: 'doughnut',
                data: {
                    labels: this.labels,
                    datasets: [
                        {
                            data: this.datasets,
                        }
                    ]
                },
                options: {
                    responsive: true,
                    plugins: {
                        htmlLegend: {
                            // ID of the container to put the legend in
                            containerID: 'custom-id',
                        },
                        title: {
                            display: true,
                            text: this.title
                        },
                        // colorschemes: {
                        //     scheme: this.colorScheme
                        // },
                    },
                }
            },
            chart:null,
        }
    },
    methods: {
        renderChart() {
            const ctx = this.$refs.pieChartArea.getContext('2d')
            if (!this.chart) {
                this.chart = new Chart(ctx, this.config);
            }
        },
        handleChartAreaClick(event) {
            if (this.chartType !== 'interactive') {
                return;
            }

            const points = this.chart.getElementsAtEventForMode(event, 'nearest', {intersect: true}, false);
            if (points.length) {
                const firstPoint = points[0];
                const label = this.chart.data.labels[firstPoint.index];
                this.handleCustomFilter(label)
                // var value = this.chart.data.datasets[firstPoint.datasetIndex].data[firstPoint.index];
                // console.log(label,value)
            }
        },
        getOrCreateLegendList(chart, id) {
            const legendContainer = document.getElementById(id);
            let listContainer = legendContainer.querySelector('ul');

            if (!listContainer) {
                listContainer = document.createElement('ul');
                listContainer.style.display = 'flex';
                listContainer.style.flexDirection = 'row';
                listContainer.style.margin = 0;
                listContainer.style.padding = 0;

                legendContainer.appendChild(listContainer);
            }

            return listContainer;
        },
        htmlLegendPlugin(){
            return {
                id: 'htmlLegend',
            }
        },
        updateChartColor(value) {
            const labelPosition = this.chart.data.labels.indexOf(value)
            let colors = this.generateColors()
            colors[labelPosition] = this.activeColor
            this.chart.data.datasets[0].backgroundColor = colors
            this.chart.update()
        },
        handleCustomFilter(value) {
            if (this.chartType !== 'interactive') {
                return;
            }
            this.activeLegend = value
            this.$store.commit("setCurrentCategory", value)
        },
        generateLabels(chart) {
            const data = chart.data;
            if (data.labels.length && data.datasets.length) {
                return data.labels.map(function (label, i) {
                    const meta = chart.getDatasetMeta(0);
                    const style = meta.controller.getStyle(i);

                    return {
                        text: label,
                        fillStyle: style.backgroundColor,
                        strokeStyle: style.borderColor,
                        lineWidth: style.borderWidth,
                        hidden: isNaN(data.datasets[0].data[i]) || meta.data[i].hidden,

                        // Extra data used for toggling the correct item
                        index: i
                    };
                });
            }
            return [];
        },
    },
    watch: {
        datasets(newVal) {
            this.chart.data.datasets[0].data = newVal;
            this.chart.update();
        },
        activeLegend(value) {
            this.updateChartColor(value)

        },
        labels(newVal) {
            this.chart.data.labels = newVal;
            this.chart.update();
        },
        title(newVal) {

            this.chart.options.plugins.title.text = newVal;
            this.chart.update();
        },
    },
    mounted() {
        this.renderChart()
    },

}
</script>
