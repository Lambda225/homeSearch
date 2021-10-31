var element = document.querySelector('.dessus >img')

element.addEventListener('click',function(){
    menu = document.querySelector('.vol')
    menu.classList.add('visible')
})

var element = document.querySelector('.vol > img')

element.addEventListener('click',function(){
    menu = document.querySelector('.vol')
    menu.classList.remove('visible')
})