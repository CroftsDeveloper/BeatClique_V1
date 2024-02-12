document.addEventListener("DOMContentLoaded", function() {
    // Add smooth transition effect to the Explore button
    const exploreButton = document.querySelector('.btn-primary');

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
    const registerButton = document.querySelector('.btn-secondary');

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

    // Select the logo element by its id
    const logo = document.getElementById('logo');

    if (logo) {
        // Add event listener for mouse entering the logo area
        logo.addEventListener('mouseenter', function() {
            // Apply a full spin and scale up effect to the logo when mouse enters
            this.style.transition = 'transform 1s cubic-bezier(0.68, -0.55, 0.27, 1.55)';
            this.style.transform = 'rotate(360deg) scale(1.2)';
        });

        // Add event listener for mouse leaving the logo area
        logo.addEventListener('mouseleave', function() {
            // Revert the rotation and scale back to their original states when mouse leaves
            this.style.transition = 'transform 0.5s ease-in-out';
            this.style.transform = 'rotate(0deg) scale(1)';
        });
    }

    // Select the Sound Kits link element
    const soundKitsLink = document.querySelector('.sound-kits-link');

    if (soundKitsLink) {
        // Add event listener for mouse entering the Sound Kits link area
        soundKitsLink.addEventListener('mouseenter', function() {
            // Apply a scale-up effect to the link when mouse enters
            this.style.transition = 'transform 0.5s ease-in-out';
            this.style.transform = 'scale(1.1)';
        });

        // Add event listener for mouse leaving the Sound Kits link area
        soundKitsLink.addEventListener('mouseleave', function() {
            // Revert the scale back to its original state when mouse leaves
            this.style.transition = 'transform 0.5s ease-in-out';
            this.style.transform = 'scale(1)';
        });
    }

    // Select all testimonial cards
    const testimonialCards = document.querySelectorAll('.testimonials .card');

    testimonialCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transition = 'transform 0.3s ease-in-out';
            this.style.transform = 'scale(1.05) rotate(5deg)';
        });

        card.addEventListener('mouseleave', function() {
            this.style.transition = 'transform 0.3s ease-in-out';
            this.style.transform = 'scale(1) rotate(0deg)';
        });
    });

   // Select the price tag element by its ID
   const priceTag = document.getElementById('price-badge');

   if (priceTag) {
       // Start the pulsating animation
       pulsate(priceTag);
   }
});

// Function to apply pulsating animation to an element
function pulsate(element) {
   let scale = 1;
   const interval = setInterval(function() {
       scale = scale === 1 ? 1.1 : 1;
       element.style.transform = `scale(${scale})`;
   }, 200);
   element.dataset.interval = interval; // Store interval ID in a custom attribute
}

// JS for register.html

