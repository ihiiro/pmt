"use strict";document.onreadystatechange=function(){if("complete"===document.readyState){let e=document.querySelectorAll('button[class="unadd"]');for(let t=0,n=e.length;t<n;t++)e[t].addEventListener("click",function(){let n=new XMLHttpRequest,o={id:e[t].getAttribute("USER_ID")};n.onload=function(){if(200==this.status&&"success"==this.responseText){let n=e[t].parentElement.parentElement.getAttribute("USER_ID"),o=document.querySelectorAll('div[USER_ID="'+n+'"');for(let e=0,t=o.length;e<t;e++)o[e].remove()}},n.open("POST","/unadduser",!0),n.setRequestHeader("Content-Type","application/json"),n.send(JSON.stringify(o))})}};