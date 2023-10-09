    $(document).ready(function() {
        $.getJSON('/data/sites.json', function(data) {
            var table = $('#repoTable').DataTable();
            data.forEach(function(repo) {
                var repoLink = `<a href="${repo.html_url}">${repo.name}</a>`;
                var siteLink = `<a href="https://wijnandb.github.io/${repo.name}">${repo.description}</a>`;
                var issuesLink = `<a href="${repo.html_url}/issues">${repo.open_issues_count}</a>`;
                table.row.add([repoLink, siteLink, issuesLink, repo.updated_at]);
            });
            table.draw();
        });
    });
