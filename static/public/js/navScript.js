document.addEventListener('DOMContentLoaded', function() {
const navItems = document.querySelectorAll('.nav-item');
if (window.innerWidth <= 768) {
    navItems.forEach(item => {
        const link = item.querySelector('.nav-link');
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const dropdown = item.querySelector('.dropdown');
            if (dropdown.style.display === 'block') {
                dropdown.style.display = 'none';
            } else {
                dropdown.style.display = 'block';
            }
        });
    });
}
});