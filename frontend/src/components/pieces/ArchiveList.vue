<template>
    <ul class="archive_list">
        <div class="close_icon_ctnr">
            <img
                src="@/assets/images/icons/close_alt.svg"
                alt="close icon for archives list"
                @click="handleClose"
            >
        </div>
        <li
            v-for="poem in poems"
            :key="poem.id"
            :data-has_read="this.poems_read.includes(poem.title)"
            @click="handleClick($event, poem.id)"
        >
            {{poem.title}}
        </li>
    </ul>
</template>

<script>
import axios from 'axios'

export default {
    data () {
        return {
            poems: [],
            poems_read: []
        }
    },

    methods : {
        async handleClick(event, id){
            // let header_nav = document.querySelector('#HeaderNavSection')
            let header_nav = document.querySelector('#PoemDisplay')
            header_nav.scrollIntoView()

            let result = await axios.get(`http://localhost:5001/poems/${id}`)
            if (result.data){
                let poem_title = document.querySelector('#poem_title')
                let poem_content = document.querySelector('#poem_content')
                poem_title.innerText = result.data.title
                poem_content.innerText = result.data.content

                if (! this.poems_read.includes(poem_title.innerText)){
                    localStorage.poems_read += `$${poem_title.innerText}`
                    this.poems_read.push(poem_title.innerText)
                    event.target.dataset.poems_read = 'true'
                }

            }  
        },
        handleClose(){
            let archive_list = document.querySelector('.archive_list')
            archive_list.style.display = 'none'

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

        if (localStorage.poems_read){
            this.poems_read = localStorage.poems_read.split('$')
            // for (let title of this.poems_read){
            //     console.log(title)
            // }
        } 
    },
}

</script>

<style lang="scss">
@import '@/assets/scss/pieces/ArchiveList.scss';
</style>