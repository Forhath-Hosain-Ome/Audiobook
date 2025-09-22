document.addEventListener('DOMContentLoaded', function() {
    const statusIndicators = document.querySelectorAll('.status-indicator');
    setInterval(() => {
        statusIndicators.forEach(indicator => {
            if (Math.random() > 0.8) {
                const dot = indicator.querySelector('.status-dot');
                if (dot.classList.contains('status-online')) {
                    dot.classList.remove('status-online');
                    dot.classList.add('status-offline');
                    indicator.querySelector('.status-text').textContent += ' (Issues)';
                } else {
                    dot.classList.remove('status-offline');
                    dot.classList.add('status-online');
                    const text = indicator.querySelector('.status-text');
                    text.textContent = text.textContent.replace(' (Issues)', '');
                }
            }
        });
    }, 5000);
});