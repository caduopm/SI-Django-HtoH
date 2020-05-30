// window.onload = function() {
//     if (window.jQuery) {  
//         // jQuery is loaded  
//         alert("Yeah!");
//     } else {
//         // jQuery is not loaded
//         alert("Doesn't Work");
//     }
// }

// Adiciona mascara nos campos com jQuery
$(document).ready(function(){
    $('#cpf').mask('000.000.000-00');
    $('#phone').mask('(99) 99999-9999');
});

// metodo mara exibir imagem escolhida
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#blah').attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    }
}