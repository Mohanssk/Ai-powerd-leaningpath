const API_BASE = 'http://localhost:5000';

function showSection(section) {
    document.querySelectorAll('.section').forEach(s => s.classList.add('hidden'));
    document.getElementById(section).classList.remove('hidden');

    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.classList.remove('bg-blue-100', 'text-blue-700');
        btn.classList.add('text-gray-700');
    });
    event.target.classList.add('bg-blue-100', 'text-blue-700');
    event.target.classList.remove('text-gray-700');
}

function setSkill(skill) {
    document.getElementById('skillInput').value = skill;
    generateRoadmap();
}

async function generateRoadmap() {
    const skill = document.getElementById('skillInput').value.trim();

    if (!skill) {
        alert('Please enter a skill');
        return;
    }

    document.getElementById('roadmapResult').classList.add('hidden');
    document.getElementById('loadingRoadmap').classList.remove('hidden');

    try {
        const response = await fetch(`${API_BASE}/generate`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ skill })
        });

        const data = await response.json();

        if (data.error) {
            alert(data.error);
            document.getElementById('loadingRoadmap').classList.add('hidden');
            return;
        }

        displayRoadmap(data.roadmap);
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to generate roadmap. Make sure the backend is running.');
    } finally {
        document.getElementById('loadingRoadmap').classList.add('hidden');
    }
}

function displayRoadmap(roadmap) {
    const container = document.getElementById('roadmapNodes');
    container.innerHTML = '';

    roadmap.nodes.forEach((node, index) => {
        const nodeEl = document.createElement('div');
        nodeEl.className = 'node bg-gradient-to-br from-blue-50 to-blue-100 border-2 border-blue-300 rounded-lg p-4 cursor-pointer hover:shadow-lg';
        nodeEl.innerHTML = `
            <div class="flex items-center justify-between">
                <div class="flex items-center space-x-3">
                    <span class="flex items-center justify-center w-8 h-8 bg-blue-600 text-white rounded-full font-semibold text-sm">${index + 1}</span>
                    <span class="font-semibold text-gray-800">${node}</span>
                </div>
                <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                </svg>
            </div>
        `;
        nodeEl.onclick = () => showNodeDetails(node);
        container.appendChild(nodeEl);
    });

    document.getElementById('roadmapResult').classList.remove('hidden');
}

async function showNodeDetails(node) {
    document.getElementById('modalTitle').textContent = node;
    document.getElementById('modalContent').innerHTML = '<div class="loading mx-auto"></div>';
    document.getElementById('modalCerts').innerHTML = '';
    document.getElementById('modal').classList.remove('hidden');

    try {
        const [explainRes, certsRes] = await Promise.all([
            fetch(`${API_BASE}/explain`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic: node })
            }),
            fetch(`${API_BASE}/node-certs`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ node })
            })
        ]);

        const explainData = await explainRes.json();
        const certsData = await certsRes.json();

        document.getElementById('modalContent').innerHTML = `
            <div class="prose max-w-none">
                <div class="whitespace-pre-wrap text-gray-700">${explainData.explanation}</div>
            </div>
        `;

        const certsContainer = document.getElementById('modalCerts');
        certsContainer.innerHTML = '<h4 class="font-semibold text-lg mb-3 text-gray-900">Free Learning Resources</h4>';

        certsData.certifications.forEach(cert => {
            const certEl = document.createElement('a');
            certEl.href = cert.url;
            certEl.target = '_blank';
            certEl.className = 'block p-4 bg-blue-50 border border-blue-200 rounded-lg hover:bg-blue-100 transition';
            certEl.innerHTML = `
                <div class="flex items-center justify-between">
                    <span class="text-blue-700 font-medium">${cert.title}</span>
                    <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path>
                    </svg>
                </div>
            `;
            certsContainer.appendChild(certEl);
        });
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('modalContent').textContent = 'Failed to load details';
    }
}

function closeModal() {
    document.getElementById('modal').classList.add('hidden');
}

async function sendMessage() {
    const input = document.getElementById('chatInput');
    const question = input.value.trim();

    if (!question) return;

    const messagesContainer = document.getElementById('chatMessages');

    const userMsg = document.createElement('div');
    userMsg.className = 'flex justify-end';
    userMsg.innerHTML = `<div class="bg-blue-600 text-white rounded-lg p-4 max-w-md">${question}</div>`;
    messagesContainer.appendChild(userMsg);

    input.value = '';

    const loadingMsg = document.createElement('div');
    loadingMsg.className = 'bg-gray-200 rounded-lg p-4 max-w-md';
    loadingMsg.innerHTML = '<div class="loading"></div>';
    messagesContainer.appendChild(loadingMsg);

    messagesContainer.scrollTop = messagesContainer.scrollHeight;

    try {
        const response = await fetch(`${API_BASE}/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question })
        });

        const data = await response.json();

        loadingMsg.remove();

        const aiMsg = document.createElement('div');
        aiMsg.className = 'bg-blue-100 rounded-lg p-4 max-w-md';
        aiMsg.innerHTML = `<p class="text-gray-800 whitespace-pre-wrap">${data.reply}</p>`;
        messagesContainer.appendChild(aiMsg);

        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    } catch (error) {
        console.error('Error:', error);
        loadingMsg.innerHTML = '<p class="text-red-600">Failed to get response</p>';
    }
}
