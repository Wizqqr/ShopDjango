

document.addEventListener('DOMContentLoaded', function() {
    const filterForm = document.getElementById('filter-form');
    const phoneList = document.getElementById('phone-list');

    filterForm.addEventListener('change', function(event) {
        event.preventDefault();

        const formData = new FormData(filterForm);

        fetch('{% url "phone_filter" %}', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': document.querySelector('input[name=csrfmiddlewaretoken]').value
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.html) {
                phoneList.innerHTML = data.html;
            } else {
                console.error('Error filtering phones:', data.errors);
            }
        })
        .catch(error => console.error('Error:', error));
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const comments = document.querySelectorAll('.comment-text');

    function fadeInComments() {
        comments.forEach(function(comment, index) {
            const commentPosition = comment.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;

            if (commentPosition < windowHeight) {
                comment.style.opacity = 1;
                comment.style.transition = 'opacity 0.5s ease ' + (index * 0.2) + 's';
            }
        });
    }

    function fadeOutComments() {
        comments.forEach(function(comment) {
            comment.style.opacity = 0;
        });
    }

    window.addEventListener('scroll', function() {
        if (window.scrollY > 100) {
            fadeInComments();
        } else {
            fadeOutComments();
        }
    });

    fadeInComments(); // Trigger the animation for comments already in view
});
// Пример анимации с использованием JavaScript
const phoneItems = document.querySelectorAll('.phone-item');

phoneItems.forEach((item, index) => {
    item.style.transitionDelay = `${index * 0.1}s`; // Задержка анимации для каждого элемента
    item.style.opacity = 0; // Начальное значение непрозрачности

    // Задержка для анимации появления элемента
    setTimeout(() => {
        item.style.opacity = 1;
    }, 500 + index * 100); // Добавление задержки для последовательного появления элементов
});
