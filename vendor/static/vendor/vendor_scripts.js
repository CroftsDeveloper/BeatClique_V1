// JavaScript for the Vendor Dashboard Page (vendor/dashboard) 

// Highlight sound kit cards on hover for better user interaction
document.querySelectorAll('.card').forEach(card => {
  card.addEventListener('mouseover', () => {
      card.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.2)';
      card.style.transform = 'scale(1.05)';
      card.style.transition = 'transform 0.3s ease, box-shadow 0.3s ease';
  });
  card.addEventListener('mouseout', () => {
      card.style.boxShadow = '';
      card.style.transform = '';
  });
});

// Newsletter Subscription
document.addEventListener("DOMContentLoaded", function() {
  const subscribeButton = document.querySelector('#button-addon2');
  const confirmationMessage = document.querySelector('#subscription-confirmation');

  subscribeButton.addEventListener('click', function() {
      // Placeholder for subscription logic)
      setTimeout(function() {
          confirmationMessage.style.display = 'block';
      }, 1000); // Show message after 1 second (1000 milliseconds)
  });
});
