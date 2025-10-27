    const switchers = [...document.querySelectorAll('.switcher')]

    switchers.forEach(item => {
      item.addEventListener('click', function() {
        switchers.forEach(item => item.parentElement.classList.remove('is-active'))
        this.parentElement.classList.add('is-active')
      })
    })
setTimeout(function() {
    const messages = document.querySelector('.messages-container');
    if (messages) {
        messages.style.transition = 'opacity 0.5s';
        messages.style.opacity = '0';
        setTimeout(() => messages.remove(), 500);
    }
}, 3000);