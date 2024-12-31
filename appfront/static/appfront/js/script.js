// Copy button functionality
document.querySelector('.copy-button').addEventListener('click', function() {
    const textToCopy = document.querySelector('.copy-text').textContent;
    navigator.clipboard.writeText(textToCopy).then(() => {
        const originalText = this.textContent;
        this.textContent = 'Wait';
        setTimeout(() => {
            this.textContent = originalText;
        }, 1500);
    }).catch(err => {
        console.error('Failed to copy text:', err);
        alert('Failed to copy text to clipboard');
    });
});

// QR code button functionality
const modal = document.getElementById('qrModal');
const qrButton = document.querySelector('.qr-button');
const closeModal = document.querySelector('.close-modal');

qrButton.addEventListener('click', function() {
    const textToShow = document.querySelector('.view-text').innerHTML;
    document.getElementById('qrCodeText').innerHTML = textToShow;
    modal.style.display = 'flex';
});

closeModal.addEventListener('click', function() {
    modal.style.display = 'none';
});

window.addEventListener('click', function(event) {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});