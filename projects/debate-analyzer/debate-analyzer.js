// Simple keyword-based detection of a few logical fallacies/devices
const fallacies = [
    { name: "Ad Hominem", keywords: ["you're stupid", "you're an idiot", "attack you"] },
    { name: "Straw Man", keywords: ["so what you're saying is", "misrepresent", "distort"] },
    { name: "Slippery Slope", keywords: ["if we allow this", "next thing you know", "inevitably lead"] },
    { name: "Appeal to Authority", keywords: ["experts agree", "studies show", "according to"] },
    { name: "Overgeneralization", keywords: ["always", "never", "everyone knows"] }
];

document.getElementById('analyzeBtn').addEventListener('click', function() {
    const input = document.getElementById('debateInput').value;
    let outputHtml = '';
    let found = false;
    fallacies.forEach(fallacy => {
        fallacy.keywords.forEach(keyword => {
            if (input.toLowerCase().includes(keyword)) {
                found = true;
                outputHtml += `<div class='fallacy'><strong>${fallacy.name}:</strong> Detected keyword "${keyword}"</div>`;
            }
        });
    });
    if (!found) {
        outputHtml = '<div class="no-fallacy">No obvious fallacies detected (MVP version).</div>';
    }
    document.getElementById('output').innerHTML = outputHtml;
    // Show 'Send to Argument Helper' button after analysis
    const sendBtn = document.getElementById('sendToArgumentHelperBtn');
    sendBtn.style.display = 'inline-block';
});

// Educational popup for intro tooltip
const introTooltip = document.querySelector('#intro-section span[title]');
if (introTooltip) {
    introTooltip.addEventListener('click', function() {
        alert('A logical fallacy is an error in reasoning that weakens an argument. Common fallacies include ad hominem, straw man, slippery slope, and more.');
    });
}

// Educational popups for info icons
function addInfoPopup(id, message) {
    const el = document.getElementById(id);
    if (el) {
        el.addEventListener('click', function(e) {
            e.preventDefault();
            alert(message);
        });
    }
}
addInfoPopup('fallacyInfo', 'A logical fallacy is an error in reasoning that weakens an argument. Common fallacies include ad hominem, straw man, slippery slope, and more.');
addInfoPopup('fallacyInfo2', 'A logical fallacy is an error in reasoning that weakens an argument. Common fallacies include ad hominem, straw man, slippery slope, and more.');
addInfoPopup('validityInfo', 'Validity: An argument is valid if the conclusion logically follows from the premises, regardless of whether the premises are true.');
addInfoPopup('soundnessInfo', 'Soundness: An argument is sound if it is valid and all its premises are actually true.');

// Argument Helper logic

// --- Argument Helper Advanced Logic ---

function updatePremiseLabels() {
    const rows = document.querySelectorAll('.premise-row');
    rows.forEach((row, idx) => {
        row.querySelector('label').textContent = `Premise ${idx + 1}:`;
    });
}

document.getElementById('addPremiseBtn').addEventListener('click', function() {
    const premisesList = document.getElementById('premises-list');
    const count = premisesList.children.length + 1;
    const row = document.createElement('div');
    row.className = 'premise-row';
    row.innerHTML = `
        <label>Premise ${count}:</label>
        <input type="text" class="premise-input" required>
        <button type="button" class="remove-premise-btn">Remove</button>
        <label class="soundness-check"><input type="checkbox" class="soundness-checkbox"> Premise is true</label>
    `;
    premisesList.appendChild(row);
    updatePremiseLabels();
    // Show remove buttons if more than one premise
    document.querySelectorAll('.remove-premise-btn').forEach(btn => btn.style.display = premisesList.children.length > 1 ? '' : 'none');
});

document.getElementById('premises-list').addEventListener('click', function(e) {
    if (e.target.classList.contains('remove-premise-btn')) {
        e.target.parentElement.remove();
        updatePremiseLabels();
        const premisesList = document.getElementById('premises-list');
        document.querySelectorAll('.remove-premise-btn').forEach(btn => btn.style.display = premisesList.children.length > 1 ? '' : 'none');
    }
});

