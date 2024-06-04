let currentPage = 1;
let projectsPerPage = 4; // Adjust the number of projects per page

function displayProjects(page) {
    const allProjects = document.querySelectorAll('.project-card');
    const totalProjects = allProjects.length;
    const maxPage = Math.ceil(totalProjects / projectsPerPage);
    currentPage = page;

    allProjects.forEach((project, index) => {
        project.style.display = 'none';
        if (index >= (page - 1) * projectsPerPage && index < page * projectsPerPage) {
            project.style.display = 'block';
        }
    });

    document.getElementById('page-number').textContent = page.toString();
}

function nextPage() {
    const totalProjects = document.querySelectorAll('.project-card').length;
    const maxPage = Math.ceil(totalProjects / projectsPerPage);
    if (currentPage < maxPage) {
        displayProjects(currentPage + 1);
    }
}

function previousPage() {
    if (currentPage > 1) {
        displayProjects(currentPage - 1);
    }
}

document.addEventListener('DOMContentLoaded', function () {
    displayProjects(1);
});
