document.querySelector('.close').addEventListener('click',
function() {
    document.querySelector('.bg-modal').style.display = 'none';

});
$(document).on('click','#buttonPop',
function() {
    document.querySelector('.bg-modal').style.display = 'flex';
});


document.querySelector('.close_text').addEventListener('click',
function() {
    document.querySelector('.bg-modal_text').style.display = 'none';

});
$(document).on('click','#buttonPop_text',
function() {
    document.querySelector('.bg-modal_text').style.display = 'flex';
});


//--------------------------------------------------------------

document.querySelector('.close2').addEventListener('click',
function() {
    document.querySelector('.bg-modal2').style.display = 'none';

});
$(document).on('click','#buttonPop2',
function() {
    document.querySelector('.bg-modal2').style.display = 'flex';
});