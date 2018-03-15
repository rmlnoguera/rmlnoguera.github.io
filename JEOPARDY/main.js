a = document.getElementById("demo");
  function loadXMLDoc() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        console.log(JSON.parse(this.responseText));
        cats=JSON.parse(this.responseText);

        for (let category of cats)
        {
        	var div = document.createElement("div");
        	div.innerHTML=category.title;
        	div.id="category "+category.id //inputs primary key of category
        	a.appendChild(div);
        	getClues(category.id);
        }
        // console.log("hello");
        // document.getElementById("demo").innerHTML =
        // this.responseText;
      }
    };
    xhttp.open("GET", "http://jservice.io/api/categories?count=5&offset=10", true);
    xhttp.send();
  }

  function getClues(cat_id) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
      	clues=JSON.parse(this.responseText);
      	var column = document.getElementById("category "+cat_id);
      	for (let queue of clues.clues)
      	{
      		// column.innerHTML+=queue.value+"<br>";
      		var div = document.createElement("div");
      		div.classList.add("box");
  	      	div.innerHTML=queue.value;
  	      	div.onclick=function(){
  	      		this.innerHTML=queue.question;
              
  	      		this.onclick=function()
  	      		{
  	      			this.innerHTML=queue.answer;
  	      		}
  	      	}
  	      	column.appendChild(div);
      		}
      	}
    	};
    xhttp.open("GET", "http://jservice.io/api/category?id="+cat_id, true);
    xhttp.send();
}