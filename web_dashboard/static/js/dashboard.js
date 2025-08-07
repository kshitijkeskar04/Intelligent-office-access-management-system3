$(document).ready(function() {
    function updateDashboard() {
        $.get('/api/access-logs', function(data) {
            let logsHtml = '';
            data.forEach(log => {
                logsHtml += `
                    <tr>
                        <td>${new Date(log.timestamp).toLocaleString()}</td>
                        <td>${log.employee_id}</td>
                        <td class="status-${log.status}">${log.status}</td>
                        <td>${Math.round(log.confidence * 100)}%</td>
                    </tr>
                `;
            });
            $('#access-logs').html(logsHtml);
        });

        $.get('/api/stats', function(stats) {
            $('#total-employees').text(stats.total_employees);
            $('#today-access').text(`${stats.today_granted} granted / ${stats.today_denied} denied`);
        });
    }

    updateDashboard();
    setInterval(updateDashboard, 5000);
});