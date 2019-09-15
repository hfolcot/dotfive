$(document).ready(function() {
    $('#catInput').hide();
    $('#addCat').on('click', function() {
        $('#catInput').slideToggle(500);
    })
    $('.catChildToggle').on('click', function() {
        var parent = parseInt($(this).attr('id'));
        getChildren(parent);
    })
})

var getChildren = function(id) {
    $.ajax({
        type: 'GET',
        url: '/categories/api/categories/?format=json',
        success: function(data) {
            var childDiv = document.getElementById('childrenOf' + id)
            childDiv.innerHTML = ``;
            var count = 0
            data.forEach(function(item) {
                if(item.parent === id) {
                    count++;
                    childDiv.innerHTML += `<div class="card card-body" id="${item.id}">
                    <a data-toggle="collapse" href="#childrenOf${item.id}" role="button" aria-expanded="false" aria-controls="childrenOf${item.id}" onclick="getChildren(${item.id})"><i class="fas fa-chevron-right"></i> ${item.name} <i class="fas fa-chevron-down"></i>
                    </a>  
                </div>
                <div class="collapse" id="childrenOf${item.id}"></div>`
                }
            })
            if (count == 0) {
                childDiv.innerHTML = `<div class="card card-body">There are no subcategories to show</div>`
            }
        }
    })    
}