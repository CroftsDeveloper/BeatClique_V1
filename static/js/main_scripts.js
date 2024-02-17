document.addEventListener("DOMContentLoaded", function() {
    // Smooth transition effect for buttons
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

    // Smooth transition effect for other buttons
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

    // Animation for logo on mouse hover
    const logo = document.getElementById('logo');
    if (logo) {
        logo.addEventListener('mouseenter', function() {
            this.style.transition = 'transform 1s cubic-bezier(0.68, -0.55, 0.27, 1.55)';
            this.style.transform = 'rotate(360deg) scale(1.2)';
        });
        logo.addEventListener('mouseleave', function() {
            this.style.transition = 'transform 0.5s ease-in-out';
            this.style.transform = 'rotate(0deg) scale(1)';
        });
    }

    // Animation for Sound Kits link
    const soundKitsLink = document.querySelector('.sound-kits-link');
    if (soundKitsLink) {
        soundKitsLink.addEventListener('mouseenter', function() {
            this.style.transition = 'transform 0.5s ease-in-out';
            this.style.transform = 'scale(1.1)';
        });
        soundKitsLink.addEventListener('mouseleave', function() {
            this.style.transition = 'transform 0.5s ease-in-out';
            this.style.transform = 'scale(1)';
        });
    }

    // Animation for testimonial cards
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

    // Pulsating animation for price tag
    const priceTag = document.getElementById('price-badge');
    if (priceTag) {
        pulsate(priceTag);
    }
});

// Function for pulsating animation
function pulsate(element) {
    let scale = 1;
    const interval = setInterval(function() {
        scale = scale === 1 ? 1.1 : 1;
        element.style.transform = `scale(${scale})`;
    }, 200);
    element.dataset.interval = interval; // Store interval ID
}

// Animation for order history icon
const orderHistoryIcon = document.getElementById('order-history-icon');
if (orderHistoryIcon) {
    let clockwiseInterval;
    let counterclockwiseInterval;

    orderHistoryIcon.addEventListener('mouseenter', function() {
        setTimeout(function() {
            clockwiseInterval = setInterval(rotateClockwise, 1000);
        }, 250);
        setTimeout(function() {
            counterclockwiseInterval = setInterval(rotateCounterclockwise, 1000);
        }, 750);
    });

    orderHistoryIcon.addEventListener('mouseleave', function() {
        clearInterval(clockwiseInterval);
        clearInterval(counterclockwiseInterval);
        orderHistoryIcon.style.transition = 'transform 1s linear';
        orderHistoryIcon.style.transform = 'rotate(0deg)';
    });
}

function rotateClockwise() {
    orderHistoryIcon.style.transition = 'transform 1s linear';
    orderHistoryIcon.style.transform = 'rotate(10deg)';
}

function rotateCounterclockwise() {
    orderHistoryIcon.style.transition = 'transform 1s linear';
    orderHistoryIcon.style.transform = 'rotate(-10deg)';
}
