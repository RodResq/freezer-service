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
        const result = await fetch('api/v1/estoque/buscar');

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
    
    const bodyResultadoPesquisa = document.getElementById('body-resultado-pesquisa');    
    if (!bodyResultadoPesquisa) return;

    if (!dados || dados['pecas'].length == 0) {
        bodyResultadoPesquisa.innerHTML = `
            <tr>
                <td colspan="5" class="text-center text-info">
                    Nenhuma peça encontrada!
                </td>
            </tr>
        `;
        return;
    }

    const pecas = dados['pecas'];

    const rows = pecas.map(peca => {
        return `
            <tr>
                <td>${peca.codigo}</td>
                <td>${peca.nome || 'N/A'}</td>
                <td>${peca.id_local_armazenamento__setor || 'N/A'}</td>
                <td>${peca.estoque__quantidade || 0}</td>
                <td>
                    <button class="btn btn-sm btn-info" title="Ver detalhes" onclick="viewPecaDetails('${peca.id}')">
                        <i class="bi bi-eye"></i>
                    </button>
                    <button class="btn btn-sm btn-success" title="Aceitar" onclick="acceptPeca('${peca.id}')">
                        <i class="bi bi-check"></i>
                    </button>
                    <button class="btn btn-sm btn-danger" title="Recusar" onclick="rejectPeca('${peca.id}')">
                        <i class="bi bi-x"></i>
                    </button>
                </td>
            </tr>
        `;

    }).join('');

    bodyResultadoPesquisa.innerHTML = rows;

}

