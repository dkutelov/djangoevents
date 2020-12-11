const replyButtons = Array.from(document.querySelectorAll('#comment-reply'))
const replyForms = Array.from(document.querySelectorAll('#reply'))
replyButtons.forEach(el => el.addEventListener('click', replyClickHandler));

function replyClickHandler(e) {
    const buttonEl = e.target;
    const commentId = buttonEl.dataset.comment_id;
    const currentForm = replyForms.find(f => f.dataset.comment_id === commentId);

    if ( buttonEl.textContent === 'Reply') {
        currentForm.style.display = 'block';
        e.target.textContent = 'Cancel';
    } else {
        currentForm.style.display = 'none';
        e.target.textContent = 'Reply';
    }
}