document.querySelectorAll('.caption-wrapper').forEach(wrapper => {
    const title = wrapper.querySelector('.category-title');

    title.addEventListener('click', () => {
        wrapper.classList.toggle('open');
    });
});
