import { showNotification } from "../notifications.js";

export function initResultadoPesquisa() {
    const btnPesquisar = document.getElementById('btnPesquisar');
    
    if (!btnPesquisar) return;

    btnPesquisar.addEventListener('click', function() {
        recuperarDadosPesquisa();
    });

}

async function recuperarDadosPesquisa() {
    let dados = [];
    try {
        const result = await fetch('api/recuperar_dados_pesquisa');

        if (!result.ok) {
            throw new Error(`Erro HTTP ${response.status}: ${response.statusText}`)
        }
        dados = await result.json();

        if (dados.success) {
            renderizarDados(dados);
        } else {
            showNotification('Dados não encontrado!')
        }
    } catch {
        console.error('Error ao recuperar os dados');
        throw new Error('Error ao recuperar dados');
    } finally {
        console.log('Finaly executado');
    }
}


function renderizarDados(dados) {
    const modal = document.getElementById('resultadoPesquisaModal');

    if (!modal) return;

    const modalInstance = new bootstrap.Modal(modal);
    modalInstance.show();

}

