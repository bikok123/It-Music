$(document).on("click", ".m", function () {
     let id = $(this).attr('id');
     $("#delete_id").val( id );
     // As pointed out in comments,
     // it is unnecessary to have to manually call the modal.
     // $('#addBookDialog').modal('show');
});