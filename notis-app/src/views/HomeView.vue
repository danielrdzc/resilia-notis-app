<template>
  <div class="home">
    <button @click="testAPI">Test API</button>
    <textarea v-model="apiResult" name="" id="" cols="30" rows="10"></textarea>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  data () {
    return {
      apiResult: ''
    }
  },
  methods: {
    testAPI() {
      this.axios.get('http://localhost:5000/api/test')
        .then((response) => {
          console.log(response)
          this.apiResult = response.data
        })
        .catch((response) => {
          alert('error')
        })
    }
  }
}
</script>
