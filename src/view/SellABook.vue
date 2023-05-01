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
          congratTextMain:
            "Nós do Obes juntamente com as instituições agradecemos a sua venda! ",
          congratTextUnder:
            "Você receberá um e-mail quando alguma instituição solicitar a venda. Atente-se ao seu telefone e realize a entrega com responsabilidade!",
        },
      ],
    };
  },
};
</script>

<style>
body {
  background-color: #e9dffc;
}
</style>
