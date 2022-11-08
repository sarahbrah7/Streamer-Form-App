<template>
  <div>
    <h1>My Streamers</h1>
    <button @click="fetchStreamers" class="btn btn-outline-alert btn-success mt-3">Fetch Streamers</button>
    <ul v-if="streamers.length > 0">
      <li 
        v-for="streamer in streamers"
        :key="streamer.id"
      >
      {{ streamer }}
      <button @click="changePlatform(
        streamer.platform,
        streamer.last_stream, 
        streamer.rating, 
        streamer.name,
        streamer.id,
      )">Update</button>
      <button @click="deleteStreamer(streamer.id)">Delete</button>
    </li>
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
    //shows streamers without requiring a button onClick
    created(){
      this.fetchStreamers()
    },
    components: { HelloWorld },
    data() {
        return {
            streamer: '',
            streamers: [],
            platform: this.platform,
            last_stream: this.last_stream,
            rating: this.rating,
            streamer_name: this.streamer_name,
            streamer_id: this.id,
        }
    },
    methods: {
        async fetchStreamers() {
            //perform an ajax request to fetch the list of streamers
            let response = await fetch("http://localhost:8000/api/streamers")
            let data = await response.json()
            this.streamers = data.streamers
        },
        async changePlatform(platform, last_stream, rating, streamer_name, streamer_id) {
          platform = !platform
          const response = await fetch("http://localhost:8000/api/streamers", {
              method : 'PUT',
              body: JSON.stringify({
                platform: platform,
                last_stream: last_stream,
                rating: rating,
                streamer_name: streamer_name,
                streamer_id: streamer_id,
              })
            })
            let data = await response.json()
            this.streamer = data.streamer
        },
        async deleteStreamer(streamer_id){
          let response = await fetch("http://localhost:8000/api/streamers", {
              method: 'DELETE',
              body: JSON.stringify({
                streamer_id: streamer_id,
            })
          })
          let data = await response.json()
          this.streamer = data.streamer
        }
    },
  }
</script>
