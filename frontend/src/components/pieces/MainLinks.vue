<!-- <template>
    <div>       
        <router-link to="/">Home</router-link>
        <router-link to="/about">About</router-link>
    </div>
</template> -->




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
        <div class="link_ctnr">            
            <img
                src="@/assets/images/icons/search.svg"
                alt="Archive Icon"
            >            
            <input
                type="text"
                @input="writeSearch($event)"
            >
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
            

            // alert('here')
        },
        writeSearch(event){
            let elem = event.target.value
            let archive_list = document.querySelector('.archive_list')

            let archive_elements = archive_list.querySelectorAll('li')

            if (elem){
                archive_list.style.display = 'flex'
                for (let archive_li of archive_elements){
                    let li_string = archive_li.innerHTML
                    let li_list = li_string.toLowerCase().split('')
                    let li_list_cut = li_list.slice(0, parseInt(li_list.length - li_list.length/2 - 1))
                    for (let elem_letter of elem){
                        if (li_list_cut.includes(elem_letter)){
                            archive_li.style.display = 'block'
                        } else {
                            archive_li.style.display = 'none'
                        }
                    }
                }                
            } else {
                archive_list.style.display = 'none'
                for (let archive_li of archive_elements){
                    archive_li.style.display = 'block'
                }
                
            }

            // if (event){
            //     let elem = event.target.value

            //     console.log(elem.value)

            // }
            console.log(elem)
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