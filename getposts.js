var FB = require('fb');
var fs = require('fs');
var next = -1;
var params;
var f = fs.createWriteStream('output.txt');
var previous = -2;
FB.setAccessToken('INSERT YOUR OWN ACCESS KEY');
FB.options({timeout: 400});
(function getPage(){
  if(next==-1){
    params = {
      fields:['message']
    };
  }
  else{
    params = {
      fields:['message'],
      until : next.toString()
    };
  }
  var q = FB.api(
    "/2709015299/feed",
    params,
    function(res){
      if(!res || res.error) {
        console.log(!res ? 'error occurred' : res.error);
        console.log('Retrying');
        getPage();
      }
      else{
        for(var i in res.data){
          if(res.data[i].message){
            //f.write('{"post":' +'"'+ res.data[i].message.replace(/\s+/g, ' ').replace(/"/g, "")+ '"' +'}\n');
            f.write(res.data[i].message.replace(/\s+/g, ' ').replace(/"/g, "")+'\n');
          }
        }
        next = res.paging.next.match(/&until=\d*&/).toString().substr(7).slice(0,-1);
        if(previous == next){
          console.log('finished');
          f.end();
          process.exit(code=0)
        }
        else if(next != undefined){
          previous = next;
          console.log(res.paging.next);
          getPage();
        }
        else{
          console.log('finished');
          f.end();
          process.exit(code=0)
        }
      }
    }
  );
}());
