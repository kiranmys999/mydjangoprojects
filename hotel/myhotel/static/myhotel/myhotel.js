/*
$(document).ready(function(){
    //confirm("hello world!");
    $('#id_city').change(function(){
        //window.alert('inside select');
        $('#cityform').submit();
    });
});
*/
var ajaxform = function(){
    var formdat = $('#formcity');
    $('#id_city').on('change', function(){
    console.log('city changed');
    $.ajax({
        url: formdat.attr('action'),
        data: formdat.serialize(),
        type: 'POST',
        success: function(data){
            //console.log(".....it worked......");
            //console.log(data.formhotel);
            $('#formhotel').children('table').html(data.formhotel);

        },
        error: function(err){
            console.log("error occured" + JSON.stringify(err));
        }
    });
    });
};

$(document).ready(ajaxform);