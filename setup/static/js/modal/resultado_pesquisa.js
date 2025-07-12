import { showNotification } from "../notifications.js";


export function initResultadoPesquisa() {
    const btnPesquisar = document.getElementById('btnPesquisar');
    
    if (!btnPesquisar) return;

    btnPesquisar.addEventListener('click', function() {
        recuperarDadosPesquisa();
    });

    const searchInput = document.querySelector('input[name="search"]');
    if (searchInput) {
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                recuperarDadosPesquisa();
            }
        });
    }

}


function construirUrlPesquisa(parametros) {
    const baseUrl = 'api/v1/estoque/buscar';

    if (Object.keys(parametros).length === 0) {
        return baseUrl;
    }

    const queryParams = new URLSearchParams();

    Object.entries(parametros).forEach(([chave, valor]) => {
        if (valor !== null && valor !== undefined && valor !== '') {
            queryParams.append(chave, valor);
        }
    });

    return `${baseUrl}?${queryParams.toString()}`;
}


function coletarParametrosPesquisa() {
    const parametros = {};

    const searchInput = document.querySelector('input[name="search"]');
    if (searchInput && searchInput.value.trim()) {
        parametros.search = searchInput.value.trim();
    }

    return parametros;

}

async function recuperarDadosPesquisa() {
    let dados = [];
    try {
        const btnPesquisar = document.getElementById('btnPesquisar');
        const textoOriginal = btnPesquisar.innerHTML;
        btnPesquisar.innerHTML = '<i class="bi bi-hourglass-split me-2"></i>Pesquisando...';
        btnPesquisar.disabled = true;

        const parametros = coletarParametrosPesquisa();

        const url = construirUrlPesquisa(parametros);

        console.log('Realizando pesquisa com parâmetros:', parametros);
        console.log('URL da requisição:', url);

        const result = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest'
            }
        })

        if (!result.ok) {
            throw new Error(`Erro HTTP ${response.status}: ${response.statusText}`)
        }
        dados = await result.json();

        if (dados.success) {
            renderizarDados(dados);
        } else {
            showNotification('Nenhum resultado encontrado!', 'warning');
            renderizarDados({pecas: []});
        }
    } catch (error) {
        console.error('Error ao recuperar os dados: ', error);
        showNotification('Erro ao realizar a pesquisa. Tente novamente.', 'error');
        renderizarDados({pecas: []});
    } finally {
        const btnPesquisar = document.getElementById('btnPesquisar');
        if (btnPesquisar) {
            btnPesquisar.innerHTML = '<i class="bi bi-search me-2"></i>Pesquisar';
            btnPesquisar.disabled = false;
        }
        console.log('Pesquisa finalizada');
    }
}


function renderizarDados(dados) {
    const modal = document.getElementById('resultadoPesquisaModal');
    if (!modal) return;
    
    const modalInstance = new bootstrap.Modal(modal);
    modalInstance.show();
    
    const bodyResultadoPesquisa = document.getElementById('body-resultado-pesquisa');    
    if (!bodyResultadoPesquisa) return;

    if (!dados || !dados['pecas'] || dados['pecas'].length === 0) {
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
                <td>${escapeHtml(peca.codigo || 'N/A')}</td>
                <td>${escapeHtml(peca.nome || 'N/A')}</td>
                <td>
                    <div class="color-indicator d-inline-flex" 
                        style="background-color:${escapeHtml(peca.id_local_armazenamento__cor_referencia)}">
                    </div>
                    <div class="d-inline-flex" style="vertical-align: text-bottom;">Estante: ${escapeHtml(peca.id_local_armazenamento__estante || 'N/A')} / Prateleira: ${escapeHtml(peca.id_local_armazenamento__prateleira || 'N/A')} / Setor: ${escapeHtml(peca.id_local_armazenamento__setor || 'N/A')}</div>
                </td>
                <td>${escapeHtml(peca.estoque__quantidade || 0)}</td>
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


function escapeHtml(texto) {
    if (typeof texto != 'string') return texto;

    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    }

    return texto.replace(/[&<>"']/g, function(m) { return map[m]; });
}
