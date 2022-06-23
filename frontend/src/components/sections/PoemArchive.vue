<template>
    <section id="PoemArchive">
        <div class="banner_ctnr">
            <img
                id="close_icon"
                src="@/assets/images/icons/close.svg"
                alt=""
                @click="closeArchive"
            >
            <h3>
                Archive
            </h3>
        </div>
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
                this.closeArchive()
            }
            
        },
        closeArchive(){
            let archive_section = document.querySelector('#PoemArchive')
            archive_section.style.display = "none"
        }
    },

    mounted: async function(){
        let result = await axios.get("http://localhost:5001/poems")
        if (result.data){
            for (let elem of result.data){
                this.poems.push({
                    "id" : elem.id,
                    "title" : elem.title
                })
            }
        }
    }
}

</script>

<style lang="scss">
@import "@/assets/scss/sections/PoemArchive.scss";
</style>