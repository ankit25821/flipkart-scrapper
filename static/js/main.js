$(document).ready(function () {
    $('#hiddenTable').DataTable({
        dom: 'Bfrtip',
        buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print'
        ]
    });
});

// $("#buttons-copy").on("click", function () {
//     $('.buttons-copy').click();
//     alert("Copied!");
// });

$("#buttons-csv").on("click", function () {
    $('.buttons-csv').click();
});

$("#buttons-excel").on("click", function () {
    $('.buttons-excel').click();
});

$("#buttons-pdf").on("click", function () {
    $('.buttons-pdf').click();
});

$("#buttons-print").on("click", function () {
    $('.buttons-print').click();
});

// buttons-copy
// buttons-csv
// buttons-excel
// buttons-pdf
// buttons-print