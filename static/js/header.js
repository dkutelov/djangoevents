document.addEventListener('DOMContentLoaded', function() {
    const elements = document.querySelectorAll('.dropdown-trigger');
    const options = {
        hover: true,
    }
    const instances = M.Dropdown.init(elements, options);
});