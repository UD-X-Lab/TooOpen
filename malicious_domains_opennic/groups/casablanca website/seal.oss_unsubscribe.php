<!DOCTYPE html>
<!-- saved from url=(0031)http://seal.oss/unsubscribe.php -->
<html lang="en" class="js"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

    <!--- basic page needs
    ================================================== -->
    
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Your Brand</title>

    <script>
        document.documentElement.classList.remove('no-js');
        document.documentElement.classList.add('js');
    </script>

    <!-- CSS
    ================================================== -->
    <link rel="stylesheet" href="./seal.oss_unsubscribe_files/stylesUnsub.css">

    
<script src="chrome-extension://dfablgdffinpaeiilgjpebchbacimpoa/eparaksts-page.js"></script></head>
<body data-new-gr-c-s-check-loaded="14.1231.0" data-gr-ext-installed=""><div class="container">
        <div class="inner-container">

        <div class="bottom">
                <h2 class="title">Do you want to unsubscribe?</h2>
                <p class="subtitle">If you unsubscribe, you will stop receiving our weekly newsletter.</p>
        <input type="email" name="Email" id="emailid" class="u-fullwidth text-center" placeholder="Your Email Address" required="">
                        <div class="buttons">

                                <button id="unsubscribe" onclick="unsub()">Unsubscribe</button>
                &nbsp;
                                <button id="go-back" onclick="back()">Go back</button>
                        </div>
            <br>
            <div id="status"></div>
        </div>
</div>

</div>



    <!-- Java Script
    ================================================== -->
        <script>

            const validateEmail = (email) => {
                return email.match(
                    /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                );
                };
           function unsub () {
                email=document.getElementById('emailid').value;
             // If field is required and empty
             if (document.getElementById('emailid').value== '' ) {
                document.getElementById('status').innerText  = 'Please enter an email address.';
             }  

            // If not the right type
            else if (validateEmail(email)) {
                email=document.getElementById('emailid').value;
                document.getElementById('status').innerText = 'Submitting...';
                setTimeout(function() {
                document.getElementById('status').innerText  = 'Your email will be removed from our database within 24 hours';
                const url = new URL(window.location.href);
                url.searchParams.set('email', email);
                window.history.replaceState(null, null, url); // or pushState

                document.getElementById('emailid').value = ''
            }, 1000)
                
            }
            else {
                document.getElementById('status').innerText  =  'Please enter a valid email address.';

        }
     }
           function back() {
            window.location.href= "index.php"
           }

        </script>



</body><grammarly-desktop-integration data-grammarly-shadow-root="true"><template shadowrootmode="open"><style>
      div.grammarly-desktop-integration {
        position: absolute;
        width: 1px;
        height: 1px;
        padding: 0;
        margin: -1px;
        overflow: hidden;
        clip: rect(0, 0, 0, 0);
        white-space: nowrap;
        border: 0;
        -moz-user-select: none;
        -webkit-user-select: none;
        -ms-user-select:none;
        user-select:none;
      }

      div.grammarly-desktop-integration:before {
        content: attr(data-content);
      }
    </style><div aria-label="grammarly-integration" role="group" tabindex="-1" class="grammarly-desktop-integration" data-content="{&quot;mode&quot;:&quot;full&quot;,&quot;isActive&quot;:true,&quot;isUserDisabled&quot;:false,&quot;isAlwaysAvailableAssistantEnabled&quot;:false}"></div></template></grammarly-desktop-integration></html>