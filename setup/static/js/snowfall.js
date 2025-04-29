/**
 * Snowfall Effect - jQuery 3.7.1 version
 * Creates a winter-themed snowfall animation effect
 */
$(document).ready(function() {
    // Create the container for the snowflakes
    const $snowfallContainer = $('<div>').addClass('snowfall-container');
    $('body').prepend($snowfallContainer);
    
    // Configuration for the snowflakes
    const totalSnowflakes = 150;
    const snowflakeSymbols = ['❅', '❆', '❄', '✻', '✼', '❉', '❋', '❊', '•'];
    
    // Create initial snowflakes
    for (let i = 0; i < totalSnowflakes; i++) {
        createSnowflake();
    }
    
    // Function to create a single snowflake
    function createSnowflake() {
        // Create snowflake element
        const $snowflake = $('<div>').addClass('snowflake');
        
        // Choose a random symbol for the flake
        const symbol = snowflakeSymbols[Math.floor(Math.random() * snowflakeSymbols.length)];
        $snowflake.html(symbol);
        
        // Set random initial position and properties
        const startPositionX = Math.random() * $(window).width();
        const startOpacity = 0.5 + Math.random() * 0.5;
        
        // Set random speed and size
        const duration = 10 + Math.random() * 20;
        const snowflakeSize = 7 + Math.random() * 18;
        
        // Apply styles using jQuery
        $snowflake.css({
            'left': startPositionX + 'px',
            'opacity': startOpacity,
            'font-size': snowflakeSize + 'px',
            'animation-duration': duration + 's',
            'animation-delay': (Math.random() * 5) + 's'
        });
        
        // Add to container
        $snowfallContainer.append($snowflake);
        
        // Remove and recreate snowflake after animation completes
        setTimeout(function() {
            $snowflake.remove();
            createSnowflake();
        }, duration * 1000);
    }
});