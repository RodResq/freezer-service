export function initResultadoPesquisa() {
    const btnPesquisar = document.getElementById('btnPesquisar');
    const modal = document.getElementById('resultadoPesquisaModal');

    if (!btnPesquisar) return;

    btnPesquisar.addEventListener('click', function() {
        console.log('Entrou no modal');
        
        const modalInstance = new bootstrap.Modal(modal);
        modalInstance.show();
        
    });

}