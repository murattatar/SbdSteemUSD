﻿######################################################################
# SbdSteemUsd v1
# by Murat Tatar
# December 2017
######################################################################


import os
import requests
import re

def Between(bas,son,cumle):
    b1 = cumle.split(bas)
    b2 = b1[1].split(son)
    ar = b2[0]
    return ar


username = raw_input(u"User Name: ")

print "Getting data..."


size = 120
fcnum = 180

if username =="": username = u"murattatar"
if fcnum =="": fcnum = 6*15-1
if size  =="": size  = 60


fcnum = int(fcnum)
size = int(size)




sli = unicode(str(60+2))
bsli_x = unicode(str(size / 1.2))
bsli_y = unicode(str(size / 4.0))

size = unicode(str(size))



## Steemit Wallet #########################################

url = "https://steemit.com/@"+username+"/transfers"
bring = requests.get(url)
arrival = bring.content



sbd1 = Between('STEEM DOLLARS','UserWallet',arrival)
sbd  = Between('-->$','<!--',sbd1)


steem1 = Between('can be converted to','UserWallet',arrival); 
steem = Between('-->',' STEEM<!',steem1)

sbd = float(sbd)
steem = float(steem)

print steem
print sbd




## BitTrex SBD / Steem #########################################


url = "https://coinmarketcap.com/currencies/steem/#markets"
bring = requests.get(url)
arrival = bring.content


bitSteem1 = Between('Bittrex','Recently',arrival); 
bitSteem2 = Between('price','</td>',bitSteem1); 
bitSteem  = Between('$','</span>',bitSteem2)




url = "https://coinmarketcap.com/currencies/steem-dollars/#markets"
bring = requests.get(url)
arrival = bring.content


bitSbd1 = Between('Bittrex','Recently',arrival); 
bitSbd2  = Between('price','</td>',bitSbd1)
bitSbd   = Between('$','</span>',bitSbd2)


bitSbd = float(bitSbd)
bitSteem = float(bitSteem)

print bitSbd
print bitSteem


print "Calculating..."






