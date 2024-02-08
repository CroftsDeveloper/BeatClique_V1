// Wait for the DOM content to be fully loaded
document.addEventListener("DOMContentLoaded", function() {

    // Add smooth transition effect to the Explore button
    const exploreButton = document.querySelector('.btn-primary');

    exploreButton.addEventListener('mouseenter', function() {
        this.style.transition = 'transform 0.2s ease-in-out';
        this.style.transform = 'scale(1.05)';
    });

    exploreButton.addEventListener('mouseleave', function() {
        this.style.transition = 'transform 0.2s ease-in-out';
        this.style.transform = 'scale(1)';
    });

    // Add smooth transition effect to the Register button
    const registerButton = document.querySelector('.btn-secondary');

    registerButton.addEventListener('mouseenter', function() {
        this.style.transition = 'transform 0.2s ease-in-out';
        this.style.transform = 'scale(1.05)';
    });

    registerButton.addEventListener('mouseleave', function() {
        this.style.transition = 'transform 0.2s ease-in-out';
        this.style.transform = 'scale(1)';
    });

});
