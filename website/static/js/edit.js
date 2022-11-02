
    function editBio(){
        const bio = document.getElementById("bio");
        const edit_button = document.getElementById("edit-button");
        edit_button.innerText = 'Done'
        bio.contentEditable = true;
        bio.style.backgroundColor = "#dddbdb";
        edit_button.addEventListener("click", function(){
        bio.contentEditable = false;
        bio.style.backgroundColor = "white";
        edit_button.innerText = 'Edit'
        }
 )


    }
