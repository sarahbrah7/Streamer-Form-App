<template>
    <!-- <div class="border rounded bg-danger shadow p-4">
        The new value is: {{ name }}
        <div>
            <input class="form-control" v-model="name">
            <button class="btn btn-sm btn-success mt-3">Save</button>
        </div> -->
    <div>
        <form id="getStreamerForm" @submit.prevent="saveNewName">
            <div id="streamerInput">
                <fieldset>
                    <input class="form-control" type="text" id="streamerName" v-model="streamer_name" />
                    <input class="form-control" type="checkbox" id="platform" v-model="platform" />
                    <input class="form-control" type="datetime-local" id="stream" v-model="last_stream" />
                    <input class="form-control" type="number" id="rating" v-model="rating" />
                    <button>Submit</button>
                </fieldset>
            </div>
        </form>
    </div>
</template> 

<script>
    export default {
        data() {
            return {
                streamer_name: this.streamer_name,
                platform: this.platform,
                last_stream: this.last_stream,
                rating: this.rating,
            }
        },
        methods: {
            async saveNewName() {
                const data = await fetch("http://localhost:8080/api/streamers", {
                    method : 'POST',
                    body: JSON.stringify({
                        streamer_name: this.streamer_name,
                        platform: this.platform,
                        last_stream: this.last_stream,
                        rating: this.rating,
                    })
                })

            }
        }
    }
</script>
