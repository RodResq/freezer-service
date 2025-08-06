export function initSnowFlake() {
    const container = document.querySelector('.snowfall-container');
    
    if (!container) {
        console.warn('Container .snowfall-container não encontrado');
        return;
    }

    const snowflakeChars = ['❄', '❅', '❆', '❉', '❋', '❊', '•', '*', '·'];
    const snowflakeCount = 150;

    for (let i = 0; i < snowflakeCount; i++) {
        createSnowflake();
    }

    function createSnowflake() {
        const snowflake = document.createElement('div');
        snowflake.className = 'snowflake';
        snowflake.textContent = snowflakeChars[Math.floor(Math.random() * snowflakeChars.length)];
        
        // Usar offsetWidth para obter a largura correta do container
        const containerWidth = container.offsetWidth;
        const startPositionX = Math.random() * (containerWidth - 20); // -20 para evitar overflow
        snowflake.style.left = startPositionX + 'px';
        
        const size = Math.random() * 1.5 + 0.5;
        snowflake.style.fontSize = size + 'em';
        snowflake.style.opacity = Math.random() * 0.8 + 0.2;
        
        const animationDuration = Math.random() * 20 + 10;
        snowflake.style.animationDuration = animationDuration + 's';
        
        const animationDelay = Math.random() * 15;
        snowflake.style.animationDelay = animationDelay + 's';
        
        container.appendChild(snowflake);
        
        setTimeout(() => {
            if (snowflake.parentNode) {
                snowflake.remove();
                createSnowflake();
            }
        }, (animationDuration + animationDelay) * 1000);
    }
}