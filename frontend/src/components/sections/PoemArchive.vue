<script setup>
import ArchiveList from '@/components/pieces/ArchiveList.vue';
</script>

<template>
    <section id="PoemArchive">
        <div class="banner_ctnr">
            <div class="archive_banner">
                <img src="@/assets/images/icons/archive.svg" alt="">
                <h3>
                    Archive
                </h3>
            </div>
            <ArchiveList/>
        </div>

    </section>

</template>

<!-- <script>
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

</script> -->

<style lang="scss">
@import "@/assets/scss/sections/PoemArchive.scss";
</style>