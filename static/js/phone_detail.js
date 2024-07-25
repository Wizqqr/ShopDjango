// phone_detail.js
document.addEventListener('DOMContentLoaded', function() {
    const simularModels = document.querySelectorAll('.simular-model');

    simularModels.forEach(model => {
        model.addEventListener('mouseover', () => {
            model.style.transform = 'scale(1.05)';
            model.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.1)';
        });

        model.addEventListener('mouseout', () => {
            model.style.transform = 'scale(1)';
            model.style.boxShadow = 'none';
        });
    });
});
