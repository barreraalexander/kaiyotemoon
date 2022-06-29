
<template>
    <button @click="clearReadHistory" >
        Clear Read History
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

<style scoped lang="scss">

button{
    @include light_shadow;
    @include sm_text;
    padding: .25em 1em;
    background-color: $proj_primary_light;
    border-radius: 10px;
    border-color: $proj_primary_dark;
    color: $proj_primary_dark;
    font-weight: 400;
    font-size: 1em;
}

</style>