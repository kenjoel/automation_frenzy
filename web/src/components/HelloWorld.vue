<template>
  <div class="hello">
    <h1 v-if="vue_env=='dev'">Upload CSV To Analyse</h1>
    <h1 v-else>Upload CSV To Asnalyse</h1>
    <form @submit="submitForm">
    <input class="input" type="file" name="files" placeholder="File name" multiple required>
    <button type="submit">submit</button>
    </form>

    <div v-if="Object.keys(result).length">
      <pie-chart 
          :datasets="Object.values(result.data)"
          :labels="Object.keys(result.data)"
          chart-type="non-interactive"
          title=""
      />
      <div class="charts">
        <div v-for="chart in result.files" :key="Object.values(chart.Hostname).find( () => true)">
         <pie-chart 
          :datasets="Object.values(chart.percent)"
          :labels="Object.keys(chart.percent)"
          chart-type="non-interactive"
          :title="Object.values(chart.Hostname).find( () => true)"
      />
      </div>
      </div>
    <a :href="result.url" download="">Download File</a>

    </div>

  </div>
</template>

<script>
import axios from "axios"
import PieChart from "./charts.vue"

export default {
  name: 'HelloWorld',
  components:{PieChart},
  data() {
      return{
        result: {},
        vue_env: process.env.VUE_APP_ENV,
      };
  },

  methods: {
    // post_backend(){

    //   const requestOptions = {
    //     method: "POST",
    //     headers: { "Content-Type": "multipart/form-data" }
    //     };


    //   // fetch("http://0.0.0.0:5301/upload", requestOptions)
    //   // .then( async response => {
    //   //   console.log("do something")
    //   //   console.log(response)
    //   // })
    // },

  submitForm(event) {
    event.preventDefault()
    this.formData = new FormData(event.target);

    // this.formData.append('name', this.fileName);
    // this.formData.append('file', this.$refs.file.files[0]);

    axios.post('http://0.0.0.0:5301/upload', this.formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    }).then(response => {
            this.result = response.data
    }).catch(error => {
        console.log(error)
    });
  },
}
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.charts{
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-items: center;
  width: 100%;
  margin: auto;
  justify-content: center;
}

.charts > div{
  margin: 10px;
}

h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
