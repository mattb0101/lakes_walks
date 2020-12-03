$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.dropdown-trigger').dropdown({hover: false});
    $('.collapsible').collapsible();
    $('.fixed-action-btn').floatingActionButton({direction: 'left', hoverEnabled: false});
    // Resize comment and texzt area when typed in
    $('#user_comment').val();
    M.textareaAutoResize($('#user_comment'));
});
