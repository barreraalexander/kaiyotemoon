<script setup>
import HeaderNav from '@/components/navbars/HeaderNav.vue';
import FooterNav from '@/components/navbars/FooterNav.vue';
</script>

<template>
  <section id="MainAppSection">
    <HeaderNav/>
    <main>
      <router-view/>
    </main>
    <FooterNav/>
  </section>
</template>

<style lang="scss">
@import "@/assets/scss/base/base.scss";
@import "@/assets/scss/base/typography.scss";
</style>
