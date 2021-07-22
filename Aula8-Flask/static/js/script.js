const items = document.querySelectorAll('.itens')

items.forEach((item)=> {
    item.addEventListener('click', () => {
        item.style.textDecoration = 'line-through'
    });
});