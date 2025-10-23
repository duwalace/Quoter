// Espera o HTML carregar antes de rodar o script
document.addEventListener("DOMContentLoaded", () => {
    
    // 1. Pega as referências dos elementos HTML
    const botao = document.getElementById("nova-citacao-btn");
    const elementoCitacao = document.getElementById("citacao");
    const elementoAutor = document.getElementById("autor");

    // 2. A função que busca os dados no seu backend
    async function buscarCitacao() {
        // Mostra um feedback para o usuário
        elementoCitacao.textContent = "Carregando...";
        elementoAutor.textContent = "";

        try {
            // 3. A MÁGICA! Faz a chamada para o seu `servico_diario`
            const response = await fetch("http://127.0.0.1:5000/citacao-do-dia");

            if (!response.ok) {
                throw new Error("Não foi possível buscar a citação.");
            }

            // 4. Converte a resposta JSON em um objeto JavaScript
            const dados = await response.json();

            // 5. Atualiza o HTML com os dados recebidos
            elementoCitacao.textContent = `"${dados.texto}"`;
            elementoAutor.textContent = `— ${dados.autor}`;

        } catch (error) {
            // 6. Mostra um erro se o backend falhar (ex: se você esqueceu de ligá-lo)
            elementoCitacao.textContent = "Erro ao carregar. Tente novamente.";
            elementoAutor.textContent = error.message;
        }
    }

    // 7. Adiciona um "ouvinte" ao botão. Quando clicado, chama a função `buscarCitacao`
    botao.addEventListener("click", buscarCitacao);

    // Opcional: Carrega uma citação assim que a página abre
    // buscarCitacao();
});