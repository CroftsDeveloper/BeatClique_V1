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


