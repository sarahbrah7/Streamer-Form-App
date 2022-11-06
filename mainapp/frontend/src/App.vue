<template>
  <div>
    <button @click="fetchStreamers">Fetch Streamers</button>
    <div>
      <ul>
        <li v-for="streamer in streamers">
          {{ streamer.name}}
          <span v-if="streamer.twitch">(Twitch Streamer)</span>
          <span v-if="!streamer.twitch">(Youtube Streamer)</span>
        </li>
      </ul>
    </div>
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
    async fetchStreamers() {
      //perform an ajax request to fetch the list of streamers
      let response = await fetch("http://localhost:8000/api/streamers")
      let data = await response.json()
      this.streamers = data.streamers
    }
  }
}
</script>