document.getElementById('checkArgumentBtn').addEventListener('click', function() {
    const premiseInputs = document.querySelectorAll('.premise-input');
    const soundnessChecks = document.querySelectorAll('.soundness-checkbox');
    const conclusion = document.getElementById('conclusion').value.trim();
    let premises = [];
    let allSound = true;
    premiseInputs.forEach((input, idx) => {
        const val = input.value.trim();
        if (val.length > 0) {
            premises.push({
                text: val,
                sound: soundnessChecks[idx].checked
            });
            if (!soundnessChecks[idx].checked) allSound = false;
        }
    });
    let output = '';
    if (premises.length < 1 || !conclusion) {
        output = '<div class="fallacy">Please enter at least one premise and a conclusion.</div>';
        document.getElementById('argumentOutput').innerHTML = output;
        return;
    }
    // Validity: is the conclusion just a restatement of a premise?
    let isRestatement = premises.some(p => p.text.toLowerCase() === conclusion.toLowerCase());
    // Check for fallacies in premises and conclusion
    let fallacyWarnings = [];
    premises.forEach((p, idx) => {
        fallacies.forEach(fallacy => {
            fallacy.keywords.forEach(keyword => {
                if (p.text.toLowerCase().includes(keyword)) {
                    fallacyWarnings.push(`<div class='fallacy'><strong>${fallacy.name} in Premise ${idx+1}:</strong> Detected keyword "${keyword}"</div>`);
                }
            });
        });
    });
    fallacies.forEach(fallacy => {
        fallacy.keywords.forEach(keyword => {
            if (conclusion.toLowerCase().includes(keyword)) {
                fallacyWarnings.push(`<div class='fallacy'><strong>${fallacy.name} in Conclusion:</strong> Detected keyword "${keyword}"</div>`);
            }
        });
    });
    if (isRestatement) {
        output += '<div class="fallacy">The conclusion is just a restatement of a premise. Try to make the conclusion a logical result of the premises.</div>';
    } else {
        output += '<div class="no-fallacy">Your argument appears <strong>valid</strong> (the conclusion is not a simple restatement).</div>';
    }
    if (fallacyWarnings.length > 0) {
        output += '<div style="margin-top:10px;"><strong>Possible fallacies detected:</strong>' + fallacyWarnings.join('') + '</div>';
    }
    if (allSound) {
        output += '<div class="no-fallacy" style="margin-top:10px;">All premises are marked as true. Your argument is <strong>sound</strong> if your premises are indeed true.</div>';
    } else {
        output += '<div class="fallacy" style="margin-top:10px;">Not all premises are marked as true. Your argument may not be sound.</div>';
    }
    output += '<div style="margin-top:10px;"><em>Tip: Make sure each premise is supported by evidence, and check for any unstated assumptions.</em></div>';
    document.getElementById('argumentOutput').innerHTML = output;
});

// --- PDF Export, Save/Load, and Examples Logic ---
// Download as PDF
function getArgumentData() {
    const premiseInputs = document.querySelectorAll('.premise-input');
    const soundnessChecks = document.querySelectorAll('.soundness-checkbox');
    const conclusion = document.getElementById('conclusion').value.trim();
    let premises = [];
    premiseInputs.forEach((input, idx) => {
        const val = input.value.trim();
        if (val.length > 0) {
            premises.push({
                text: val,
                sound: soundnessChecks[idx].checked
            });
        }
    });
    return { premises, conclusion };
}

function setArgumentData(data) {
    // Clear current premises
    const premisesList = document.getElementById('premises-list');
    premisesList.innerHTML = '';
    data.premises.forEach((p, idx) => {
        const row = document.createElement('div');
        row.className = 'premise-row';
        row.innerHTML = `
            <label>Premise ${idx+1}:</label>
            <input type="text" class="premise-input" required value="${p.text}">
            <button type="button" class="remove-premise-btn" ${data.premises.length === 1 ? 'style="display:none;"' : ''}>Remove</button>
            <label class="soundness-check"><input type="checkbox" class="soundness-checkbox" ${p.sound ? 'checked' : ''}> Premise is true</label>
        `;
        premisesList.appendChild(row);
    });
    document.getElementById('conclusion').value = data.conclusion;
    updatePremiseLabels();
    document.querySelectorAll('.remove-premise-btn').forEach(btn => btn.style.display = data.premises.length > 1 ? '' : 'none');
}

