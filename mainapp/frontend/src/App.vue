<template>
  <div>
  <!-- <button @click="fetchStreamers">Fetch Streamers</button> -->
    <h1>My Streamers</h1>
    <ul v-if="streamers.length > 0">
      <li 
        v-for="streamer in streamers"
        :key="streamer.id"
      >{{ streamer }}</li>
    </ul>
    <h4 v-else>
      You do not have any streamers at the moment
    </h4>
  </div>
</template>

<script>
export default{
  data() {
    return {
      streamers: [],
    }
  },
  methods : {
    async mounted() {
      //perform an ajax request to fetch the list of streamers
      let response = await fetch("http://localhost:8000/api/streamers");
      let data = await response.json();
      this.streamers = data.streamers;
    }
  }
}
</script>
