$(document).ready(function() {
    $('#catInput').hide();
    $('#addCat').on('click', function() {
        $('#catInput').slideToggle(500);
    })
})

var addChild = function(parentId) {
    document.getElementById('id_parent').value = parentId;
}


var getChildren = function(id, parentCount) {
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
                    subCatLevel = '<i class="fas fa-chevron-right"></i>'.repeat(parentCount);
                    childDiv.innerHTML += `<div class="card card-body" id="${item.id}">
                    <a data-toggle="collapse" href="#childrenOf${item.id}" role="button" aria-expanded="false" aria-controls="childrenOf${item.id}" onclick="getChildren(${item.id}, ${parentCount + 1})"> ` + subCatLevel + ` ${item.name} 
                    </a><a href="/categories/edit/${item.id}">Edit</a>  
                    <span class="btn btn-sm btn-secondary" data-toggle="modal" data-target="#addSubCatModal" id="addCat${item.id}" onclick=addChild(${item.id})>Add One <i class="fas fa-plus"></i> </span>
                </div>
                <div class="collapse" id="childrenOf${item.id}"><span class="btn btn-success" id="addCat${id}" onclick=addChild(${id})>Add One <i class="fas fa-plus"></i> </span></div>`
                }
            })
            if (count == 0) {
                childDiv.innerHTML = `<div class="card card-body" id="childrenOf${id}">There are no subcategories to show<span class="btn btn-success" id="addCat${id}" onclick=addChild(${id})  data-toggle="modal" data-target="#addSubCatModal">Add One <i class="fas fa-plus"></i> </span>
              </div>`
            }
        }
    })    
}