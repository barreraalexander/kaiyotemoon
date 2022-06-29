
<template>
    <ul class="archive_list">
        <li
            v-for="poem in poems"
            :key="poem.id"
            @click="handleClick($event, poem.id)"
        >
            {{poem.title}}
        </li>
    </ul>
</template>

<script>
import axios from 'axios'
// import { watch } from 'fs'

export default {
    data () {
        return {
            poems: [],
            poems_read: ''
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

                localStorage.poems_read += `$${poem_title.innerText}`
                this.poems_read.push(poem_title.innerText)

                console.log(this.poems_read)

            }
            
            
                        
        },
    },

    mounted: async function(){
        // localStorage.clear()


        let result = await axios.get("http://localhost:5001/poems")
        if (result.data){
            for (let elem of result.data){
                this.poems.push({
                    "id" : elem.id,
                    "title" : elem.title
                })
            }
        }

        if (localStorage.poems_read){
            this.poems_read = localStorage.poems_read.split('$')
            for (let title of this.poems_read){
                console.log(title)
            }
            // console.log(this.poems_read)
        } 
    },


    // watch: {
    //     poems_read(newStr){
    //         console.log('changed')
    //         localStorage.poems_read = newStr;
        
    //     }
    // }
}

</script>

<style lang="scss">
@import '@/assets/scss/pieces/ArchiveList.scss';
</style>