html =  u"""<!DOCTYPE html><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /> 
<title>SbdSteem in  USD</title> <head> 
<style class="cp-pen-styles"> 
body, 
html { 
  padding: 0 10px;
  margin: 0;
  background: #0e0f11;
  color: #ecf0f1;
  font-family: "Open Sans", sans-serif;
  min-height: 100vh;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
      -ms-flex-direction: row;
          flex-direction: row;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  width: 95%;
}
* {
}
h1, p { text-align: center;}

html,body{background: url("bg.jpg") no-repeat fixed center; }

a:link,
a:hover,
a:active,
a:visited {
  -webkit-transition: color 150ms;
  transition: color 150ms;
  color: #95a5a6;
  text-decoration: none;
}
a:hover {
  color: #5f5c5d;
  text-decoration: none;


}
.contain { 
	width: auto;
	margin-left: 7%;
	margin-right: 7%;
	
}
.row {
	overflow: auto;
	width: 83%;
	margin-right: auto;
	margin-left: 50px;
}
.row__inner {
	-webkit-transition: 400ms -webkit-transform;
	transition: 400ms -webkit-transform;
	transition: 400ms transform;
	transition: 400ms transform, 400ms -webkit-transform;
	font-size: 0;
	white-space: normal;
	margin: 100px 0;
	padding-bottom: 10px;
}
.tile { white-space: nowrap;
  position: relative;
  display: inline-block;
  width: """ + size + u"""px;
  height: """ + size + u"""px;
  margin-right: 8px;
  font-size: 5px;
  cursor: pointer;
  -webkit-transition: 400ms all;
  transition: 400ms all;
  -webkit-transform-origin: center left;
          transform-origin: center left;
}
.tile__img {border-radius:50%; /* opacity: 0.15; */
  width: """ + size + u"""px;
  height: """ + size + u"""px;
  -o-object-fit: cover;
     object-fit: cover;
}
.tile__details {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  top: 0;
  font-size: 5px;
  opacity: 0;
 /* background: -webkit-linear-gradient(bottom, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 100%);
  background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 100%);*/
  -webkit-transition: 400ms opacity;
  transition: 400ms opacity;
}
.tile__details:after,
.tile__details:before {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  /*display: #000;*/
}
.tile__details:after {
  margin-top: -""" + sli + u"""px;
  margin-left: -""" + sli + u"""px;
  width: """ + size + u"""px;
  height: """ + size + u"""px;
  /* border: 4px solid #ecf0f1; */
  border: 2px solid #06d6a9;
  line-height: 60px;
  text-align: center;
  border-radius: 100%;
  
 
}
.tile__details:before { 
  /* content: "▶"; */
  left: 0;
  width: 100%;
  font-size: 5px;
  margin-left: 7px;
  margin-top: -18px;
  text-align: center;
  /* background: rgba(0,0,0,0.1); */

}
.tile:hover .tile__details { z-index:9999;
  opacity: 1; 
}
.tile__title { text-align:center; color:#06d6a9;
font-size:5px;


  position: absolute;
  bottom: 40%;
  width:100%;
  margin-left:auto; margin-right:auto;
}




.row__inner:hover .tile:hover {
  -webkit-transform: scale(1.7);
          transform: scale(1.7);
  z-index:9999;

  
}




.tile:hover ~ .tile {


  -webkit-transform: scale(.92) translate3d(""" + bsli_x + u"""px, """ + bsli_y + u"""px, 0);
          transform: scale(.92) translate3d(""" + bsli_x + u"""px, """ + bsli_y + u"""px, 0);

}







</style></head><body>


<div class="contain">

  <h1>"""+ username + u"""'s<br> SBDs and STEEMs total value in USD</h1>


<span style="white-space:nowrap">Code</span> by <a style="white-space:nowrap" href="https://steemit.com/@murattatar">Murat Tatar</a>. Suggest by <a href="https://steemit.com/@omeratagun">Ömer Atagün</a>. 
  Effect inspired by <a href="https://codepen.io/joshhunt/pen/LVQZRa">joshhunt</a>. Background by <a href="https://pixabay.com/tr/users/Uki_71-1547363/">Uki_71</a>
  


  
<div class="row__inner">




<div class="tile" onclick="window.open('https://steemit.com/@""" + unicode(username) +u"""','myw');">
      <div class="tile__media">
        <img class="tile__img" src="https://img.busy.org/@""" + unicode(username) + u"""?crop=limit&s=800" />
      </div>
      <div class="tile__details">
        <div class="tile__title">
          <div style="font-size: 12px; position: relative; top: 38px;">""" + unicode(username) + u"""</div>
        </div>
      </div>
    </div>





<div class="tile" onclick="window.open('https://bittrex.com/Market/Index?MarketName=BTC-SBD','myw');">
      <div class="tile__media">
        <div style="font-size: 9px; position: relative;bottom: 30px; left:20px;text-align:center">
""" +unicode(str(sbd))+ u""" SBD = $"""+unicode(str(sbd*bitSbd))+u"""
<br>
""" +unicode(str(steem))+ u""" Steem = $"""+unicode(str(steem*bitSteem))+u"""
<br><br>
Total in USD
<br>
<span style="font-size: 10px; font-weight: 900">$"""+unicode(str((steem*bitSteem)+(sbd*bitSbd)))+u"""</span>

        <div>
      </div>
      <div class="tile__details">
        <div class="tile__title">
          """ + u"""<div style="font-size: 12px; position: relative; top: 40px;">on BitTrex</div>""" + u"""
        </div>
      </div>
    </div>









    </div>





</div>



</body>





</html>"""



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


o = open("SbdSteemUsd.html","w"); o.write(html.encode("utf-8")); o.close()






