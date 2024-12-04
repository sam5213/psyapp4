document.getElementById('bookingForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const formData = new FormData(this);
    fetch('/book', {
        method: 'POST', // Убедитесь, что метод соответствует маршруту на сервере
        body: formData
    }).then(response => response.json())
      .then(data => alert(`Вы успешно записались на консультацию!`))
      .catch(error => console.error('Ошибка:', error));
});

document.getElementById('cancellationForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const formData = new FormData(this);
    fetch('/cancel', {
        method: 'DELETE', // Предположим, что маршрут /cancel ожидает DELETE запрос
        body: formData
    }).then(response => response.json())
      .then(data => alert(`Ваша консультация была отменена.`))
      .catch(error => console.error('Ошибка:', error));
});
