<template>
    <div class="main_link_ctnr">
        <div class="link_ctnr">
            <img
                src="@/assets/images/icons/home.svg"
                alt="Home Icon"
            >
            <router-link to="/">
                Home
            </router-link>
        </div>
        <div class="link_ctnr">
            <img
                src="@/assets/images/icons/about.svg"
                alt="About Icon"
            >
            <router-link
                to="/about">
                About
            </router-link>
        </div>
        <div id="mainlinks_archive" class="link_ctnr" @click="toggleArchiveList($event)">
            <img
                src="@/assets/images/icons/archive.svg"
                alt="Archive Icon"
            >            
            <a>
                Archive
            </a>
        </div>
    </div>
</template>


<script >

export default {
    methods: {
        toggleArchiveList(event){
            let archive_list = document.querySelector('.archive_list')
            if (event.target.status==null){
                event.target.status = 'showing'
                archive_list.style.display = 'flex'
                
            } else {
                event.target.status = null
                archive_list.style.display = 'none'
            }
            console.log(archive_list)
        }
    }
}

</script>


<style lang="scss" scoped>

.main_link_ctnr{
    display: contents;
}

.link_ctnr{
    display: flex;
    gap: .5em;
    align-items: center;
    font-size: .7em;
    a{
        text-decoration: underline;
        cursor: pointer;
    }
}

</style>