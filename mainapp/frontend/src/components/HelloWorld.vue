<template>
    <div class="border border-secondary p-4 rounded">
        <h3 class="font-weight-bold">Add a streamer:</h3>
        <form @submit.prevent="saveNewName">
            <div class="form-group mt-4 mb-4 row">
                <label for="streamer_name" class="col-sm-3 col-form-label">Streamer's name:</label>
                <div class="col-sm-9">
                    <input type="text" class="form-control" id="streamer_name" placeholder="Streamer's name" v-model="streamer_name" />
                </div>
            </div>
            <div class="form-group mb-4 row">
                <label for="stream" class="col-sm-3 col-form-label">Previous stream:</label>
                <div class="col-sm-9">
                    <input class="form-control" type="datetime-local" id="stream" v-model="last_stream" />
                </div>
            </div>
            <div class="form-group mb-4 row">
                <label for="rating" class="col-sm-3 col-form-label">Streamer Rating:</label>
                <div class="col-sm-1">
                    <select class="form-control" type="number" id="rating" v-model="rating">
                        <option>1</option>
                        <option>2</option>
                        <option>3</option>
                        <option>4</option>
                        <option>5</option>
                    </select>
                </div>
            </div>

            <div class="form-check row">
                <div class="col-sm-10 offsetsm-2">
                    <input class="form-check-input ml-2" type="checkbox" id="platform" v-model="platform" />
                    <label for="streamer_name" class="form-check-label d-flex">Twitch streamer?</label>
                </div>                                     
            </div>

            <div class="form-group row mb-3 mt-3">
                <div class="col-sm-3">
                    <button class="btn btn-secondary">Submit</button>
                </div>
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
                current_streamer: this.current_streamer,
            }
        },
        methods: {
            async saveNewName() {
                const response = await fetch("http://localhost:8000/api/streamers", {
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
