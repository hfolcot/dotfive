$(document).ready(function() {
    $('#catInput').hide();
    toggleTooltips();
    $('#addCat').on('click', function() {
        $('#catInput').slideToggle(500);
    })
})

var toggleTooltips = function () {
    $('[data-toggle="tooltip"]').tooltip()
  }

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
                    childDiv.innerHTML += `<div class="card card-body sub-cat-card mt-2" id="${item.id}">
                    <div class="d-flex flex-row justify-content-between mb-2"><a data-toggle="collapse" href="#childrenOf${item.id}" role="button" aria-expanded="false" aria-controls="childrenOf${item.id}" onclick="getChildren(${item.id}, ${parentCount + 1})"> ` + subCatLevel + ` ${item.name} 
                    </a>  
                    <div class="d-flex flex-row justify-content-end mb-2"><span data-toggle="tooltip" data-placement="top" title="Add a subcategory to ${item.name}"><span class="btn btn-sm btn-success mr-2" data-toggle="modal" data-target="#addSubCatModal" id="addCat${item.id}" onclick=addChild(${item.id})><i class="fas fa-plus"></i> </span></span><a class="btn btn-sm btn-info mr-2" href="/categories/edit/${item.id}" data-toggle="tooltip" data-placement="top" title="Edit or move ${item.name}"><i class="fas fa-edit"></i></a></div>
                </div>
                <div class="collapse collapse-bottom-border" id="childrenOf${item.id}"></div></div>`
                }
            })
            if (count == 0) {
                childDiv.innerHTML = `<div class="card card-body sub-cat-card mt-2" id="childrenOf${id}"><div class="d-flex flex-row justify-content-between">There are no subcategories to show<span class="btn btn-sm btn-success" id="addCat${id}" onclick=addChild(${id})  data-toggle="modal" data-target="#addSubCatModal"><i class="fas fa-plus"></i> </span></div>
              </div>`
            }
            toggleTooltips(); //Tooltip CSS will not load for newly generated elements without this
        }
    })    
}