// PDF Export
if (window.jspdf === undefined) {
    var script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js';
    document.head.appendChild(script);
}
document.getElementById('downloadPdfBtn').addEventListener('click', function() {
    const { premises, conclusion } = getArgumentData();
    const doc = new window.jspdf.jsPDF();
    doc.setFontSize(16);
    doc.text('Argument Export', 10, 15);
    doc.setFontSize(12);
    premises.forEach((p, idx) => {
        doc.text(`Premise ${idx+1}: ${p.text} [${p.sound ? 'Marked true' : 'Not marked true'}]`, 10, 30 + idx*10);
    });
    doc.text(`Conclusion: ${conclusion}`, 10, 40 + premises.length*10);
    doc.save('argument.pdf');
});
// Save/Load
function getSavedArguments() {
    return JSON.parse(localStorage.getItem('savedArguments') || '[]');
}
function saveArgument() {
    const { premises, conclusion } = getArgumentData();
    const name = prompt('Enter a name for this argument:');
    if (!name) return;
    let saved = getSavedArguments();
    saved.push({ name, premises, conclusion });
    localStorage.setItem('savedArguments', JSON.stringify(saved));
    alert('Argument saved!');
}
document.getElementById('saveArgumentBtn').addEventListener('click', saveArgument);
// --- Modal Overlay and Accessibility Logic ---
const modalOverlay = document.getElementById('modalOverlay');
function showModal(modal) {
    modal.style.display = 'block';
    modalOverlay.style.display = 'block';
    // Focus first button/input in modal
    setTimeout(() => {
        const focusable = modal.querySelector('button, [tabindex]:not([tabindex="-1"])');
        if (focusable) focusable.focus();
    }, 50);
}
function hideModal(modal) {
    modal.style.display = 'none';
    modalOverlay.style.display = 'none';
}
modalOverlay.addEventListener('click', function() {
    hideModal(templatesModal);
    hideModal(document.getElementById('loadModal'));
});
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        hideModal(templatesModal);
        hideModal(document.getElementById('loadModal'));
    }
});
// --- Templates Modal Logic (updated) ---
const templates = [
    {
        name: 'Syllogism',
        description: 'A classic deductive argument: All A are B. C is A. Therefore, C is B.',
        data: {
            premises: [
                { text: 'All mammals are warm-blooded.', sound: true },
                { text: 'Whales are mammals.', sound: true }
            ],
            conclusion: 'Whales are warm-blooded.'
        }
    },
    {
        name: 'Modus Ponens',
        description: 'If A, then B. A. Therefore, B.',
        data: {
            premises: [
                { text: 'If it rains, the ground gets wet.', sound: true },
                { text: 'It is raining.', sound: true }
            ],
            conclusion: 'The ground gets wet.'
        }
    },
    {
        name: 'Modus Tollens',
        description: 'If A, then B. Not B. Therefore, not A.',
        data: {
            premises: [
                { text: 'If the alarm is set, it will ring.', sound: true },
                { text: 'The alarm did not ring.', sound: true }
            ],
            conclusion: 'The alarm was not set.'
        }
    },
    {
        name: 'Disjunctive Syllogism',
        description: 'A or B. Not A. Therefore, B.',
        data: {
            premises: [
                { text: 'Either the test is today or tomorrow.', sound: true },
                { text: 'The test is not today.', sound: true }
            ],
            conclusion: 'The test is tomorrow.'
        }
    }
];
const showTemplatesBtn = document.getElementById('showTemplatesBtn');
const templatesModal = document.getElementById('templatesModal');
const closeTemplatesModal = document.getElementById('closeTemplatesModal');
const templateListDiv = templatesModal.querySelector('.template-list');
showTemplatesBtn.addEventListener('click', function() {
    templateListDiv.innerHTML = templates.map((t, i) =>
        `<div class='template-item'>
            <strong>${t.name}</strong><br>
            <span>${t.description}</span><br>
            <button type='button' class='load-template-btn small-btn' data-tidx='${i}'>Load</button>
        </div>`
    ).join('');
    showModal(templatesModal);
});
closeTemplatesModal.addEventListener('click', function() {
    hideModal(templatesModal);
});
document.body.addEventListener('click', function(e) {
    if (templatesModal.style.display === 'block' && !templatesModal.contains(e.target) && e.target !== showTemplatesBtn && e.target !== modalOverlay) {
        hideModal(templatesModal);
    }
});
templateListDiv.addEventListener('click', function(e) {
    if (e.target.classList.contains('load-template-btn')) {
        const tidx = e.target.getAttribute('data-tidx');
        setArgumentData(templates[tidx].data);
        hideModal(templatesModal);
    }
});
// --- Enhanced Library (Load Argument) Modal (updated) ---
function updateLoadModal() {
    const modal = document.getElementById('loadModal');
    let saved = getSavedArguments();
    if (saved.length === 0) {
        modal.innerHTML = '<em>No saved arguments found.</em>';
        modal.style.display = 'block';
        return;
    }
    modal.innerHTML = '<strong>Saved Arguments:</strong><ul style="padding-left:0;">' + saved.map((a, i) =>
        `<li style='margin-bottom:10px;list-style:none;'>
            <span style='font-weight:600;'>${a.name}</span>
            <button type='button' class='load-arg-btn small-btn' data-idx='${i}'>Load</button>
            <button type='button' class='rename-arg-btn small-btn' data-idx='${i}'>Rename</button>
            <button type='button' class='delete-arg-btn small-btn' data-idx='${i}'>Delete</button>
        </li>`
    ).join('') + '</ul><button type="button" id="closeLoadModal">Close</button>';
    modal.style.display = 'block';
}
document.getElementById('loadArgumentBtn').addEventListener('click', function() {
    updateLoadModal();
    showModal(document.getElementById('loadModal'));
});
document.getElementById('loadModal').addEventListener('click', function(e) {
    let saved = getSavedArguments();
    if (e.target.classList.contains('load-arg-btn')) {
        const idx = e.target.getAttribute('data-idx');
        setArgumentData(saved[idx]);
        hideModal(document.getElementById('loadModal'));
    }
    if (e.target.classList.contains('rename-arg-btn')) {
        const idx = e.target.getAttribute('data-idx');
        const newName = prompt('Enter a new name:', saved[idx].name);
        if (newName) {
            saved[idx].name = newName;
            localStorage.setItem('savedArguments', JSON.stringify(saved));
            updateLoadModal();
        }
    }
    if (e.target.classList.contains('delete-arg-btn')) {
        const idx = e.target.getAttribute('data-idx');
        if (confirm('Delete this argument?')) {
            saved.splice(idx, 1);
            localStorage.setItem('savedArguments', JSON.stringify(saved));
            updateLoadModal();
        }
    }
    if (e.target.id === 'closeLoadModal') {
        hideModal(document.getElementById('loadModal'));
    }
});
// Examples
const examples = [
    {
        name: 'Classic Syllogism',
        premises: [
            { text: 'All humans are mortal.', sound: true },
            { text: 'Socrates is a human.', sound: true }
        ],
        conclusion: 'Socrates is mortal.'
    },
    {
        name: 'Unsound Argument',
        premises: [
            { text: 'All birds can fly.', sound: false },
            { text: 'Penguins are birds.', sound: true }
        ],
        conclusion: 'Penguins can fly.'
    },
    {
        name: 'Fallacy Example',
        premises: [
            { text: 'Everyone knows that eating carrots improves your eyesight.', sound: false }
        ],
        conclusion: 'You should eat more carrots to see better.'
    }
];
document.querySelectorAll('.example-btn').forEach((btn) => {
    btn.addEventListener('click', function() {
        const idx = parseInt(btn.getAttribute('data-example')) - 1;
        setArgumentData(examples[idx]);
    });
}); 