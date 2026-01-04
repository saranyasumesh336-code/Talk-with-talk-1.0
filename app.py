from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
 <h1>  _______&&_______&&______&&_______&&____ </h1>
            <h1>My First html  Website</h1>
        <body style="text-align:center; font-bont
        :Arial;">
            <h1>Welcome to your self localhost Website</h2>
            <h3>This website is created using Python in Pydroid 3</h3>
            <h4>Made by Student</h3>
            <html>
                <head>
          <h1> this page created all off join this community</h2>
          <h2>hello frends we want</h2><h2>all having and enjoying website this is</h2><h2> you can tolkwith frinds and chat the link is</h2> 
 <h4>@tolkwithtalk.0.0.0/200</h4>
 <h2>click the link and open the dowload and open the app</h2>
 <h2>app review for your command in box and type: your name your email</h2>
 <h1>THANK YOU For Visit this website</h3>
 <h1>___________________________________</h1>




 
  
                    <h0> enter your command</h0>
    
     
  
     
           <h2>_________________________________________</h2>
       <h1>your name       ______       </h1>
       <h1>your email      _______        </h1>
          </head>
       </body>
   </python>
   """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2000)