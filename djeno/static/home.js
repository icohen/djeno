$(function(){
    init();
});

function init(){
    $.ajax({'url':'/api/v1/person',
            'async': false
           })
           .done(function ( data ){
               var familyTree = data.objects;
               initFamilyTree( familyTree );
            });
};