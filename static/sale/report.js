var date_range = null;
var date_now = new moment().format('YYYY-MM-DD');

function generate_report() {
    var parameters = {
        'action': 'report',
        'start_date': '2023-01-01',
        'end_date': '2023-02-18',
    };

    if (date_range !== null) {
        parameters['start_date'] = date_range.startDate.format('YYYY-MM-DD');
        parameters['end_date'] = date_range.endDate.format('YYYY-MM-DD');
    }

    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: parameters,
            dataSrc: ""
        },
        order: false,
        paging: false,
        ordering: false,
        info: false,
        searching: false,
        dom: 'Bfrtip',
    });
}


$(function () {
    $('input[name="date_ranger"]').daterangepicker({
        locale : {
            format: 'YYYY-MM-DD',
        }
    }).on('apply.daterangepicker', function(ev, picker) {
        date_range = picker;
        console.log(picker.startDate.format('DD/MM/YYYY') + ' - ' + picker.endDate.format('DD/MM/YYYY'));
    });

    generate_report()
});

