document.addEventListener('DOMContentLoaded', function() {
   var setMaxButton = document.getElementById('setMax');
   var sortButton = document.getElementById('sortPrice');

   setMaxButton.addEventListener('click', function() {
      chrome.tabs.query({active:true, lastFocusedWindow: true}, tabs => {
         chrome.tabs.update({url: tabs[0].url + "?&max=100"});
      });
   });

   code = `
      // get all the products divs
      products = document.getElementsByClassName('product-list');

      // put prices and names in array. then sort it
      keyValues = [];

      for (i = 0; i < products.length; i++) {
         key = products[i].getElementsByClassName('product-card-grid-container-product-box-name')[0].innerText;

         raw_value = products[i].getElementsByClassName('product-price product-new-price')[0];
         if (raw_value == undefined) {
            raw_value = products[i].getElementsByClassName('product-price_')[0];
            if (raw_value == undefined) {
               str = '99,9' + '\u00a0' + '€';
               raw_value = document.createElement('div');
               raw_value.innerHTML = str;
            }
         }

         raw_value = raw_value.innerHTML.replace(/\&nbsp;/g, " ").split(" ")[0];
         value = parseFloat(raw_value.replace(",", ".")); 

         keyValues.push([ key, value ]);
      }

      keyValues.sort(function compare(kv1, kv2) {
         return kv1[1] - kv2[1];
      });

      keyValues.slice(0, 10);
   `

   sortButton.addEventListener('click', function() {
      chrome.tabs.query({active:true, lastFocusedWindow: true}, tabs => {
         chrome.tabs.executeScript(tabs[0].id, { code }, function(result) {
            for (i = 0; i < result[0].length; i++) {
               document.getElementById(i.toString()).innerText = result[0][i];
            }
         });
      });
   });
}, false);
