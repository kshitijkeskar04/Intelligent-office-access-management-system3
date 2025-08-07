$(document).ready(function() {
    $('#snapshot-btn').click(function() {
        $.post('/api/snapshot', function(response) {
            alert(`Snapshot saved: ${response.filename}`);
        });
    });
});