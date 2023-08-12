// profile.js
document.addEventListener('DOMContentLoaded', function () {
    const profileModal = document.getElementById('profileModal');
    const profileLink = document.querySelector('.nav__link.profile');

    // Open modal when clicking on "Profile" link
    profileLink.addEventListener('click', function (event) {
        event.preventDefault();
        profileModal.style.display = 'block';
    });

    // Close modal when clicking outside of it
    window.addEventListener('click', function (event) {
        if (event.target === profileModal) {
            profileModal.style.display = 'none';
        }
    });
});