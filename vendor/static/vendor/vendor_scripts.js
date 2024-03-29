// Wait for the DOM content to be fully loaded
document.addEventListener("DOMContentLoaded", function() {

    // Add smooth transition effect to the Explore button
    var exploreButton = document.querySelector('.btn-primary');
  
    if (exploreButton) {
        exploreButton.addEventListener('mouseenter', function() {
            this.style.transition = 'transform 0.2s ease-in-out';
            this.style.transform = 'scale(1.05)';
        });
    
        exploreButton.addEventListener('mouseleave', function() {
            this.style.transition = 'transform 0.2s ease-in-out';
            this.style.transform = 'scale(1)';
        });
    }
  
    // Add smooth transition effect to the Register button
    var registerButton = document.querySelector('.btn-secondary');
  
    if (registerButton) {
        registerButton.addEventListener('mouseenter', function() {
            this.style.transition = 'transform 0.2s ease-in-out';
            this.style.transform = 'scale(1.05)';
        });
    
        registerButton.addEventListener('mouseleave', function() {
            this.style.transition = 'transform 0.2s ease-in-out';
            this.style.transform = 'scale(1)';
        });
    }
  
    // Select the logo container by its id
    var logoContainer = document.getElementById('logo-container');
  
    if (logoContainer) {
        // Add event listener for mouse entering the logo container area
        logoContainer.addEventListener('mouseenter', function() {
            // Apply a rotation effect to the logo when mouse enters
            var logo = this.querySelector('.navbar-logo');
            if (logo) {
                logo.style.transition = 'transform 0.5s ease-in-out';
                logo.style.transform = 'rotate(10deg)';
            }
        });
    
        // Add event listener for mouse leaving the logo container area
        logoContainer.addEventListener('mouseleave', function() {
            // Revert the rotation back to its original state when mouse leaves
            var logo = this.querySelector('.navbar-logo');
            if (logo) {
                logo.style.transition = 'transform 0.5s ease-in-out';
                logo.style.transform = 'rotate(0deg)';
            }
        });
    }
  
});
