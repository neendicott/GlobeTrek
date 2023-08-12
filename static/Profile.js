// Get references to the modal and its content
const profileModal = document.getElementById('profileModal');
const modalContent = profileModal.querySelector('.modal-content');

// Get references to the button or element that opens the modal
const openProfileButton = document.getElementById('openProfileButton');

// Function to open the modal
function openModal() {
    profileModal.style.display = 'block';
}

// Function to close the modal
function closeModal() {
    profileModal.style.display = 'none';
}

// Add event listener to open the modal
openProfileButton.addEventListener('click', openModal);

// Add event listener to close the modal when clicking outside the content
window.addEventListener('click', (event) => {
    if (event.target === profileModal) {
        closeModal();
    }
});

// Add event listener to close the modal when pressing the Escape key
window.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
        closeModal();
    }

