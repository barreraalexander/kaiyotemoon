<template>
    <section id="PoemArchive">
        <h3>
            Poem Archive
        </h3>
        <ul>
            <li
                v-for="poem in poems"
                :key="poem.id"
                @click="handleClick($event, poem.id)"            >
                {{poem.title}}
            </li>
        </ul>
    </section>

</template>

<script>
import axios from 'axios'

export default {
    data () {
        return {
            poems: []
        }
    },

    methods : {
        async handleClick(event, id){
            let result = await axios.get(`http://localhost:5001/poems/${id}`)
            if (result.data){
                let poem_title = document.querySelector('#poem_title')
                let poem_content = document.querySelector('#poem_content')
                poem_title.innerText = result.data.title
                poem_content.innerText = result.data.content
            }
            
        }
    },

    mounted: async function(){
        let result = await axios.get("http://localhost:5001/poems")
        if (result.data){
            for (let elem of result.data){
                // this.poem_titles.push(elem.title)
                this.poems.push({
                    "id" : elem.id,
                    "title" : elem.title
                })
            }
        }
        // let poems = 
        // console.log(this.poem_display_methods)
    }
}

</script>

<style lang="scss">
@import "@/assets/scss/sections/PoemArchive.scss";
</style>