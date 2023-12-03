<!-- Generate Report -->
    function generatePDF() {
    html2pdf(document.getElementById('pdfContainer')).then(function(canvas) {
        var pdf = new jsPDF('l', 'mm', 'a4');
        pdf.addImage(canvas.toDataURL('image/png'), 'PNG', 10, 10, 280, 200);
        pdf.rotate(90);
        pdf.save('generated-report.pdf');
    });
}
