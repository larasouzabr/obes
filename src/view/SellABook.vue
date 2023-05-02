<template>
  <multi-step-form :type="sell"></multi-step-form>
</template>

<script>
import MultiStepForm from "@/components/preview/MultiStepForm.vue";
export default {
  components: {
    MultiStepForm,
  },
  data: () => {
    return {
      sell: [
        {
          isSelling: true,
          typeofAction: "vender",
          congratTextMain: "Nós do Obes agradecemos a sua venda! ",
          congratTextUnder:
            "Você receberá um e-mail quando alguém solicitar a compra. Atente-se ao seu telefone e realize a entrega com responsabilidade!",
        },
      ],
    };
  },
};
</script>

<style scoped>
body {
  background-color: #e9dffc;
}
</style>
