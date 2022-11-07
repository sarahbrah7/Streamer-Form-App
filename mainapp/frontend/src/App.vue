<template>
  <div>
    <h1>My Streamers</h1>
    <button @click="fetchStreamers" class="btn btn-outline-alert btn-success mt-3">Fetch Streamers</button>
    <ul v-if="streamers.length > 0">
      <li 
        v-for="streamer in streamers"
        :key="streamer.id"
      >{{ streamer }}</li>
    </ul>
    <h4 v-else>
      You do not have any streamers at the moment
    </h4>
    <HelloWorld />
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

  export default{
    components: { HelloWorld },
    data() {
        return {
            streamer: '',
            streamers: [],
        }
    },
    methods: {
        async fetchStreamers() {
            //perform an ajax request to fetch the list of streamers
            let response = await fetch("http://localhost:8080/api/streamers");
            let data = await response.json();
            this.streamers = data.streamers;
        }
    },
  }
</script>
