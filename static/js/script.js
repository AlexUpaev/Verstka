const modal  = document.querySelector('.modal');
const buttonCart = document.querySelector('.button__cart');
const buttonClosed = document.querySelector('.button--closed');
const cancelButton = document.querySelector('.cancelButton');

buttonCart.addEventListener('click', toggleModal);
buttonClosed.addEventListener('click', toggleModal);
cancelButton.addEventListener('click', toggleModal);

function toggleModal() {
    modal.classList.toggle('open');
}