<template>
  <section class="container">
    <profileHeader :imageUrl="imageUrl"></profileHeader>
  </section>
</template>

<script>

import profileHeader from '@/components/profile/HeaderInfo.vue'

export default {
name:  'ProfilePage',
components:{
profileHeader
},
data() {
    return {
      imageUrl: 'https://conteudo.imguol.com.br/c/entretenimento/80/2017/04/25/a-atriz-zoe-saldana-como-neytiri-em-avatar-1493136439818_v2_1x1.jpg',
    };
  }
}
</script>

<style>
body{
  background-color: #F9F2FF;
}
</style>