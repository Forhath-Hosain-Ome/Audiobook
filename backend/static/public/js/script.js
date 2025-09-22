const dropArea = document.getElementById('dropArea');
const fileInput = document.getElementById('fileInput');
const fileName = document.getElementById('fileName');
const progressBar = document.getElementById('progressBar');
const statusText = document.getElementById('statusText');
const processBtn = document.querySelector('.process-btn');
const audioControls = document.getElementById('audioControls');
const audioPlayer = document.getElementById('audioPlayer');
const audioName = document.getElementById('audioName');

// Event Listeners
dropArea.addEventListener('click', () => {
    fileInput.click();
});

fileInput.addEventListener('change', handleFileSelect);

dropArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropArea.style.borderColor = '#6e8efb';
    dropArea.style.backgroundColor = '#eef0ff';
});

dropArea.addEventListener('dragleave', () => {
    dropArea.style.borderColor = '#a777e3';
    dropArea.style.backgroundColor = '#f8f9ff';
});

dropArea.addEventListener('drop', (e) => {
    e.preventDefault();
    dropArea.style.borderColor = '#a777e3';
    dropArea.style.backgroundColor = '#f8f9ff';
    
    if (e.dataTransfer.files.length) {
        fileInput.files = e.dataTransfer.files;
        handleFileSelect();
    }
});

processBtn.addEventListener('click', processPDF);

// Functions
function handleFileSelect() {
    if (fileInput.files.length) {
        const file = fileInput.files[0];
        if (file.type === 'application/pdf') {
            fileName.textContent = file.name;
            statusText.textContent = 'File selected. Click "Process PDF" to continue.';
        } else {
            statusText.textContent = 'Please select a PDF file.';
            fileInput.value = '';
            fileName.textContent = 'No file selected';
        }
    }
}

function processPDF() {
    if (!fileInput.files.length) {
        statusText.textContent = 'Please select a PDF file first.';
        return;
    }
    
    // Simulate processing
    statusText.textContent = 'Processing PDF...';
    progressBar.style.width = '30%';
    
    setTimeout(() => {
        progressBar.style.width = '70%';
        statusText.textContent = 'Extracting text...';
    }, 1500);
    
    setTimeout(() => {
        progressBar.style.width = '90%';
        statusText.textContent = 'Generating audio...';
    }, 3000);
    
    setTimeout(() => {
        progressBar.style.width = '100%';
        statusText.textContent = 'Complete!';
        
        // Show audio player
        audioControls.style.display = 'flex';
        audioPlayer.src = 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3'; // Sample audio
        audioName.textContent = 'Converted: ' + fileInput.files[0].name.replace('.pdf', '.mp3');
        
        // Update step indicator
        document.querySelectorAll('.step')[2].classList.add('completed');
    }, 4500);
}