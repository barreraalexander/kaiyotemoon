
<template>
    <button @click="clearReadHistory" >
        clear
    </button>
</template>

<script>


export default {
    methods : {
        clearReadHistory(){
            localStorage.poems_read = ''
            let archive_lists = document.querySelectorAll('li[data-has_read=true]')
            for (let elem of archive_lists){
                elem.dataset.has_read = "false"
            }
            location.reload()
        }
    }
}

</script>