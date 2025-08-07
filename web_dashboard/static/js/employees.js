$(document).ready(function() {
    // Load employee list
    function loadEmployees() {
        $.get('/employees', function(data) {
            let html = '';
            data.forEach(emp => {
                html += `
                    <tr>
                        <td>${emp.id}</td>
                        <td>
                            <img src="/employees/${emp.image}" class="employee-photo">
                        </td>
                        <td>
                            <button class="btn btn-sm btn-danger delete-btn" data-id="${emp.id}">
                                Delete
                            </button>
                        </td>
                    </tr>
                `;
            });
            $('#employees-table').html(html);
        });
    }

    // Add new employee
    $('#addEmployeeForm').submit(function(e) {
        e.preventDefault();
        const formData = new FormData(this);
        
        $.ajax({
            url: '/employees',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function() {
                $('#addEmployeeModal').modal('hide');
                loadEmployees();
            }
        });
    });

    // Delete employee
    $(document).on('click', '.delete-btn', function() {
        const empId = $(this).data('id');
        if (confirm(`Delete employee ${empId}?`)) {
            $.ajax({
                url: `/employees/${empId}`,
                type: 'DELETE',
                success: loadEmployees
            });
        }
    });

    loadEmployees();
});