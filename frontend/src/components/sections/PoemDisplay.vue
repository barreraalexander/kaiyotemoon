<script setup>
import axios from 'axios';
</script>

<template>
    <section id="PoemDisplay">
        <h1 id="poem_title">
            {{poem_title}}
        </h1>
        <p id="poem_content">
            {{poem_content}}
        </p>
    </section>
</template>

<script>

export default {
    data () {
        return {
            poem_title: "title",
            poem_content: "content",
        }
    },

    methods : {
        async getPoems() {
            let result = await axios.get('http://localhost:5001/poems')
            if (result.data){
                return result.data
            }
        },
        async getPoem() {
            let result = await axios.get('http://localhost:5001/poems')
            if (result.data){
                return result.data
            }
        },
    },

    mounted: async function(){
        let poems = await this.getPoem()
        if (poems){
            this.poem_title = poems[2].title
            this.poem_content = poems[2].content            
        }
    }


}

</script>

<style lang="scss">
@import "@/assets/scss/sections/PoemDisplay.scss";
</style>