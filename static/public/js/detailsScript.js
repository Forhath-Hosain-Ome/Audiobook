// Functionality for the management buttons
document.addEventListener('DOMContentLoaded', function() {
    // View button functionality
    const viewButtons = document.querySelectorAll('.btn-view');
    viewButtons.forEach(button => {
        button.addEventListener('click', function() {
            const card = this.closest('.pdf-card');
            const title = card.querySelector('.pdf-title').textContent;
            alert(`Viewing PDF: ${title}`);
        });
    });
    
    // Edit button functionality
    const editButtons = document.querySelectorAll('.btn-edit');
    editButtons.forEach(button => {
        button.addEventListener('click', function() {
            const card = this.closest('.pdf-card');
            const title = card.querySelector('.pdf-title').textContent;
            alert(`Editing PDF: ${title}`);
        });
    });
    
    // Delete button functionality
    const deleteButtons = document.querySelectorAll('.btn-delete');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const card = this.closest('.pdf-card');
            const title = card.querySelector('.pdf-title').textContent;
            
            if (confirm(`Are you sure you want to delete ${title}?`)) {
                card.style.opacity = '0';
                setTimeout(() => {
                    card.remove();
                    alert(`${title} has been deleted successfully.`);
                }, 300);
            }
        });
    });
});