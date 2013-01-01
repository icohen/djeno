$(function(){
    init();
});

function init(){
    $.get('/api/v1/person', function ( data ){
       var familyTree = data.objects;
       initFamilyTree( familyTree );
    });
};