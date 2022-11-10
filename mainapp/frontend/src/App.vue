<template>
  <div class="container-xxl">
    <header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
      <div class="col-4 pt-1">
        <span class="fs-2">Streamer Tracker</span>
      </div>
      <div class="col-4 text-center">
        <br>
      </div>
      <div class="col-4 d-flex justify-content-end align-items-center">
        <button @click="fetchStreamers" class="btn btn-outline-secondary me-2">Fetch Streamers</button>
      </div>
    </header>
    <table class="table" v-if="streamers.length > 0">
      <thead class="thead-dark">
        <tr>
          <th scope="col">Streamer</th>
          <th scope="col">Last time streamed</th>
          <th scope="col">Twitch stream?</th>
          <th scope="col">Rating</th>
          <th scope="col"> </th>
          <th scope="col"></th>
          <th scope="col"></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="streamer in streamers"
        :key="streamer.id">
          <th scope="row">{{ streamer.name }}</th>
          <td>
            <p>{{ streamer.last_stream.substring(0,10) }} &nbsp;&nbsp; {{ streamer.last_stream.substring(11,19) }}</p>
          </td>
          <td v-if="streamer.platform == true" class="text-success">
            Yes
          </td>
          <td v-else class="text-danger">No</td>
          <td>{{ streamer.rating }}</td>
          <td> </td>
          <td>
            <button @click="changePlatform(
              streamer.platform,
              streamer.last_stream, 
              streamer.rating, 
              streamer.name,
              streamer.id,
            )" class="btn btn-secondary">Update</button>
          </td>
          <td>
            <button @click="deleteStreamer(streamer.id)" class="btn btn-danger">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
    <h4 v-else>
      You do not have any streamers at the moment
    </h4>
    <br>
    <div class="form-inline">
      <HelloWorld />
    </div>
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
            this.fetchStreamers()
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
          this.fetchStreamers()
        }
    },
  }
</script>
