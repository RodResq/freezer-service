export function initSnowFlake() {
    const container = document.querySelector('.snowfall-container');
    const snowflakeChars = ['❄', '❅', '❆', '❉', '❋', '❊', '•', '*', '·'];
    const snowflakeCount = 150;
    
    for (let i = 0; i < snowflakeCount; i++) {
        createSnowflake();
    }
    
    function createSnowflake() {
        const snowflake = document.createElement('div');
        snowflake.className = 'snowflake';
        snowflake.textContent = snowflakeChars[Math.floor(Math.random() * snowflakeChars.length)];
        
        const startPositionX = Math.random() * window.innerWidth;
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
            snowflake.remove();
            createSnowflake();
        }, (animationDuration + animationDelay) * 1000);
    }
}