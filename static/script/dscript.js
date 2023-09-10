// Get references to the button, popup, and close button
document.addEventListener('DOMContentLoaded', function() {
    // Your JavaScript code here
  
const showPopupButton = document.querySelector('.btn-login');
const popup = document.getElementById('popup');
const closePopupButton = document.getElementById('closePopup');

// Show the popup when the button is clicked
showPopupButton.addEventListener('click', () => {
    popup.style.display = 'block';
    document.body.style.overflow = 'hidden'; // Prevent scrolling when the popup is open
});

// Close the popup when the close button is clicked
closePopupButton.addEventListener('click', () => {
    popup.style.display = 'none';
    document.body.style.overflow = 'auto'; // Allow scrolling again
});

});
