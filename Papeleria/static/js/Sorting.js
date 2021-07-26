function sortTable(n,numeric = false, tableName){
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById(tableName);
    switching = true;
    //Set the sorting direction to ascending:
    dir = "asc";
    /*Make a loop that will continue until
    no switching has been done:*/
    while (switching) {
        switching = false;
        rows = table.rows;
        /*Start a loop through all table rows:*/
        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("td")[n];
            y = rows[i + 1].getElementsByTagName("td")[n];
            if(!numeric){
                if(dir=="asc"){
                    if(x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()){
                        shouldSwitch = true;
                        break;
                    }
                }
                else if(dir=="desc"){
                    if(x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()){
                        shouldSwitch = true;
                        break;
                    }
                }
            }else{
                if(dir=="asc"){
                    if(Number(x.innerHTML) > Number(y.innerHTML) ){
                        shouldSwitch = true;
                        break;
                    }
                }
                else if(dir=="desc"){
                    if(Number(x.innerHTML) < Number(y.innerHTML) ){
                        shouldSwitch = true;
                        break;
                    }
                }
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            switchcount++;
        }
        else{
            if(switchcount == 0 && dir=="asc"){
                dir = "desc";
                switching = true;
            }
        }
    }
}
$('th').on('click', function () {
    let column = $(this).data('column');
    let name = $(this).closest('table').attr('id');
    let order = $(this).data('order');
    let text = $(this).html();
    let numeric = $(this).data('numeric');
    text = text.substring(0, text.length - 1);
    if(order === 'desc'){
        $(this).data('order', 'asc');
        text += ' &#9650';
        sortTable(column,numeric,name);
        
    }
    else{
        $(this).data('order', 'desc');
        text += ' &#9660';
        sortTable(column,numeric,name);     
    }
    $(this).html(text);
});
