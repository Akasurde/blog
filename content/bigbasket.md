Title: Canceling BigBasket BBStar membership the hard way
Date: 2020-04-10 12:03
Modified: 2020-04-10 12:03
Category: AngularJS
Tags: webapps, ui, ux, angularjs
Slug: bigbasket-bbstar-membership-revoked
Authors: Abhijeet Kasurde
Summary: In this post, I shared my experience about BigBasket membership cancellation process


On 8th April, 2020, I got a notification that my [BigBasket](https://www.bigbasket.com) BBStar membership got renewed and I was charged for Rs. 299/- for the next six months of membership. I decided not to continue my membership.

I visited BigBasket website and started looking for the option to cancel membership. But to my surprise, I could not find such option. After searching and reading through Quora questions and FAQs section, I realised that I need to install BigBasket Mobile app on my mobile phone and cancel from there. Then I installed BigBasket Android App from Google Play Store and logged in using my credentials.

I tinkered with the App and realised that there is no such option available in the BigBasket app as well. I surprised to see this. I tried to contact BigBasket support team but due to All India lockdown due to COVID-19 situation, I failed miserably.

So, I started looking into the website code which via [Firefox Developer Tools](https://developer.mozilla.org/en-US/docs/Tools) and soon learned that the BigBasket.com is written in AngularJS.

I searched a lot for a button which would trigger the "Cancel the membership" workflow, but could not find such options. I am not sure if this business decision or bad UI/UX decision.
I continued my journey of reading the code and found main app called ["app.min.js"](https://www.bigbasket.com/static/v2263/desktop-web/bbstar/app.min.js). I soon learned that this JS contained all the required code I needed. I added a XHR Breakpoint in Firefox developer tools to stop the ongoing XHR requests for BBStar membership summary info and can debug a bit for more info. I again logged into the app, visited BBStar section and voila !!! I was stopped by breakpoint. This may sound naive but for system developer like me who knew nothing about AngularJS was a moment of truth.

I found a method called "unsubscribeFromBbStar" in the code on line 408, which I was sure, will trigger the "Cancellation" workflow. I went to console section, typed "$scope.unsubscribeFromBbStar()" and hit continue in breakpoint panel. I was greeted with message that you are about to unsubscribe the membership. I clicked "continue" and DONE. I checked my BB wallet and I saw my payment for the membership was refunded in my BB walled account.

![BBWallet Screenshot]({filename}/images/bb/bb_wallet.png)

I learned a lot while doing this programming exercise. BigBasket can take a note that this functionality is not available in their web and mobile application. Thanks for reading this. Cheers.