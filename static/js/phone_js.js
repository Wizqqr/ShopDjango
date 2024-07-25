// Файл phone_js.js
document.addEventListener('DOMContentLoaded', function() {
    const commentForm = document.getElementById('comment-form');
    const commentsSection = document.querySelector('.comments-section');

    commentForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(commentForm);
        const url = commentForm.dataset.url;

        fetch(url, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': document.querySelector('input[name=csrfmiddlewaretoken]').value
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.text) {
                const commentText = document.createElement('p');
                commentText.classList.add('comment-text');
                commentText.textContent = data.text;

                // Добавляем новый комментарий с анимацией
                commentsSection.appendChild(commentText);
                setTimeout(() => {
                    commentText.classList.add('show');
                }, 100); // Даем небольшую задержку перед добавлением класса

                // Очистка формы после успешной отправки
                commentForm.reset();
            } else {
                console.error('Error creating comment:', data.errors);
            }
        })
        .catch(error => console.error('Error:', error));
    });
});


document.addEventListener('DOMContentLoaded', function () {
    const phoneListContainer = document.getElementById('phone-list');

    fetch('/api/phones/')
        .then(response => response.json())
        .then(data => {
            phoneListContainer.innerHTML = '';
            data.forEach(phone => {
                const phoneItem = document.createElement('li');
                phoneItem.className = 'phone-item';

                const phoneImage = document.createElement('img');
                phoneImage.className = 'phone-image';
                phoneImage.src = phone.image;
                phoneItem.appendChild(phoneImage);

                const phoneText = document.createElement('div');
                phoneText.className = 'phone_text';

                const phoneTitle = document.createElement('h2');
                phoneTitle.className = 'phone-title';
                phoneTitle.textContent = phone.title;
                phoneText.appendChild(phoneTitle);

                const phoneDescription = document.createElement('div');
                phoneDescription.className = 'phone-description';

                const phonePrice = document.createElement('p');
                phonePrice.className = 'phone-price';
                phonePrice.textContent = `$${phone.price_for_first}.00`;
                phoneDescription.appendChild(phonePrice);

                const phoneStock = document.createElement('p');
                phoneStock.className = 'phone-stock';
                phoneStock.textContent = phone.in_stock ? 'В наличии' : 'Нет в наличии';
                phoneDescription.appendChild(phoneStock);

                const phoneDetailLink = document.createElement('a');
                phoneDetailLink.className = 'phone-detail-link';
                phoneDetailLink.href = `/phone_list/${phone.id}/`;
                phoneDetailLink.textContent = 'Подробнее';
                phoneDescription.appendChild(phoneDetailLink);

                phoneText.appendChild(phoneDescription);
                phoneItem.appendChild(phoneText);

                phoneListContainer.appendChild(phoneItem);
            });
        })
        .catch(error => console.error('Error fetching phone data:', error));
});
