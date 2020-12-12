 document.addEventListener("DOMContentLoaded", function (event) {
    const scrollpos = sessionStorage.getItem('scrollpos');
    const storedPath = sessionStorage.getItem('storedPath');
    const currentPath = location.pathname;
    console.log(storedPath, currentPath);
    if (scrollpos && storedPath === currentPath) {
        window.scrollTo(0, scrollpos);
        sessionStorage.removeItem('scrollpos');
    }
});

window.addEventListener("beforeunload", function (e) {
    console.log(location.href);
    sessionStorage.setItem('scrollpos', window.scrollY);
    sessionStorage.setItem('storedPath', location.pathname);
});