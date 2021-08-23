import whois
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/search")
def search():
  domainName = request.args.get("domain")
  # print(domainName)
  
  try:
    result = whois.whois(domainName)
    # print(result)

    if result.domain_name:
      return render_template("results.html", data=result.items())
    else:
      return render_template("error.html")

  except:
    return render_template("error.html")



  