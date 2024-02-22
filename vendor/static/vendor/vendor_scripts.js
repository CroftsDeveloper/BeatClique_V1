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
  
    // Select the logo container by its id
    const logoContainer = document.getElementById('logo-container');
  
    // Add event listener for mouse entering the logo container area
    logoContainer.addEventListener('mouseenter', function() {
        // Apply a rotation effect to the logo when mouse enters
        const logo = this.querySelector('.navbar-logo');
        logo.style.transition = 'transform 0.5s ease-in-out';
        logo.style.transform = 'rotate(10deg)';
    });
  
    // Add event listener for mouse leaving the logo container area
    logoContainer.addEventListener('mouseleave', function() {
        // Revert the rotation back to its original state when mouse leaves
        const logo = this.querySelector('.navbar-logo');
        logo.style.transition = 'transform 0.5s ease-in-out';
        logo.style.transform = 'rotate(0deg)';
    });
  
  });
  