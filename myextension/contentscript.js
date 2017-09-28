alert("Hello! I am an alert box!!");

function postToServer(encodedstr, relUrl){
    var xhr = new XMLHttpRequest();
    var url = "http://127.0.0.1:5000/stackoverflow" + relUrl;
    xhr.open("POST", url, true);
    //console.logs(url);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function() {           //Call a function when the state changes.
            if(xhr.readyState == 4 && xhr.status == 200) {
            console.log(xhr.responseText);
        }
    }
    xhr.send(encodedstr);
}

window.addEventListener('load',function(){
    console.log("DOM loaded");
    var elements = document.getElementsByClassName('question-hyperlink');
    console.log(elements);
    for(var i = 0, len = elements.length; i < len; i++) {
        elements[i].addEventListener("click", function(e){
            var d = new Date();
            console.log(e.srcElement.textContent);
            var timestamp = d.toUTCString();
            var content = e.srcElement.textContent;
            //var nonstr = "url=" + document.URL+"&action=clickupvote&content=" + content + "&timeStamp=" +timestamp;
            //console.log(nonstr);
            var encodedstr = "url=" + encodeURIComponent(document.URL)+"&action=clickquestion&content=" + encodeURIComponent(content) + "&timestamp=" + encodeURIComponent(timestamp);
            console.log(encodedstr);
            console.log("encoded the string");
            postToServer(encodedstr, "/logs");
        });
     
    }

    var elements1 = document.getElementsByClassName('job');
    console.log(elements1);
    for(var i = 0, len = elements1.length; i < len; i++){
        elements1[i].addEventListener("click", function(e){
            var d = new Date();
            var timestamp = d.toUTCString();
            var content = e.srcElement.textContent;
            var encodedstr = "url=" + encodeURIComponent(document.URL)+"&action=clickjob&content=" + encodeURIComponent(content) + "&timestamp=" + encodeURIComponent(timestamp);
            console.log(encodedstr);
            postToServer(encodedstr, "/logs");
            //port.postMessage({ action: 1 , content : element.textContent });
        });
    }

    var elements2 = document.getElementsByClassName('vote-up-off');
    console.log(elements2);
    for(var i = 0, len = elements2.length; i < len; i++){
        elements2[i].addEventListener("click", function(e){
            var d = new Date();
            var timestamp = d.toUTCString();
            var content = ''
            var encodedstr = "url=" + encodeURIComponent(document.URL)+"&action=clickupvote&content=" + encodeURIComponent(content) + "&timestamp=" + encodeURIComponent(timestamp);
            console.log(encodedstr);
            postToServer(encodedstr, "/logs");
            //port.postMessage({ action: 1 , content : element.textContent });
        });
    }
    //var rootelement = document.documentElement;
    //console.log(rootelement);
    //rootelement.addEventListener("scroll", function(){

    //    });
    var tag_elements = document.getElementsByClassName('post-tag');
    console.log(tag_elements);
    for(var i = 0, len = tag_elements.length; i < len; i++){
            tag_elements[i].addEventListener("click", function(e){
            var d = new Date();
            var timestamp = d.toUTCString();
            var content = e.srcElement.textContent;
            var encodedstr = "url=" + encodeURIComponent(document.URL)+"&action=clicktag&content=" + encodeURIComponent(content) + "&timestamp=" + encodeURIComponent(timestamp);
            console.log(encodedstr);
            postToServer(encodedstr, "/logs");
        });
    }

    var url = document.URL;
    var patt = new RegExp("/questions/[0-9]+");
    var res = patt.test(url);
    console.log(res);
    if (res == true){
        p_answer_tags = document.getElementsByClassName("post-text");
        for(var i = 0, len = p_answer_tags.length; i < len; i++){
            p_answer_tags[i].addEventListener("copy", function(e){
                var d = new Date();
                var timestamp = d.toUTCString();
                var content = e.srcElement.innerHTML; 
                var encodedstr = "url=" + encodeURIComponent(document.URL)+"&action=copy&content=" + encodeURIComponent(content) + "&timestamp=" + encodeURIComponent(timestamp);
                console.log(encodedstr);
                postToServer(encodedstr, "/logs");
                
            });
        }   
    }
    else{}



});
