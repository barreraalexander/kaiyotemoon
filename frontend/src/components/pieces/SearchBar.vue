<template>
    <div class="search_bar link_ctnr">            
        <img
            src="@/assets/images/icons/search.svg"
            alt="Archive Icon"
        >            
        <input
            type="text"
            @input="writeSearch($event)"
        >
    </div>
</template>

<script>
export default {
    methods: {
        writeSearch(event){
            let elem = event.target.value
            let archive_list = document.querySelector('.archive_list')

            let archive_elements = archive_list.querySelectorAll('li')

            if (elem){
                archive_list.style.display = 'flex'
                for (let archive_li of archive_elements){
                    let li_string = archive_li.innerHTML
                    let leven_dist = this.leven(elem, li_string);
                    if (leven_dist > 10){
                        archive_li.style.display = 'block'
                    } else {
                        archive_li.style.display = 'none'
                    }
                }                
            } else {
                archive_list.style.display = 'none'
                for (let archive_li of archive_elements){
                    archive_li.style.display = 'block'
                }
                
            }
        },
        leven(str1, str2){
            var track = Array(str2.length + 1).fill(null).map(() =>
            Array(str1.length + 1).fill(null));
            for (let i = 0; i <= str1.length; i += 1) {
                track[0][i] = i;
            }
            for (let j = 0; j <= str2.length; j += 1) {
                track[j][0] = j;
            }
            for (let j = 1; j <= str2.length; j += 1) {
                for (let i = 1; i <= str1.length; i += 1) {
                    const indicator = str1[i - 1] === str2[j - 1] ? 0 : 1;
                    track[j][i] = Math.min(
                        track[j][i - 1] + 1, // deletion
                        track[j - 1][i] + 1, // insertion
                        track[j - 1][i - 1] + indicator, // substitution
                    );
                }
            }
            return track[str2.length][str1.length];
        }
    }
}
</script>

<style scoped>

.search_bar{
    display: flex;
    align-items: center;
}

</style>